---
date:
    created: 2025-12-05
tags:
  - Programming
---
My note about Reactjs 17+
<!-- more -->

# 1. Set up

## 1.1 Scaffold template
React templates can be created through the following commands(these commands do not require global dependencies installation):
- `npx create-next-app@latest`: react template integrate with `next.js`
- `npx create-react-router@latest`: template paired with react router and vite
- `npx create-expo-app@latest`: template that create Android, IOS & web app. It provides SDK for React Native
- `npm install --save-dev parcel && npm create parcel react-client my-react-app`
- `npm create vite@latest my-app -- --template react-ts`
- `npx create-rsbuild --template react`

`npx create-next-app@latest` dependencies: can choose js/ts
```json
{
  "dependencies": {
    "next": "16.0.6",
    "react": "19.2.0",
    "react-dom": "19.2.0"
  },

  "devDependencies": {
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "babel-plugin-react-compiler": "1.0.0",
    "eslint": "^9",
    "eslint-config-next": "16.0.6",
    "typescript": "^5"
  }
}
```

`npx create-react-router@latest` dependencies: only ts options
```json
{
	"dependencies": {
	    "@react-router/node": "^7.9.2",
	    "@react-router/serve": "^7.9.2",
	    "isbot": "^5.1.31",
	    "react": "^19.1.1",
	    "react-dom": "^19.1.1",
	    "react-router": "^7.9.2"
  },

  "devDependencies": {
    "@react-router/dev": "^7.9.2",
    "@tailwindcss/vite": "^4.1.13",
    "@types/node": "^22",
    "@types/react": "^19.1.13",
    "@types/react-dom": "^19.1.9",
    "tailwindcss": "^4.1.13",
    "typescript": "^5.9.2",
    "vite": "^7.1.7",
    "vite-tsconfig-paths": "^5.1.4"
  }
}
```

`npx create-expo-app@latest`:


## 1.2 Migrate from react-scripts
Previous projects package config:
```json
{
	"devDependencies": {
		"react-scripts": "^4.0.3"
	},
	"scripts": {
		"start": "react-scripts start",
		"build": "react-scripts build"
	}
}
```

Steps of migration:
1. `npm uninstall react-scripts && npm install vite @vitejs/plugin-react --dev`
2. add `vite.config.js` to the folder of `package.json`:
```js file:vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true,
    proxy: {
      '/api': {
	       target: 'http://localhost:8082', // backend url
	       changeOrigin: true,
	       // rewrite: (path) => path.replace(/^\/api/, '')
      },
    },
  },
  build: {
    outDir: 'build',
    assetsDir: 'assets',
    sourcemap: true,
  },
  // resolve: {
  //  alias: {
  //    '@': '/src',
  //  },
  //}
});
```
3. edit `package.json`:
```json
{
	"scripts": {
		"start": "vite",
		"build": "vite build",
		"serve": "vite preview"
	}
}
```
4. Move `index.html` from `public/` to root folder, fix any import inside `index.html` and add this line: `<script type="module" src="/src/index.jsx"></script>` after `<div id="root">`
5. rename all `.js` files to `.jsx`
6. Rename all env variables with prefix of `React_` to `Vite_`
7. replace `process.env` to `import.meta.env`

## 1.3 Core components
Core libraries:
- React
- React-dom

Build Tools(any one of below can be used to bundle and build react code):
- Vite: fast for building
- Parcel: easy to use
- Rsbuild: suitable for performance
- Webpack: classic bundler in conjunction with Babel

pipelines: ts compile > react build > js code

build tool config:
- ts/js
- CSR support
- SSR Support
- SSG
- RSC

## 1.4 Program entry
```jsx group:1.4 file:index.jsx
import App from "./App.jsx"
import { createRoot } from "react-dom/client"

const root = createRoot(document.getElementById("root))
root.render(<App />)
```

## 1.5 Config CSR vs SSR
CSR: React not using nextjs by default is CSR

SSR(2 ways to config SSR):
- Scaffold the project using nextjs command from section 1.1
- Manual

SSR has 2 ways to render component(either hydrate or use RSC architecture):
- hydration for manual setup: https://medium.com/simform-engineering/how-to-implement-ssr-server-side-rendering-in-react-18-e49bc43e9531
- RSC architecture for manual: https://thefrontenddev.medium.com/getting-started-with-react-server-components-rsc-react-19-and-next-js-in-action-7093448ee5f0

