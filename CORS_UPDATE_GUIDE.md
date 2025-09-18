# 🚨 CRITICAL: CORS Update Required for New Vercel URL

## Problem Identified:
Your Vercel URL changed from:
- **Old**: `https://geine-support-git-main-viplav-kumars-projects.vercel.app`
- **New**: `https://geine-support.vercel.app`

But your backend CORS configuration still only allows the old URL!

## Current Error:
```
Access to XMLHttpRequest at 'https://geine-support-backend.onrender.com/api/analytics' 
from origin 'https://geine-support.vercel.app' has been blocked by CORS policy: 
No 'Access-Control-Allow-Origin' header is present on the requested resource.
```

## ⚡ IMMEDIATE ACTION REQUIRED:

### Step 1: Update CORS in Render Backend
1. **Go to**: https://render.com/dashboard
2. **Select**: `geine-support-backend` service
3. **Click**: Environment tab
4. **Find**: `CORS_ORIGINS` variable
5. **Update to**:
   ```
   http://localhost:3000,http://127.0.0.1:3000,https://geine-support-git-main-viplav-kumars-projects.vercel.app,https://geine-support.vercel.app
   ```
6. **Save Changes** (triggers auto-redeploy)

### Step 2: Verify Required Environment Variables in Render
Ensure these are set:
- `CORS_ORIGINS` = `http://localhost:3000,http://127.0.0.1:3000,https://geine-support-git-main-viplav-kumars-projects.vercel.app,https://geine-support.vercel.app`
- `GEMINI_API_KEY` = `AIzaSyD6Woh8quth0dFw6l4RTdG9pFgTPhdtyro`
- `AI_PROVIDER` = `gemini`
- `PORT` = `8000`
- `ENV` = `production`

### Step 3: Verify Vercel Environment Variable
1. **Go to**: https://vercel.com/dashboard
2. **Select**: `geine-support` project
3. **Settings** → **Environment Variables**
4. **Verify**: `REACT_APP_BACKEND_URL` = `https://geine-support-backend.onrender.com`

## Testing After Fix:
1. **Wait 3-5 minutes** for Render redeploy
2. **Clear browser cache** (Ctrl+Shift+R)
3. **Test**: https://geine-support.vercel.app/
4. **Check console**: Should see successful API calls

## Expected Results:
- ✅ No CORS policy errors
- ✅ Analytics loads successfully
- ✅ Knowledge base loads successfully  
- ✅ Chat functionality works
- ✅ All API endpoints return data

---
**CRITICAL**: Update CORS_ORIGINS in Render IMMEDIATELY to fix this issue!