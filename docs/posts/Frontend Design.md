---
date:
    created: 2025-12-16
draft: true
tags:
  - Design
---
My note about UI layouts, css
<!-- more -->

# 1. Layout design

## 1.1 Home page layout


# 2. basic CSS

# 3. CSS framework

# 4. Frontend Effects

## 4.1 Input throttle
**Debounce源码:**

[https://blog.csdn.net/qq_53030983/article/details/123106233](https://blog.csdn.net/qq_53030983/article/details/123106233)

**Debouce使用:**

一个输入框条件查询。每次输入一次调用一次服务查询。这样时间长消耗大。我们就可以使用 函数防抖 (只执行最后一次) 执行最后一次调用。减小服务开销。防抖函数的逻辑是设置一个时间间隔,忽略时间间隔里的任何输入变化,然后执行回调

vue:
```vue fold
<script>  
 export default {  
     data() {  
         return {  
             number:0,  
         }  
     },  
     methods: {  
         // number 验证  
         NumberInput: debounce(function (value) {  
             if (value && value.toString().includes(".")) {  
                 if (value.toString().split(".")[1].length > 4) {  
                     this.number = this.toFixed(value, 4)  
                 }  
             }  
         }, 100),  
         toFixed(number, fractionDigits) {  
             var times = Math.pow(10, fractionDigits);  
             var roundNum = Math.round(number * times) / times;  
             return roundNum.toFixed(fractionDigits);  
         },  
     }  
 }  
     /**  
      * 函数节流  
      * @param fn  
      * @param interval  
      * @returns {Function}  
      * @constructor  
      */  
     function Throttle(fn, t) {  
         let last;  
         let timer;  
         let interval = t || 500;  
         return function () {  
             let args = arguments;  
             let now = +new Date();  
             if (last && now - last > interval) {  
                 clearTimeout(timer);  
                 timer = setTimeout(() => {  
                     last = now;  
                     fn.apply(this, args);  
                 }, interval);  
             } else {  
                 last = now;  
                 fn.apply(this, args);  
             }  
         };  
     }  
     /**  
      * 函数防抖 (只执行最后一次点击)  
      * @param fn  
      * @param delay  
      * @returns {Function}  
      * @constructor  
      */  
     function debounce(fn, t) {  
         let delay = t || 500;  
         let timer;  
         return function () {  
             let args = arguments;  
             if (timer) {  
                 clearTimeout(timer);  
             }  
             timer = setTimeout(() => {  
                 timer = null;  
                 fn.apply(this, args);  
             }, delay);  
         };  
     }  
 </script>
 <template>
	 <input v-model.number="number" @input="NumberInput" style="width: 200px">
 </template>
```

## 4.2 progress bar for upload/download

## 4.3 Parallex Effect

## 4.4 Hover in text