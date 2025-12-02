---
date:
    created: 2025-11-11
draft: true
tags:
  - Programming
---
<!-- more -->
# 1. Defend search engine Crawler





# 2. Authentication

## 2.1 Authenticate with firebase

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