# 2. React syntax
pass variable/expression to html part with `{}`
```jsx
export default function Profile() {  
	return (  
			<Avatar  
				person={{ name: 'Lin Lanying', imageId: '1bX5QH6' }}  
				size={100}  
			/>  
		);  
}
```

list render: use `filter` or `map`
```jsx
const people = [
  'Creola Katherine Johnson: mathematician',
  'Mario José Molina-Pasquel Henríquez: chemist',
  'Mohammad Abdus Salam: physicist',
  'Percy Lavon Julian: chemist',
  'Subrahmanyan Chandrasekhar: astrophysicist'
];

export default function List() {
  const listItems = people.map(person =>
    <li>{person}</li>
  );
  return <ul>{listItems}</ul>;
}
```

conditional render: use `&&`, `<cond> ? va1 : val2`, `if/else`
```jsx
export default function Item({name, isPacked}){
	if(name === "")
		return null
	return (
		<li className="item">
	      {isPacked ? (
	        <strong>
	          {name}
	        </strong>
	      ) : (
	        <p> {name} </p>
	      )}
	    </li>
	)
}
```
# 3. React Components

## 3.1 How to declare component
```jsx
export default function myComponent(){
	// javascript code
	return (<>
		<!-- content of myComponent -->
	</>)
}
```

## 3.2 React Hooks
### 3.2.1 useState vs useReducer
**useState:** `useState` creates a state variable and a simple setter for that variable. When the setter is called, it triggers rerender
```jsx
export default function myComponent(){
	const [index, setIndex] = useState(0)
	
	return (<>
		index: {index}
	</>)
}
```

Note:
- `setState` from `useState` only changes the value after the next `render()` takes place, which means if you print out the value right after `setState` within a function/event handler(whether sync/async), the state value will still be the previous value before inputting in the `setState`

**useReducer:** define more complicated logic of updating a state that `useState` for re-rendering. `useReducer` takes a regular variable as initial state and a function that can updates the state variable based on different action. When you call `dispatch`, it will trigger rerender.
```jsx fold
const tasks = [
  { id: 0, text: 'Visit Kafka Museum', done: true },
  { id: 1, text: 'Watch a puppet show', done: false },
  { id: 2, text: 'Lennon Wall pic', done: false }
];
let nextId = 3;
function tasksReducer(tasks, action){
	switch(action.type) {
		case 'add': {
			return [...tasks,
				{
					id: action.id,
					text:action.text
					done: false
				}
			]
		},
		case 'change': {
			return tasks.map(t => {
				return t.id === action.task.id ? action.task : t
			});
		},
		case 'deleted': {
			return tasks.filter(t => t.id !== action.id)
		},
		default: {
	      throw Error('Unknown action: ' + action.type);
	    }
	}
}

export default function TaskApp(){
	function handleAddTask(text){
	    dispatch({
	      type: 'added',
	      id: nextId++,
	      text: text,
	    });
	}

	function handleChangeTask(task) {
		dispatch({
		  type: 'changed',
		  task: task
		});
	}

	function handleDeleteTask(taskId) {
		dispatch({
		  type: 'deleted',
		  id: taskId
		});
	}
	
	return (
	<>
		<h1>Prague itinerary</h1>
		<AddTask
			onAddTask={handleAddTask}
		/>
		<TaskList
			tasks={tasks}
			onChangeTask={handleChangeTask}
			onDeleteTask={handleDeleteTask}
		/>
	</>
	)
	
}
```

### 3.2.2 useMemo & UseCallback
**UseMemo:**
`UseMemo` allows us to cache a value when components rerender. Components only recreated the values returned by `useMemo` when the variables inside dependency array change.  It can save heavy computation of certain values when the component rerender is triggered by parent component. The first arg is a callback that does not accept input(typically synchronous) and the second arg is dependency array that contains either state, props or variables from other `useMemo`
```jsx
export default function TaskList({ taskList }){
	const [ filter, setFilter] = useState("")
	
	const filteredTasks = useMemo(() => {
		return taskList.filter(t =>
			t.name.toLowerCase().includes(filter.toLowerCase())
		)
	}, [filter, taskList])
}
```

