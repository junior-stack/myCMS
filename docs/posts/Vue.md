---
date:
    created: 2025-12-01
tags:
  - Programming
---
My note about Vue 3
<!-- more -->

# 1. Set up
## 1.1 Scaffold project
Create template code: `npm create vue@latest`(does not require global dependency)
package dependencies:
```json
{
	"dependencies": {
	    "vue": "^3.5.25"
  },

  "devDependencies": {
    "@vitejs/plugin-vue": "^6.0.2",
    "vite": "^7.2.4",
    "vite-plugin-vue-devtools": "^8.0.5"
  }
}
```
## 1.2 Program entry
Program entry files(calling order from top to below):
- index.html
- main.js
- App.Vue

App level APIs:
- `createApp`:  return `app` instance
- `app.mount`: mount the `app`to a div element
- `app.component`: makes a component available for use anywhere
- `app.use`:
- `app.config.errorhandler`

## 1.3 Config: SSR, CSR
- CSR: Vue by default is CSR, if not configured intentionally
- SSR
	- How to config(project template: https://github.com/vitejs/vite-plugin-vue/blob/main/playground/ssr-vue/index.html):
	1. we maintain `App.vue`. We change the one `main.js` to `server.js` and `client.js`. 
	2. Hydration step: 
		- `server.js`: call `createSSRApp` instead of `createApp` from CSR mode, then call `renderToString` on return result of `createSSRApp`
		- `Client.js`: edit `createSSRApp(app).mount('#app')`
	3. Inside `index.html`, add `<script type="module" src="/src/entry-client.js"></script>`
	- extra support:
		- Nuxt
		- Quarsar
		- Vite SSR
	- Note:
		- Avoid using `window`, `document` API
		- certain lifecycle hooks won't execute: `beforeMount`, `onMount`, `beforeUpdate`, `updated`
		- Put async IO in the hook of `onServerPrefetch` for security when performing them in setup
		- global state: use Pinia. Don't export or share state variables
		- router: use SSR router
		- avoid using `provide/inject` on component. Use `app.provide`
# 2. Vue Syntax

`.vue` file general structure:
```vue
<script>
	// define functions
	// register components method
</script>
<template>
	<!-- Define html components -->
</template>
<style scoped>
	/* customize css for above html */
</style>
```

1. Mustache(double curly braces)
```vue
<script>
	const msg = "hello";
	const ok = 1;
	const rawHtml = '<span style="color: red">This should be red.</span>';
</script>

<template>
	<!-- Mustache parses real-time value of variables/expression
	into plain text in html
 -->
 
	<span>Message: {{ msg }}</span>
	<span>Ok: {{ ok ? 'YES' : 'NO' }}</span>
	<span>{{ rawHtml }}</span>
</template>

```

2. Directives: v-html, v-bind, v-if, v-for, v-on, v-model, v-slot:
```vue fold
<!-- 
1. v-bind: assign variable/expression values to an element's attribute
-->
<button v-bind:disabled="isButtonDisabled">Button</button>
<button :disabled="isButtonDisabled">Button</button>
<!-- dynamic attribute, attr value should be in lower case-->
<button :[attr]="isButtonDisabled">Button</button>
<!-- bind multiple attributes at one time, 
	const objectOfAttrs = {id: 'container', class: 'wrapper', style: 'background-color:green'}
-->
<div v-bind="objectOfAttrs"></div>
<!-- calling function values-->
<time :title="toTitleDate(date)"> {{ formatDate(date) }} </time>

<!--
2. v-on: binds a function to an event or event's modifier,
   syntax: v-on:<Event_Name>[.<Modifier_Name>]="<Function_Name>"
   Event_Name(common): click, mouseover/mouseenter, mouseout/mouseleave, 
					   keydown/keyup/keypress, change, submit, fous/blur, 
					   load/error, scroll
   Mofifier: https://vuejs.org/guide/essentials/event-handling.html
--> 
<a v-on:click="doSomething">Click</a>
<a @click="doSomething">Click</a>
<!-- dynamic event, eventName is a variable, its value should be lowercase 
-->
<a @[eventName]="doSomething">Click</a>
<!-- modifier -->
<form @submit.prevent="onSubmit"><input /></form>

<!-- 
3. v-if: render components based on condition
   v-show: render component but toggle display CSS property based on condition, suitable if you need to toggle to show sth very often
-->
<p v-if='message = "A"'>A</p>
<p v-else-if='message = "B"'>B</p>
<p v-else>C</p>
<p v-show="message === 'A'">You can see me</p>

<!--
4. v-for: render item based on array or object
 -->
 <!-- array: const items = ref([{ message: 'Foo' }, { message: 'Bar' }]) -->
<li v-for="item in items">{{ item.message }}</li>
<!-- object: const myObject = reactive({ title: 'How to do lists in Vue', author: 'Jane Doe', publishedAt: '2016-04-10' }) 
-->
<li v-for="(value, key, index) in myObject">
  {{ index }}. {{ key }}: {{ value }}
</li>
<!-- for range -->
<span v-for="n in 10">{{ n }}</li>
<!-- Note: v-for and v-if cannot be used on same element like this:
	<li v-for="todo in todos" v-if="todo.enable">{{ todo }}</li>
It should be used as following
 -->
<template v-for="todo in todos">
	<li v-if="todo.enable">{{ todo }}</li>
</template>

<!--
5. v-model: bind the value of input html elements to a variable, can be used for <input>, <textarea>, <select>, more can be found: https://vuejs.org/guide/essentials/forms.html
 -->
<input v-model="message" />
<textarea v-model="message" />
<select v-model="selected">
	<option :value="{ number: 123 }">123</option>
</select>
```

# 3. Vue Components

## 3.1 Option vs Composition
Vue has 2 syntax styles(difference of the two styles: https://vuejs.org/guide/introduction.html#api-styles):
- Option API
- Composition API(used in this note)
## 3.2 States management
Component maintain state variables for rendering. Whenever state variables are changed, Vue rerender the components. The state variables are usually set by events triggered by user interactions on the UI.

Create states with `ref`:
```vue
<script setup>
// declare state variable and set state hooks
import { ref } from "vue"

// declare state variable
const count = ref(0)

// set state
function increment(){
	count.value++;
}
</script>

<template>
	<!-- Note: use count instead of count.value below -->
	<button @click="increment"> {{ count }}</button>
</template>
```
create states with `reactive`:

## 3.3 computed method
Vue uses `computed` to create computed properties of the components. Whenever we have complicated expressions or call functions that rely on state variables or other variables, we can put them in computed properties. The benefit of this is that whenever the components render, computed properties cache these expressions and vue does not need to re-evaluate these expressions if their dependencies(i.e: state variables) does not change during this render.

`Compute` example:
```vue
<script setup>
import { reactive, computed } from 'vue'

const author = reactive({
  name: 'John Doe',
  books: [
    'Vue 2 - Advanced Guide',
    'Vue 3 - Basic Guide',
    'Vue 4 - The Mystery'
  ]
})

// use1: publishedBooksMessage is cached if author is not changed
const publishedBooksMessage = computed(() => {
  return author.books.length > 0 ? 'Yes' : 'No'
})

// use2: compute properties can reuse previous value
const publishedBooksMessage = computed({
	// be aware: don't make get return previous the first time to load
	//           publishedBooksMessage
	get(previous){
		if(author.books.length > 0)
			return author.books.length < 100 ? 'Yes' : 'No'
		return previous
	}
})
</script>

<template>
  <p>Has published books:</p>
  <span>{{ publishedBooksMessage }}</span>
</template>
```

## 3.4 watch method
`watch` creates callback behavior when a state variable changes. The callback behavior includes: manipulate DOM, change another state, perform async operations. The first argument of `watch` can be ref, reactive, getter function or an array of previous types, the second argument is a function or async function. `watch` callback by default happens  **after** parent component updates (if any), and **before** the owner component's DOM updates.

```vue
<script setup>
const x = ref("hello world")
const y = reactive({ y: 0})

// 1. single ref
watch(x, (newX, oldX) => {
	console.log(`newX: ${newX}, oldX: ${oldX}`)
})

// 2. reactive object
watch(y, (newY, oldY) => {
	console.log(`newY: ${newY.y}`)
})
// only watch a specific field of y, trigger if y.y is replaced
watch(()=>y.y, (newY, oldY) => {
	console.log(newY)
})
// say y.y is an object, this triggers if y.y mutates and not just replaced
watch(()=>y.y, (newY, oldY) =>{
	console.log(newY)
}, {deep: true})

// 3. getter method, can contain state/props/computed variables
watch(
	()=> x.value + y.y.toString(),
	(curr, prev) => console.log(curr)
)

// 4. array of sources
watch([x, ()=> y.y], ([newX, newY])=>{
	console.log(`x is ${newX}, y is ${newY}`)
})

// 5. async hook
watch(()=> y.y, async (newY, oldY)=>{
	x.value = "loading";
	try{
		const res = await fetch('https://yesno.wtf/api')
		x.value = (await res.json()).answer
	}catch(err){
		x.value = "hello world";
	}
})

// 6. 3rd arg: immediate
//    by default, watch callback executes only when watched source changes, we can force callback to be executed right after the watched source is created in addition to when it changes by passing immediate
watch(x, (newX, oldX) => {
	console.log(`newX: ${newX}, oldX: ${oldX}`)
}, { immediate: true })

// 7. 3rd arg: once
//   make watch callback executes only once when watched souce changes
watch(x,(newValue, oldValue) => {
},{ once: true })

</script>
```

`watchEffect`: automatically track callback dependencies instead of having to explicily maintain in `watch`. It's equivalent to pass `{immediate: true}` into `watch`. It can be more efficient then `watch` when there are multiple dependency variables and we track properties within these variables.
```vue
<script setup>
// can track state variables/props/computed variables
watchEffect(async () => {
	const response = await fetch(`https://jsonplaceholder.typicode.com/todos/${y.y}`)
})
	x.value = await response.json();
