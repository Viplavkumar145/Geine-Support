# 🚀 Vercel Deployment Guide for Geine-Support Frontend

## 📋 Your Backend is Ready!
✅ Backend URL: `https://geine-support-backend.onrender.com`
✅ Backend deployed successfully on Render

## 🎯 Next: Deploy Frontend to Vercel

### Step 1: Test Your Backend
First, let's verify your backend is working:

```bash
# Health check
curl https://geine-support-backend.onrender.com/api/health

# Test chat
curl -X POST https://geine-support-backend.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello", "session_id": "test", "brand_tone": "friendly"}'
```

### Step 2: Update Backend CORS Settings

In your Render dashboard, add/update these environment variables:

```env
CORS_ORIGINS=https://your-frontend-domain.vercel.app,https://your-custom-domain.com
```

### Step 3: Deploy Frontend to Vercel

1. **Go to [vercel.com](https://vercel.com)**
   - Sign up/Login with GitHub
   - Click "New Project"

2. **Import Repository**
   - Select your `geine-support` repository
   - Click "Import"

3. **Configure Project**
   ```
   Framework Preset: React
   Root Directory: frontend
   Build Command: npm run build
   Output Directory: build
   Install Command: npm install
   ```

4. **Environment Variables**
   Add this environment variable:
   ```
   REACT_APP_BACKEND_URL=https://geine-support-backend.onrender.com
   ```

5. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Your frontend will be live!

### Step 4: Update Backend CORS

After getting your Vercel URL (e.g., `your-app.vercel.app`):

1. Go to Render dashboard
2. Navigate to your backend service
3. Go to Environment tab
4. Update `CORS_ORIGINS`:
   ```
   CORS_ORIGINS=https://your-app.vercel.app,https://www.your-app.vercel.app
   ```

### Step 5: Custom Domain (Optional)

1. **In Vercel:**
   - Go to Project Settings → Domains
   - Add your custom domain
   - Follow DNS configuration instructions

2. **Update Backend CORS:**
   ```
   CORS_ORIGINS=https://your-custom-domain.com,https://www.your-custom-domain.com
   ```

## 🔧 Troubleshooting

### Common Issues:

1. **CORS Errors**
   ```
   Error: Access blocked by CORS policy
   Solution: Update CORS_ORIGINS in Render with your Vercel domain
   ```

2. **API Not Found**
   ```
   Error: 404 on API calls
   Solution: Verify REACT_APP_BACKEND_URL is correct
   ```

3. **Build Fails**
   ```
   Error: Build command failed
   Solution: Ensure package.json has correct scripts
   ```

## 📊 Deployment URLs

After deployment, you'll have:
- **Backend**: `https://geine-support-backend.onrender.com`
- **Frontend**: `https://your-app.vercel.app`
- **Custom Domain**: `https://yourdomain.com` (optional)

## ✅ Final Checklist

- [ ] Backend deployed on Render ✅
- [ ] Frontend deployed on Vercel
- [ ] CORS configured correctly
- [ ] Environment variables set
- [ ] Custom domain configured (optional)
- [ ] SSL certificates active (automatic)
- [ ] All features tested in production

## 🎉 Success!

Once completed, your AI customer support platform will be live and accessible worldwide!

### Test Your Live Application:
1. Visit your Vercel URL
2. Go to Live Chat
3. Send a message
4. Verify AI responses work
5. Test knowledge base upload
6. Check analytics dashboard

---

Your complete AI support platform is now ready for customers! 🌟