**UseCallback:**
By default, methods defined inside a component are recreated on every render. To optimize this, we can first move the methods outside and make it public, but sometimes the methods may contain state variables of this component and need to perform actions. Therefore, we can use `useCallback` to optimize. `useCallback` caches the either sync or async methods to avoid recreating functions unless its specified dependencies changed. This can help if we pass the function to a child component because when parent component re-renders, it won't create new function and pass to the props of child component to make it re-render every time. 
Use it when:
- pass the function to a child component
- the method is used in `useEffect`
- your created function needs to create a lot of variables/resources

**How to use:** The first arg of `useCallback` can be either a function or async function that can return anything and the second is a dependencies array.
```jsx
export default function ProductPage({productId, referrer}){
	const handleSubmit = useCallback((orderDetails) => {
		fetch(baseUrl + "/product" + productId, {
			method: "POST",
			headers: {
				"Content-Type": "application/json"
			},
			body: JSON.stringify({referrer, orderDetails})
		})
	}, [productId, referrer])
	
	// we can also create a method that only renders after initial render
	const handleSubmit = useCallback((orderDetails) => {
		fetch(baseUrl + "/product" + productId)
	}, [])
}
```

### 3.2.3 useEffect vs useLayoutEffect

**useEffect:** `useEffect()` is like `watch` method from Vue or commonly used to fetch and load data. The first argument is a function that returns nothing(cannot be async function but supports async operation, see the example of how to call async function below). The second arg can be either no argument, `[]`, `[dep]`:
- no arg: `useEffect` runs the callback each time the component renders
- `[]`: runs only once after the initial render(mount), typically used to perform async ops
- `[dep]`: runs after the initial render and whenever any variables inside `[dep]` change, `[dep]` stores props, state variables, returned variables from `useCompute` or `useCallback`functions. If you are using certain methods, you must pass that method into `[dep]`
```jsx
// 2 ways to perform asyn operations in useEffect:

// 1. (1) define async in useEffect callback
//    (2) use the await result inside the defined callback
const [data, setData] = useState("")
useEffect(() => {
	// 1.1 define async func
	const fetchData = async () => {
		const response = await fetch("https://yourapi.com")
		const json = await response.json()
		setData(json)
	}
	
	// 1.2. call async func
	fetchData().catch(e => console.error(e));
}, [])

// 2. we can move the async func outside into useCallback
const [data, setData] = useState("")
// 2.1
const fetchData = useCallback(async () => {
	const data = await fetch("https://www.api.com")
	setData(data)
}, [])
// 2.2 call fetchData and pass fetchData into [dep] of useEffect
useEffect(()=>{
	fetchData().catch(e => console.error(e))
}, [fetchData])
```

**useLayoutEffect:**`useLayoutEffect` first arg accepts synchronous function with synchronous operations. `useLayoutEffect` happens before browser paint the component, while `useEffect` happens after painting. 

**When to use:** 
Sometimes, a component's size and position is dynamic and not known until you render it because it has children props.With this hook, we can know the exact size and position before painting and rerender the component based on the exact size and location. 

