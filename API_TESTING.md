# 🧪 API Testing Commands

## Test Analytics Endpoint
curl -X GET "https://geine-support-backend.onrender.com/api/analytics" \
  -H "Origin: https://geine-support-git-main-viplav-kumars-projects.vercel.app"

## Test Knowledge Base Endpoint  
curl -X GET "https://geine-support-backend.onrender.com/api/knowledge-base" \
  -H "Origin: https://geine-support-git-main-viplav-kumars-projects.vercel.app"

## Test Chat Endpoint (POST)
curl -X POST "https://geine-support-backend.onrender.com/api/chat" \
  -H "Content-Type: application/json" \
  -H "Origin: https://geine-support-git-main-viplav-kumars-projects.vercel.app" \
  -d '{
    "message": "Hello, test message",
    "session_id": "test_session_123", 
    "brand_tone": "friendly"
  }'

## Test CORS Preflight (OPTIONS)
curl -X OPTIONS "https://geine-support-backend.onrender.com/api/chat" \
  -H "Origin: https://geine-support-git-main-viplav-kumars-projects.vercel.app" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: Content-Type" \
  -v

# Expected Results:
# ✅ Status: 200 OK
# ✅ Headers include: Access-Control-Allow-Origin
# ✅ No CORS errors
# ✅ Valid JSON responses