</script>

```

## 3.5 useTemplateRef
`useTemplateRef` allows us to reference a specific element within the current component in javascript. We can only use this reference variable after the component is mounted(i.e: we can use it in `onMount` or callbacks in `watch`)

Reference element within current component:
```vue
<script setup>
import { useTemplateRef, onMounted } from 'vue'

// 2. reference the element through reference name in useTemplateRef
const input = useTemplateRef('my-input')

onMounted(() => {
  // 3. Use the reference in onMounted hook
  input.value.focus()
})
</script>

<template>
	<!-- 1. define the reference name within the ref attribute -->
  <input ref="my-input" />
</template>
```

Reference element within child component(use `defineExpose`):
- child component:
```vue
<script setup>
import { useTemplateRef } from 'vue'

// 2. reference the element through reference name in useTemplateRef
const myInput = useTemplateRef('my-input')

// 3. Expose the ref
defineExpose({
  myInput
})
</script>

<template>
	<!-- 1. define the reference name within the ref attribute -->
  <input ref="my-input" />
</template>
```
- parent component:
```vue
<script setup>
import { useTemplateRef, onMounted } from 'vue'

// 5. reference the element through reference name in useTemplateRef
const childRef = useTemplateRef('child-ref')

// 6. Use the childcomponent input reference in onMount
onMounted(()=>{
	const childComponentInput = childRef.value.myInput
	input.value.focus()
})

