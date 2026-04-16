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
- Uvicorn(ASGI server specifically for python application)

## 2.2 Dynamic web server

## 2.3 Web build system
- vite
- webpack
- RScore

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
Cors error is the error arised by browser's CORS policies.  Browsers enforce a security measure called the Same-Origin Policy. This policy prevents a web page from making requests to a different domain, port, or protocol than the one it originated from, leading to Cross-Origin Resource Sharing (CORS) errors. 

To summarize, when the web page downloaded from the web page server requests an api url that does not target to web page server, you will see a COR error message in the console `Access to fetch at 'http://localhost:58058/Admin/User/Login' from origin 'http://localhost:3000' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.`
### 5.1.1 Frontend proxy
When your frontend makes a request to a relative URL, the proxy intercepts it and forwards it to the specified target server (e.g., `http://localhost:8080/api/data`). Here are the proxy config for different build tools:

```Javascript group:5.1.1 file:Webpack
// config/index.js
module.exports = {
	dev: {
		proxyTable: {
			'/api': {
				target: '<backend_api_url>',
				changeOrigin: true,
				pathRewrite: { '^/api': '' },
			}
		}
	}
}

// config/dev.env.js
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
	NODE_ENV: '"development"',
	// process.env.BASE_API becomes "/api/", when you call fetch, it will send request to "/api/<module_name>/<API>"
	BASE_API: '"/api/"'
})

// direct webpack config: build/webpack.dev.conf.js
const config = require('../config')
const devWebpackConfig = merge(baseWebpackConfig,{
	devServer: {
		proxy: config.dev.proxyTable
	},
	plugins: [
		new webpack.DefinePlugin({
	      'process.env': require('../config/dev.env')
	    }),
	]
}
```
```Javascript group:5.1.1 file:Vite
// vite.config.js
export default defineConfig({
	server: {
		port: 3000,
		open: true,
		proxy: {
			'/': {
				target: '<backend_url>',
				changeOrigin: true,
				// rewrite: (path) => path.replace(/^\/api/, ''),
			}
		}
	}
})
```


When you set the proxy server, browser sees the request as being made to the same origin(your frontend's development server) and there is no Same-Origin Policy on the proxy server on that port

This method is primarily for development and may not be suitable for production environments without a proper reverse proxy setup.

### 5.1.2 Backend Access-Control-Allow-Origin
This is a server-side solution where the server you are trying to access explicitly allows requests from specific origins (or all origins with `*`). The server then responds with the `Access-Control-Allow-Origin` header indicating which origins are permitted.
expressjs:
```javascript
app.use(cors())
```



# 5. SEO
## 5.1 How to find SEO score
https://www.youtube.com/watch?v=8OcWDOpkb7U

# 6. Defend search engine Crawler





# 7. Authentication

## 7.1 Authenticate with firebase

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