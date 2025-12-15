---
date:
    created: 2025-11-11
draft: true
tags:
  - Programming
---
<!-- more -->
# 1. Some theories

## 1.1 SPA
## 1.2 SSR vs SSG vs CSR


# 2. Tool
## 2.1 Static web server
- Windows IIS
- Apache
- Niginx

## 2.2 Dynamic web server

## 2.3 Web build system
- vite
- webpack

## 2.4 How to debug Nodejs

## 2.5 Load balance

| Tier     | Layer       | method                    |
| -------- | ----------- | ------------------------- |
| Basic    | Application | Nginx                     |
|          |             | DNS load balancer         |
| Medium   | Transport   | LVS(linux virtual server) |
| Advanced |             | F5(hardware)              |



# 3. JS Native API
## 3.1 DOM API
- windows
- document

## 3.2 Inject background process

# 4. Default behavior in HTML
## 4.1 event propagation
Event bubbling: Simply speaking, event bubbling means when a specific event of a child DOM element(not child component) is triggered, the event handlers of all its ancestors elements(not ancestor component) will also be triggered. Below is an example of event bubbling in reactjs:
```jsx
function Button({ onClick, children }) {
  return (
    <button onClick={onClick}>
      {children}
    </button>
  );
}
// when clicking a button, the event handler of the toolbar will also be triggered
function Toolbar(){
	return (
		<div className="Toolbar" onClick={()=>alert("Toolbar")}>
			<Button onClick={()=>alert("Playing")}>Play</Button>
			<Button onClick={()=>alert("Upload")}>Upload</Button>
		</div>
	)
}
```

# 5. Common error
## 5.1 CORS error
Cors error is the error arised by browser's CORS policies.
### 5.1.1 Frontend proxy
When your frontend makes a request to a relative URL, the proxy intercepts it and forwards it to the specified target server (e.g., `http://localhost:8080/api/data`).

How does this work:
browsers enforce a security measure called the Same-Origin Policy. This policy prevents a web page from making requests to a different domain, port, or protocol than the one it originated from, leading to Cross-Origin Resource Sharing (CORS) errors. 
Package.json(react):
```json
"proxy": 8080
```
When you set the proxy server, browser sees the request as being made to the same origin(your frontend's development server) and there is no Same-Origin Policy on the proxy server on that port

This method is primarily for development and may not be suitable for production environments without a proper reverse proxy setup.

### 5.1.2 Backend Access-Control-Allow-Origin
This is a server-side solution where the server you are trying to access explicitly allows requests from specific origins (or all origins with `*`). The server then responds with the `Access-Control-Allow-Origin` header indicating which origins are permitted.
expressjs:
```javascript
app.use(cors())
```

### 5.1.3 CORS error from oidc
A CORS (Cross-Origin Resource Sharing) error with an OIDC (OpenID Connect) client typically occurs when a web application hosted on one domain attempts to communicate with an OIDC Identity Provider (IdP) or an API on a different domain, and the browser's security policy, known as the Same-Origin Policy, blocks the request. This happens because the server (IdP or API) has not explicitly granted permission for the client's origin to access its resources.

Common Scenarios and Solutions:

- **IdP Configuration Issues:**
    - **Incorrect Redirect URIs:** Ensure the `redirect_uri` configured in your OIDC client matches exactly (including scheme, host, and port) with what is registered on the OIDC IdP. Mismatches are a frequent cause of CORS-related issues during the authentication flow.
    - **Missing or Incorrect CORS Headers on IdP:** The IdP's `/authorize` or token endpoints might not be sending the necessary `Access-Control-Allow-Origin` header in their responses, or the value in the header might not include the client's origin. The IdP's configuration needs to be adjusted to allow requests from your client's domain.
    
- **API Access Issues:**
    
    - **Backend API CORS Configuration:** If your OIDC client is making calls to a separate backend API after authentication, that API also needs to be configured for CORS. The API server must include the `Access-Control-Allow-Origin` header (and potentially `Access-Control-Allow-Methods` for preflight requests) in its responses to allow your client's origin.
    - **Preflight Requests (OPTIONS):** For certain HTTP methods (e.g., PUT, DELETE, POST with specific content types), browsers send a preflight `OPTIONS` request before the actual request. The API server must handle these `OPTIONS` requests and respond with the appropriate CORS headers.

# 5. Defend search engine Crawler





# 6. Authentication

## 6.1 Authenticate with firebase

1. Go to Firebase console > create new project

2. Project Settings > Your app in your project > web > register app name > copy the `firebaseConfig`(ex below):

   ```javascript
   import { initializeApp } from "firebase/app";
   
   const firebaseConfig = {
     apiKey: "AIzaSyB8ii648W088_BIFpgucYADOdAmNJHrVlY",
     authDomain: "uniblock-dashboard.firebaseapp.com",
     projectId: "uniblock-dashboard",
     storageBucket: "uniblock-dashboard.firebasestorage.app",
     messagingSenderId: "637843188854",
     appId: "1:637843188854:web:b5a882dc988135c9cc8357"
   };
   
   const app = initializeApp(firebaseConfig);
   ```

3. Console dashboard > side pannel > **Build** > **Authentication **> sign with email/password or Google