</script>

<template>
	<!-- 4. define the reference name within the ref attribute -->
  <ChildComponent ref="child-ref" />
</template>
```

Reference element within parent component: impossible with `useTemplateRef`
## 3.6 control parent component
In order to control the parent component behavior from child component or set the state of parent component or let parent component execute something, we can create an event on child component and bind the event with a function from parent component. Then we control when to emit events inside child component to trigger.

Example: we want to create a toggle button that can control the theme of the layout
- toggle button(child component):
```vue
<script setup>
const emit = defineEmits(['colorToggle'])

function toggleColor(){
	emit("colorToggle")
}
</script>
<template>
	<button @click="toggleColor">
		Enable Night Mode
	</button>
</template>
```
- Layout(parent component):
```vue
<script setup>
const isNightMode = ref(false)

function enableNightMode(){
	isNightMode.value = !isNightMode.value
}
</script>
<template>
	<div>
		{{ isNightMode ? "Night" : "Day" }}
	</div>
	<ToggleButton @colorToggle="enableNightMode" />
</template>
```

pass arguments to events:
- child:
```vue
<script setup>
const emit = defineEmits(['my-custom-event'])

function emitEvent(){
	const payload = { msg: "hello" }
	emit("my-custom-event", payload )
}
</script>
<template>
	<button @click="emitEvent">Emit</button>
</template>
```
- parent:
```vue
<script setup>

function eventHandler(payload){
	console.log(payload)
}
</script>
<template>
	<div>
		{{ isNightMode ? "Night" : "Day" }}
	</div>
	<ChildComponent @my-custom-event="eventHandler" />
