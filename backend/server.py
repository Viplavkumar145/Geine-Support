import os
import logging
import uuid
import time
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from openai import OpenAI
from pydantic import BaseModel

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / ".env")

# --------------------------------------------------
# Setup logging
# --------------------------------------------------
logging.basicConfig(level=logging.INFO)

# --------------------------------------------------
# Pydantic Model for chat requests
# --------------------------------------------------
class ChatRequest(BaseModel):
    message: str

# --------------------------------------------------
# FastAPI App Initialization
# --------------------------------------------------
def create_app() -> FastAPI:
    app = FastAPI()

    # CORS
    origins = os.environ.get("CORS_ORIGINS", "http://localhost:3000").split(",")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Environment Vars
    mongo_url = os.environ.get("MONGO_URL")
    db_name = os.environ.get("DB_NAME", "supportgenie")
    openai_api_key = os.environ.get("OPENAI_API_KEY")

    # Setup MongoDB
    if mongo_url:
        try:
            mongo_client = AsyncIOMotorClient(mongo_url)
            app.state.db = mongo_client[db_name]
            logging.info("✅ Connected to MongoDB")
        except Exception as e:
            logging.error(f"❌ MongoDB connection failed: {str(e)}")
            app.state.db = None
    else:
        logging.warning("⚠️ No MONGO_URL provided. Running without DB.")
        app.state.db = None

    # Setup OpenAI client
    if not openai_api_key:
        logging.warning("⚠️ No OPENAI_API_KEY set. AI responses will fallback.")
        app.state.openai = None
    else:
        app.state.openai = OpenAI(api_key=openai_api_key)

    # --------------------------------------------------
    # Routes
    # --------------------------------------------------

    @app.get("/")
    async def root():
        return {"message": "🚀 SupportGenie backend is running!"}

    @app.post("/chat")
    async def chat(request: Request, payload: ChatRequest):
        user_message = payload.message.strip()
        if not user_message:
            raise HTTPException(status_code=400, detail="Message cannot be empty")

        session_id = str(uuid.uuid4())
        db = request.app.state.db
        client = request.app.state.openai

        start_time = time.perf_counter()

        # Default fallback if OpenAI is not configured or fails
        ai_text = "AI service is unavailable. A human agent will assist you."
        escalate = True
        latency = 0.0

        if client is not None:
            try:
                completion = await client.chat.completions.acreate(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are SupportGenie AI assistant. Respond politely and helpfully."},
                        {"role": "user", "content": user_message},
                    ],
                    temperature=0.7,
                )
                ai_text = completion.choices[0].message.content
                escalate = False
                latency = time.perf_counter() - start_time
            except Exception as e:
                logging.error(f"❌ OpenAI API call failed: {str(e)}")
                ai_text = "Our AI service is unavailable. A human agent will assist you."
                escalate = True
                latency = 0.0

        # Save chat to MongoDB if connected
        if db is not None:
            try:
                await db.chats.insert_one(
                    {
                        "session_id": session_id,
                        "user_message": user_message,
                        "ai_response": ai_text,
                        "escalate": escalate,
                        "latency": latency,
                        "timestamp": time.time(),
                    }
                )
            except Exception as e:
                logging.error(f"❌ Failed to save chat in MongoDB: {str(e)}")

        return {"response": ai_text, "escalate": escalate, "latency": latency}

    @app.get("/health")
    async def health():
        return {"status": "ok"}

    return app


# --------------------------------------------------
# Uvicorn Entrypoint
# --------------------------------------------------
app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
