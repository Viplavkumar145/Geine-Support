# Deployment Guide

## 📊 **Live Application**
- **Frontend**: https://geine-support.vercel.app/ ✅
- **Backend**: https://geine-support-backend.onrender.com ✅
- **Custom Domain**: geinesupport.com

---

## 🌐 **Frontend (Vercel)**
- **Platform**: Vercel
- **Framework**: React
- **Environment**: `REACT_APP_BACKEND_URL=https://geine-support-backend.onrender.com`

## 🔧 **Backend (Render)**
- **Platform**: Render.com
- **Runtime**: Python 3.11
- **Environment Variables**:
  ```env
  GEMINI_API_KEY=your_api_key
  AI_PROVIDER=gemini
  ENV=production
  MONGO_URL=your_mongodb_url
  CORS_ORIGINS=https://geine-support.vercel.app,https://geinesupport.com
  ```

---

## 🧪 **Testing**
```bash
# Health check
curl https://geine-support-backend.onrender.com/api/health

# Test chat API
curl -X POST https://geine-support-backend.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello", "session_id": "test", "brand_tone": "friendly"}'
```

**🎉 Your AI Customer Support Platform is live!**

## 🌐 Deploying Geine-Support to Production

This guide covers different deployment options for your Geine-Support application.

### 🔧 Deployment Options

#### Option 1: Vercel (Frontend) + Railway/Render (Backend)
**Best for: Small to medium applications**

1. **Frontend (Vercel)**
   - Push your code to GitHub
   - Connect Vercel to your repository
   - Set build command: `cd frontend && npm run build`
   - Set output directory: `frontend/build`

2. **Backend (Railway/Render)**
   - Connect your GitHub repository
   - Set start command: `cd backend && python -m uvicorn server:app --host 0.0.0.0 --port $PORT`
   - Add environment variables from `.env.example`

#### Option 2: Netlify (Frontend) + Heroku (Backend)
**Best for: Quick deployment**

1. **Frontend (Netlify)**
   - Connect GitHub repository
   - Build command: `cd frontend && npm run build`
   - Publish directory: `frontend/build`

2. **Backend (Heroku)**
   - Add `Procfile`: `web: cd backend && python -m uvicorn server:app --host 0.0.0.0 --port $PORT`
   - Set Python buildpack
   - Configure environment variables

#### Option 3: Docker Deployment
**Best for: Full control and scalability**

```dockerfile
# Frontend Dockerfile (frontend/Dockerfile)
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
FROM nginx:alpine
COPY --from=0 /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# Backend Dockerfile (backend/Dockerfile)
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 🌍 Custom Domain Setup

#### For Vercel:
1. Go to your project settings
2. Add your custom domain
3. Configure DNS records:
   ```
   Type: A
   Name: @
   Value: 76.76.19.61
   
   Type: CNAME
   Name: www
   Value: cname.vercel-dns.com
   ```

#### For Netlify:
1. Site settings → Domain management
2. Add custom domain
3. Configure DNS:
   ```
   Type: A
   Name: @
   Value: 75.2.60.5
   
   Type: CNAME
   Name: www
   Value: your-site-name.netlify.app
   ```

### 📋 Pre-Deployment Checklist

- [ ] Remove debugging console.log statements
- [ ] Update CORS origins for production domain
- [ ] Set up MongoDB Atlas (production database)
- [ ] Configure environment variables for production
- [ ] Test all API endpoints
- [ ] Set up SSL certificate (automatic with most platforms)
- [ ] Configure error logging and monitoring

### 🔒 Production Environment Variables

```env
# Production .env
MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/supportgenie
GEMINI_API_KEY=your_production_gemini_key
AI_PROVIDER=gemini
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
ENV=production
PORT=8000
```

### 🚀 Performance Optimization

1. **Frontend Optimization**
   - Enable React production build
   - Configure CDN for static assets
   - Enable compression

2. **Backend Optimization**
   - Set up connection pooling for MongoDB
   - Configure proper logging
   - Set up health checks

3. **Database Optimization**
   - Use MongoDB Atlas clusters
   - Set up proper indexing
   - Configure backup strategies

### 📊 Monitoring & Analytics

1. **Application Monitoring**
   - Set up error tracking (Sentry)
   - Configure performance monitoring
   - Set up uptime monitoring

2. **Analytics**
   - Google Analytics for frontend
   - API usage analytics
   - User behavior tracking

### 🔧 Troubleshooting Common Issues

1. **CORS Errors**
   - Update CORS_ORIGINS in backend .env
   - Ensure protocol matches (http/https)

2. **Database Connection**
   - Verify MongoDB Atlas IP whitelist
   - Check connection string format

3. **API Key Issues**
   - Verify Gemini API key is active
   - Check API quota limits

4. **Build Failures**
   - Ensure all dependencies are in package.json
   - Check Node.js/Python versions

### 📞 Support

For deployment issues, check:
- Platform-specific documentation
- Community forums
- GitHub issues

Remember to update your DNS records and allow 24-48 hours for full propagation.