</template>
```
## 3.7 Props & Expose
When we pass parameters from parent to child:
- parent:
```vue
<template>
	<ChildComponent :foo="'hello world'" />
</template>
```
- child:
```vue
<script setup>
const props = defineProps(['foo'])
watch(()=> props.foo, (newFoo) => console.log(newFoo))
</script>
```

When we pass parameters from chilld to parent:
- child:
```vue
<script setup>
const msg = ref("hello world")
defineExpose({ msg })
</script>
```
- parent:
```vue
<script setup>
import { useTemplateRef, onMounted } from 'vue'
const childRef = useTemplateRef('child-ref')
onMounted(()=>{
	const msg = childRef.value.msg
})

</script>

<template>
  <ChildComponent ref="child-ref" />
</template>
```

## 3.8 Life hook

- onMounted: hook after the the vue component is mounted, can take sync/async hook, commonly used to fetch api for data when page is loading, add event listener to window
- onUnmounted: hook after the vue component is unmounted
- onUpdated: hook after state change but before DOM updates on page in browser
- nextTick: hook after the DOM updates on page in browser

order of hook:
onMounted(parent) -> onMounted(children)

## 3.9 Slot
Parents can pass html elements into children components for rendering through slots.

Basic:
- childComponent:
```vue
<template>
	<!-- slot pair will be replaced by html elements passed by parent-->
	<button><slot>defalt content</slot></button>
</template>
```
- parent component:
```vue
<template>
	<!-- pass msg value-->
	<ChildComponent>{{ msg }}</ChildComponent>
	<!-- pass Html -->
	<ChildComponent>
		<span>Hello world</span>
	<ChildCompnent>
	<!-- when pass nothing, anything appears inside slot will appear-->
	<ChildComponent />
</template>
```

Multiple slots:
- children:
```vue
<template>
  <div class="card">
    <div v-if="$slots.header" class="card-header">
      <slot name="header" />
    </div>
    
    <div v-if="$slots.default" class="card-content">
      <slot />
    </div>
    
    <div v-if="$slots.footer" class="card-footer">
      <slot name="footer" />
    </div>
  </div>
</template>
```
- parent:
```vue
<template>
	<ChildrenComponent>
		<template v-slot:header>
			<!-- Content for header slot -->
		</template>
	</ChildrenComponent>
	<ChildrenComponent>
		<template #header>
			<!-- Content for header slot -->
		</template>
	</ChildrenComponent>
	<ChildrenComponent>
	  <template #header>
	    <h1>Here might be a page title</h1>
	  </template>
	
	  <!-- implicit default slot -->
	  <p>A paragraph for the main content.</p>
	  <p>And another one.</p>
	
	  <template #footer>
	    <p>Here's some contact info</p>
	  </template>
	</ChildrenComponent>
</template>
```

## 3.10 provide/inject
provide/inject is the way to set shared data for all of its descendant components(not just parent/child) to access. It saves the need to pass props when there is a long chain between an ancestor and descendant.

- Ancestor Component(use `provide` to provide data to all its descendant)
```vue
<script setup>
import { provide, ref } from 'vue'
// first arg is key to retrieve in descendant, second arg is value
provide('key1','hello!')

const counter = ref(0)
function updateCounter(){
	counter.value += 1
}
// classic use
provide('key2', { counter, updateCounter})
</script>
```
- descendant(use `inject` to retrieve the keys from `provide`)
```vue
<script setup>
import { inject } from 'vue'

const { counter, updateCounter } = inject('key2')
</script>

<template>
  <button @click="updateCounter">{{ counter }}</button>
</template>
```

## 3.11 Components with async setup
## 3.12 Async Component
When we use `defineAsyncComponent`, we typically use it with `import()` function to lazy load heavy components. `import()`makes network request to retrieve the components' javascript bundle when the component is rendered combining with `v-if`(when condition of `v-if` is true). On the other hand, if we use `import ... from '...'` to load the component, we always load the heavy components eagerly when the page is loading. Some use cases of `AsyncComponent`:
- heavy components with `v-if` condition to be false or not immediately visible when loading the page
- router page that is not loaded.

Use Case 1(defer loading heavy):
- LoadingComponent:
```vue fold
<template>
  <div class="loading-overlay">
    <div class="loader"></div>
  </div>
</template>

