#!/bin/bash

# Render Setup Script for Geine-Support Backend
echo "🚀 Setting up Geine-Support Backend for Render..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Verify installation
echo "✅ Verifying installation..."
python -c "import fastapi; print('FastAPI:', fastapi.__version__)"
python -c "import google.generativeai; print('Gemini API: Ready')"

# Check environment variables
echo "🔧 Checking environment variables..."
if [ -z "$GEMINI_API_KEY" ]; then
    echo "⚠️  Warning: GEMINI_API_KEY not set"
else
    echo "✅ GEMINI_API_KEY configured"
fi

if [ -z "$MONGO_URL" ]; then
    echo "⚠️  Warning: MONGO_URL not set"
else
    echo "✅ MONGO_URL configured"
fi

echo "🎉 Setup complete! Starting server..."
exec python -m uvicorn server:app --host 0.0.0.0 --port ${PORT:-8000}