In this example(https://react.dev/reference/react/useLayoutEffect), since `ToolTipContainer` has children props. We can only know the height of `ToolTipContainer` after we know what exactly is passed as children to render and we need to render `ToolTipContainer` based on its height. Thus, we need to use `useLayoutEffect` in this case.

### 3.2.4 useRef
`useRef(initialValue)` itself returns a mutable object with a single property called `current` whose initial value is set to `initialValue`. This object does not trigger re-render. It can be passed to `ref` attribute of an html element to track and access the dom element and use with browser APIs like `focus`, `scrollIntoVies`, `play`, `select` and so on.

```jsx
import { useRef } from 'react';

export default function Form() {
  // step 1
  const inputRef = useRef(null);

  function handleClick() {
    inputRef.current.focus();
  }

  return (
    <>
	  <!-- step 2-->
      <input ref={inputRef} />
      <button onClick={handleClick}>
        Focus the input
      </button> 
    </>
  );
}
```

## 3.3 Special Component

### 3.3.1 RSC in SSR
Note: When you enable SSR mode and choose **RSC architecture** in react, there are 2 types of components:
- Server Component(by default)
- Client Component(declared by `"use client"`)

Server Component: Servers render Server Components into html on server side. Best used when the component needs to load or fetch static resources remotely or access the resources on the server locally(rather than have to fetch server resources from client) because the server can load the resources during the build process of server components.  Some notes about server components
- cannot use hooks like `useState`
- but can nest Client components inside to use react hooks
- support **async component**

Client Component key notes: 
- client components are like regular components in CSR mode
- can use **server functions** to let server execute

> [!warning]+ Nesting with each other
>- server component cannot be imported in a file declared with `"use Client"`, otherwise, it will be treated as client component
>- solution is to pass server component in props


| pattern                      | supported | How                                                                                     |
| ---------------------------- | --------- | --------------------------------------------------------------------------------------- |
| Client inside server         | yes       | direct import                                                                           |
| Server inside client(import) | no        | it forces server component to be client component                                       |
| Server inside client(props)  | yes       | Pass the Server Component as `children` or another prop from a parent Server Component. |

How to setup and create RSC components: https://thefrontenddev.medium.com/getting-started-with-react-server-components-rsc-react-19-and-next-js-in-action-7093448ee5f0


## 3.4 Common pattern

### 3.4.1 Props & Expose
**Props:** In order for parent component to trigger children component's rerender through UI interactions of parent component, we lift the state into parent component and pass this state to children component to make children component re-render. This is called props down. Below is example of how to pass props from parent to children:
```jsx group:3.7 file:ChildComponent.jsx
function ChildComponent(props) {
	return (<>
		<h2> {props.msg} </h2>
	</>)
}
```
```jsx group:3.7 file:ParentComponent.jsx
import ChildComponent from './ChildComponent';

function ParentComponent(){
	const [msg, setMsg] = useState("")
	
	return (
		<ChildComponent msg={msg} />
		
		<!-- users control ChildComponent through Input at parent-->
		<Input onChange={(e)=> setMsg(e.target.value)} />
	)
}
```

special props

| properties | role                                                                                     |
| ---------- | ---------------------------------------------------------------------------------------- |
| key        | when new key is passed to a component's prop, the component will reset its states values |
| children   | this prop receives slot elements for this component                                      |
| className  | assign css classes                                                                       |
| style      | assign inline style object                                                               |
| ref        | assign return value of `useRef` to this property to access DOM                           |

style keys:

| category   | key                   | role                                                                        |
| ---------- | --------------------- | --------------------------------------------------------------------------- |
| Layout     | display               | Defines the rendering box type(ex: `'flex'`, `'grid'`, `'block'`, `'none'`) |
|            | margin/padding        | Sets external and internal spacing                                          |
|            | width/height          | Sets dimension                                                              |
|            | position              | position element(ex: `'absolute'`, `'relative'`, `'fixed'`)                 |
|            | top,right,bottom,left | Used with position                                                          |
| Flexbox    | flexDirection         | Specifies the direction of flex items(ex: `'row'`, `'column'`)              |
|            | justifyContent        | Aligns items along the main axis(ex: `'center'`, `'space-between'`)         |
|            | alignItems            | Aligns items along the cross axis(ex: `'flex-start'`, `'stretch'`)          |
|            | flex                  | growth and shrinkage                                                        |
| Visual     | Color                 | Sets text color                                                             |
|            | backgroundColor       | Sets the background color of the element                                    |
|            | borderRadius          | Rounds the corners of the element's outer border.                           |
|            | border                | Sets the width, style, and color of the border                              |
|            | opacity               | Sets the transparency level from 0 to 1                                     |
|            | boxshadow             | add shadow effect                                                           |
| Typography | fontSize              | set the size of font                                                        |
|            | fontWeight            | set thickness of characters                                                 |
|            | fontFamily            | font family                                                                 |
|            | textAlign             | horizontal alignment for text (e.g., `'center'`, `'right'`)                 |


**Expose:** There is no expose method in react as defined in vue.

### 3.4.2 Emit events
In order for child component to trigger parent component's re-render through UI interaction at Child component level, we define event at child component to be emitted and pass event handler from parent to children. This is called event up.
```jsx
// 1. define event name "onPlay" through props
function Button({ onPlay, children }) {
  return (
  // emit the event through onClick
    <button onClick={onPlay}>
      {children}
    </button>
  );
}

function PlayButton() {
  const [isPlaying, setIsPlaying] = useState(false)

  return (
    <Button onClick={()=> setIsPlaying(!isPlaying)}>
      Play "{isPlaying}"
    </Button>
  );
}
```

Common events:

| categories | Events        | element                       | When is it fire                                                             |
| ---------- | ------------- | ----------------------------- | --------------------------------------------------------------------------- |
| Mouse      | onClick       | button, div, p                | mouse press down and release                                                |
|            | onDoubleClick | button, div, p                | double click                                                                |
| Form       | onSubmit      | form                          | when a submit type button is clicked                                        |
|            | onInput       | input, select, textarea       | when there is change in input field                                         |
|            | onChange      | input,textarea, select        | when contents of the element changes                                        |
|            | onFocus       | input,textarea, select        | when user clicks the input element and the element becomes active for input |
|            | onBlur        | input,textarea, select        | when input element lose activeness                                          |
| Clipboard  | onCopy        | div, p                        | when user copies data from it                                               |
|            | onCut         | div, p                        | when user cuts data from it                                                 |
|            | onPaste       | input, textarea               | when user pastes data into it                                               |
| Pointer    | onPointerDown | button, div, p                | just press down from mouse, touch or pen                                    |
|            | onPointerMove | button, div, p                | mouse, touch or pen move on element                                         |
|            | onPointerUp   | button, div, p                | mouse, touch or pen released on element                                     |
| generic    | onError       | video,img, iframe,script,link | when element fails to load                                                  |
|            | onLoad        | video,img, iframe,script,link | when element load resources                                                 |
| UI         | onScroll      | div                           | when user scroll page                                                       |
|            | onResize      | div                           | when size of browser window changes                                         |
| keyboard   | onKeyDown     | input                         | when user presses a key from keyboard                                       |
|            | onKeyPress    | input                         | when user presses a key from keyboard                                                                            |
|            | onKeyUp       | input                         | when user presses and releases a key                                        |

All supported events: https://legacy.reactjs.org/docs/events.html#animation-events
Event handler cheatsheet: https://react.dev/reference/react-dom/components/common#react-event-object

Events(parameter type in event handler) API you may use:
- preventDefault()
- stopPropagation()
### 3.4.3 useContext
`useContext` can also be a solution to trigger re-render from children to parent or from parent to children. In addition, it allows us to define states that can be shared between parent components and all of its descendant components
1. We first define our context state and setter through `createContext`. `createContext` accepts a variable or a setter function to create a global context to be shared.
2. Then you can access the context through `useContext` by passing the returned result from `createContext`. `useContext` will first find the value from the closest context provider value; if this cannot be found, it will look up the value from the `createContext`.
```jsx group:3.10 file:taskContext.jsx
import { createContext, useContext } from "react"

const TasksContext = createContext(null)
const TasksDispatchContext = createContext(null)

export function useTasks(){
	return useContext(TasksContext)
}

export function useTasksDispatch(){
	return useContext(TasksDispatchContext)
}

export function TasksProvider({ children }){
	// or we can also use useReduce to create state and setter
	const [tasks, setTasks] = useState([])
	
	return (
		<TasksContext value={tasks}>
			<TasksDispatchContext value={setTasks}>
				{ children }
			</TasksDispatchContext>
		</TasksContext>
	)
}
``` 
```jsx group:3.10 file:App.jsx
import { TasksProvider } from './TasksContext';

export default function TaskApp() {
  return (
    <TasksProvider>
      <ChildrenComponent />
    </TasksProvider>
  );
}
```
```jsx group:3.10 file:ChildrenComponent.jsx
import { useTasks, useTasksDispatch } from './TasksContext';

export default function ChildrenComponent(){
	const tasks = useTasks()
	const dispatch = useTasksDispatch()
}
```

### 3.4.4 slot
- pass value to customized properties
```jsx group:3.8 file:ChildComponent.jsx
function ChildComponent(props) {
	return (<>
		<h2> {props.msg} </h2>
		{props.children}
	</>)
}
```

### 3.4.5 LifeCycle
Loading a page(initial render):
render(from root component) -> mount(insert the components into the DOM through `appendChild`) -> useLayoutEffect(perform only synchronous operations in its hook) -> browser paint the screen ->useEffect(can perform async operations)

re-render:
setstate from `useState` buffer update -> render(from components that call setState to leaf components) -> useLayoutEffect -> browser paint -> useEffect
# 4. React Optimization
CheckList:
- if a function is passed from parent to child, try to use `useCallback` to optimize
## 4.1 Memo() & React compiler
`React.Memo()` is used for optimizing _child_ components when their _parent_ re-renders but passes the _same props_ down, stopping unnecessary rendering in the component tree.


# 5. React Router

# 6. Redux

# 7. Security
## 7.1 CVE-2025-55182
https://www.wiz.io/blog/nextjs-cve-2025-55182-react2shell-deep-dive
exploit: https://www.youtube.com/watch?v=jlFwcB0Csbs



