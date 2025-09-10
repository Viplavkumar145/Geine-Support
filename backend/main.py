import os
import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from emergent.sdk import LlmChat, UserMessage
from motor.motor_asyncio import AsyncIOMotorClient
import uuid

# --------------------------------------------------
# Setup logging
# --------------------------------------------------
logging.basicConfig(level=logging.INFO)

# --------------------------------------------------
# FastAPI App Initialization
# --------------------------------------------------
app = FastAPI()

# CORS Settings
origins = os.environ.get("CORS_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Environment Variables
# --------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
DB_NAME = os.environ.get("DB_NAME", "supportgenie")
EMERGENT_LLM_KEY = os.environ.get("EMERGENT_LLM_KEY")

# --------------------------------------------------
# MongoDB Connection (Safe Mode)
# --------------------------------------------------
db = None

if MONGO_URL:
    try:
        mongo_client = AsyncIOMotorClient(MONGO_URL)
        db = mongo_client[DB_NAME]
        logging.info("✅ Connected to MongoDB")
    except Exception as e:
        logging.error(f"❌ MongoDB connection failed: {str(e)}")
        db = None
else:
    logging.warning("⚠️ No MONGO_URL provided. Running without database.")

# --------------------------------------------------
# Helper: AI Response with Safe Fallback
# --------------------------------------------------
async def get_ai_response(message: str, session_id: str):
    api_key = EMERGENT_LLM_KEY

    # ✅ Fallback if no API key
    if not api_key:
        logging.warning("⚠️ No EMERGENT_LLM_KEY found. Using fallback response.")
        return (
            "AI service is not configured. Let me connect you with a human agent.",
            True,
            0.0,
        )

    system_message = (
        "You are SupportGenie AI assistant. Respond politely and helpfully to customer queries."
    )

    try:
        chat = (
            LlmChat(
                api_key=api_key,
                session_id=f"supportgenie_{session_id}",
                system_message=system_message,
            )
            .with_model("openai", "gpt-4o")
        )

        user_message = UserMessage(text=message)
        response = await chat.send_message(user_message)

        if not response:
            raise ValueError("Empty response from AI")

        return response.text, False, response.latency if hasattr(response, "latency") else 0.0

    except Exception as e:
        logging.error(f"❌ LLM service failed: {str(e)}")
        return (
            "Our AI service is temporarily unavailable. A human agent will assist you shortly.",
            True,
            0.0,
        )

# --------------------------------------------------
# WebSocket Chat Endpoint
# --------------------------------------------------
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    session_id = str(uuid.uuid4())
    logging.info(f"Client {client_id} connected with session {session_id}")

    try:
        while True:
            data = await websocket.receive_text()
            logging.info(f"📩 Received from {client_id}: {data}")

            ai_response, escalate, latency = await get_ai_response(data, session_id)

            # ✅ Save chat to Mongo (if available)
            if db:
                try:
                    await db.chats.insert_one(
                        {
                            "client_id": client_id,
                            "session_id": session_id,
                            "user_message": data,
                            "ai_response": ai_response,
                            "escalate": escalate,
                            "latency": latency,
                        }
                    )
                except Exception as e:
                    logging.error(f"❌ Failed to save chat in MongoDB: {str(e)}")

            await websocket.send_json(
                {
                    "response": ai_response,
                    "escalate": escalate,
                    "latency": latency,
                }
            )

    except WebSocketDisconnect:
        logging.info(f"🔌 Client {client_id} disconnected")
    except Exception as e:
        logging.error(f"❌ Unexpected error: {str(e)}")
        await websocket.close()

# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------
@app.get("/")
async def root():
    return {"message": "🚀 SupportGenie backend is running!"}
