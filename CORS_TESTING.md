# 🧪 CORS Testing Instructions

## Test API Connectivity from Browser Console

1. **Open your site**: https://geine-support.vercel.app/
2. **Open browser console** (F12 → Console tab)
3. **Run these test commands** one by one:

### Test 1: Check Analytics API
```javascript
fetch('https://geine-support-backend.onrender.com/api/analytics', {
  method: 'GET',
  headers: {
    'Origin': 'https://geine-support.vercel.app'
  }
})
.then(response => {
  console.log('Analytics Response Status:', response.status);
  console.log('Analytics Response Headers:', [...response.headers.entries()]);
  return response.text();
})
.then(data => console.log('Analytics Data:', data))
.catch(error => console.error('Analytics Error:', error));
```

### Test 2: Check Knowledge Base API
```javascript
fetch('https://geine-support-backend.onrender.com/api/knowledge-base', {
  method: 'GET',
  headers: {
    'Origin': 'https://geine-support.vercel.app'
  }
})
.then(response => {
  console.log('Knowledge Base Response Status:', response.status);
  console.log('Knowledge Base Response Headers:', [...response.headers.entries()]);
  return response.text();
})
.then(data => console.log('Knowledge Base Data:', data))
.catch(error => console.error('Knowledge Base Error:', error));
```

### Test 3: Check Backend Health
```javascript
fetch('https://geine-support-backend.onrender.com/', {
  method: 'GET',
  headers: {
    'Origin': 'https://geine-support.vercel.app'
  }
})
.then(response => {
  console.log('Backend Health Status:', response.status);
  console.log('Backend Health Headers:', [...response.headers.entries()]);
  return response.text();
})
.then(data => console.log('Backend Health Data:', data))
.catch(error => console.error('Backend Health Error:', error));
```

## Expected Results:

### ✅ If CORS is Fixed:
- Status: 200 OK
- Headers include: `access-control-allow-origin: https://geine-support.vercel.app`
- Data returns successfully

### ❌ If CORS Still Broken:
- Status: Failed to fetch
- Error: CORS policy blocked
- No `access-control-allow-origin` header

## Next Steps:
1. Run these tests in browser console
2. Share the results with me
3. Based on results, we'll know if CORS update worked

---
**CRITICAL**: If tests still fail, CORS_ORIGINS was not updated in Render!