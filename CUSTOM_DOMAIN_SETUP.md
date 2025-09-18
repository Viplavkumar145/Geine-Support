# 🌐 Custom Domain Setup Guide: geinesupport.com

## Current Status:
- **Current URL**: https://geine-support.vercel.app/
- **Target Custom Domain**: https://geinesupport.com
- **Backend**: https://geine-support-backend.onrender.com

## 📋 Domain Setup Steps:

### Step 1: Configure Domain in Vercel

1. **Go to Vercel Dashboard**: https://vercel.com/dashboard
2. **Select your project**: `geine-support`
3. **Go to Settings** → **Domains**
4. **Add Custom Domain**:
   - Enter: `geinesupport.com`
   - Enter: `www.geinesupport.com` (optional)
5. **Click "Add"**

### Step 2: DNS Configuration at Your Domain Provider

**You need to add these DNS records at your domain registrar:**

#### For Root Domain (geinesupport.com):
```
Type: A
Name: @
Value: 76.76.19.19
TTL: 3600
```

#### For WWW Subdomain (www.geinesupport.com):
```
Type: CNAME
Name: www
Value: cname.vercel-dns.com
TTL: 3600
```

### Step 3: Update Environment Variables

#### A. Update Backend CORS (Render):
1. **Go to**: https://render.com/dashboard
2. **Select**: `geine-support-backend`
3. **Environment tab** → Update `CORS_ORIGINS`:
   ```
   http://localhost:3000,http://127.0.0.1:3000,https://geine-support.vercel.app,https://geinesupport.com,https://www.geinesupport.com
   ```

#### B. Update Frontend Environment (Vercel):
1. **Vercel Dashboard** → **Settings** → **Environment Variables**
2. **Verify**: `REACT_APP_BACKEND_URL` = `https://geine-support-backend.onrender.com`

### Step 4: SSL Certificate (Automatic)
- Vercel automatically provisions SSL certificates
- Usually takes 5-10 minutes after DNS propagation
- You'll get HTTPS automatically

## 🧪 Testing Checklist:

### After Domain Setup:
1. **Wait for DNS propagation** (30 minutes to 24 hours)
2. **Test domain access**: 
   - https://geinesupport.com
   - https://www.geinesupport.com
3. **Test API functionality**:
   - Live Chat
   - Analytics loading
   - Knowledge base loading

### Browser Console Tests:
```javascript
// Test 1: Check backend connectivity
fetch('https://geine-support-backend.onrender.com/api/analytics')
  .then(r => console.log('Status:', r.status))
  .catch(e => console.error('Error:', e));

// Test 2: Check environment variable
console.log('Backend URL:', process.env.REACT_APP_BACKEND_URL);
```

## 🚨 Common Issues & Solutions:

### Issue 1: "This domain is not configured"
- **Solution**: DNS records not propagated yet. Wait 2-4 hours.

### Issue 2: CORS Errors with New Domain
- **Solution**: Ensure backend CORS_ORIGINS includes new domain.

### Issue 3: SSL Certificate Not Working
- **Solution**: Wait for Vercel SSL provisioning (5-10 minutes).

## 📞 Domain Provider Instructions:

### Popular Providers:
- **GoDaddy**: DNS Management → Add Records
- **Namecheap**: Advanced DNS → Add New Record  
- **Cloudflare**: DNS → Add Record
- **Google Domains**: DNS → Custom records

### Step-by-Step for Any Provider:
1. Login to domain registrar
2. Find "DNS Management" or "DNS Settings"
3. Add the A and CNAME records above
4. Save changes
5. Wait for propagation

## 🎯 Expected Timeline:
- **Vercel Configuration**: 5 minutes
- **DNS Propagation**: 30 minutes - 24 hours
- **SSL Certificate**: 5-10 minutes after DNS
- **Full Functionality**: Within 24 hours

## 🔍 Verification Commands:
```bash
# Check DNS propagation
nslookup geinesupport.com

# Check SSL certificate
curl -I https://geinesupport.com
```

---
**Note**: Keep both domains (vercel.app and custom) working during transition!