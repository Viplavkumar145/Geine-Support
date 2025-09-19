#!/bin/bash

# Secure Environment Setup Script
echo "🔒 Setting up secure environment..."

# Check if .env exists
if [ ! -f "backend/.env" ]; then
    echo "📝 Creating .env from template..."
    cp backend/.env.example backend/.env
    echo "✅ .env file created from template"
    echo "⚠️  Please edit backend/.env and add your actual API keys"
else
    echo "✅ .env file already exists"
fi

# Verify .env is in .gitignore
if grep -q "backend/.env" .gitignore; then
    echo "✅ .env is properly ignored by git"
else
    echo "❌ WARNING: .env is NOT in .gitignore!"
fi

# Check git status
echo "📊 Git status:"
git status --porcelain | grep -E "\.(env|key)" || echo "✅ No sensitive files staged"

echo "🎉 Environment setup complete!"
echo "💡 Remember: Never commit your .env file to git!"