<style scoped>
.loading-overlay {
/* Position the overlay fixed to cover the entire viewport */
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
 /* Set background color to gray with some opacity */
	background-color: rgba(128, 128, 128, 0.5); /* Gray with 50% opacity */
 /* Ensure it is on top of all other content */
	z-index: 9999;
 /* Center the loader within the overlay */
	display: flex;
	justify-content: center;
	align-items: center;
}
/* Optional: Add a simple CSS spinner */
.loader {
  border: 8px solid #f3f3f3; /* Light gray border */
  border-top: 8px solid #3498db; /* Blue border for the spinner effect */
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
```
- use asynComponent:
```vue fold
<script setup>
import { ref } from "vue"
import LoadingComponent from "./Components/LoadingComponent"

const loadingStatus = ref(false)

function updateloadingStatus(){
	loadingStatus.value = !loadingStatus.value
}

const HeavyComponent = defineAsyncComponent({
	loader: () => import("./Components/HeavyComponent"),
	loadingComponent: LoadingComponent
})
</script>
<template>
	<HeavyComponent v-if="loadingStatus" />
	<button @click="loadingStatus">Load</button>
</template>
```

use case 2(router):
```vue fold
<script setup>
import { defineAsyncComponent } from 'vue';

const AsyncAbout = defineAsyncComponent({
  loader: () => import('./views/About.vue'),
  loadingComponent: { template: '<div>Loading About...</div>' }, // Optional loading component
  errorComponent: { template: '<div>Error loading About!</div>' }, // Optional error component
  delay: 200, // Optional delay before showing loading component (ms)
  timeout: 3000 // Optional timeout for loading (ms)
});

const router = createRouter({
  history: createWebHistory(),
  routes: [
	{
	  path: '/',
	  name: 'Home',
	  component: () => import('./views/Home.vue')
	},
	{
	  path: '/about',
	  name: 'About',
	  component: AsyncAbout // Using the defined async component
	}
  ]
});

export default router;
</script>
```

Use case 3(use with `<Suspense>`):
Suppose we have a component nested with different async components or components with async setup. Without Suspense, we will see each components loading spinner at a time when each of them handle their loaded state. The `<Suspense>` component gives us the ability to display top-level loading / error states while we wait on these nested async dependencies to be resolved.
```vue
<script setup>
import AsyncSetUpComponent from "./Components/AsyncSetUpComponent"
const HeavyComponent = defineAsyncComponent({
	loader: () => import("./Components/HeavyComponent"),
	loadingComponent: LoadingComponent
})
</script>
<template>
	<Suspense>
		<!-- below elements go to default slot of Suspense -->
		<AsyncSetUpComponent />
		<HeavyComponent />
		
		<!-- loading go to fallback slot of Suspense-->
		<template #fallback> Loading... </template>
	</Suspense>
</template>
```
# 4. Built-in Components
## 4.1 `<Component>`

## 4.2 `<Suspense>`

# 5. Other classes
## 5.1 Composable function
Composable functions can encapsulate anything you defined in vue `<script setup>`, including state variables, computed properties, ref elements, prop variable, lifecycle hook, watched callback, customized functions. And they can return state variables & customized functions.

Commonly, we create composable functions to take a state variable as input and use watch method to watch that input variable. Examples like fetching data from a url below:
- composable function:
```vue
<script setup>
import { ref, watchEffect, toValue } from 'vue'

export function useFetch(url) {
  const data = ref(null)
  const error = ref(null)
  const fetchData = () => {
    // reset state before fetching..
    data.value = null
    error.value = null

    fetch(toValue(url))
      .then((res) => res.json())
      .then((json) => (data.value = json))
      .catch((err) => (error.value = err))
  }

  watchEffect(() => {
    fetchData()
  })

  return { data, error }
}
</script>
```
- calling composable functions:
```vue
<script setup>
const url = ref('/initial-url')

const { data, error } = useFetch(url)

// this should trigger a re-fetch due to watchEffect inside
url.value = '/new-url'
</script>
```

## 5.2 Custom directive
We create custom directive when we want to manipulate a specific DOM directly. We typically define it to focus on an element, integrate with a library that manipulates DOM(charting lib, make an element drag and drop), add event handling.

More: https://vuejs.org/guide/reusability/custom-directives.html
# 6. Vue Router


# 7. Pinia
Pinia is the newest library that has replaced Vuex. Pinia can implement a global store across the entire application where every components can access. Without Pinia, we can still implement this global store, but it may not work in SSR environment.


# 8. Passive attributes
## 8.1 Fallthrough attributes

