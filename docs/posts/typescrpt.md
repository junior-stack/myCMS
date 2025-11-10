---
date:
    created: 2025-10-10
draft: true
---
<!-- more -->
[resource](http://ts.xcatliu.com/basics/union-types.html)

# 一. 基本

## 1. TS与JS的区别与联系:

ts增加了:

+ 类型
+ ES新特性和ES不具备的特性

联系:

+ 所有js代码可被ts解析, ts是js的超集



## 2. 开发环境搭建

1. 使用npm安装Typescript: 一下依赖:
   + `npm i -g typescript ts-loader`(用于将typescript编译成js)
   + `npm i -g ts-node`可以跳过编译阶段直接执行ts代码(可独立与上面的依赖, 即不装上面以来只装ts-node)
2. (*可能)若在powershell里使用`tsc -v`出现在`在此系统上禁用脚本`, 先`get-ExecutionPolicy`查看是否为restricted, 再以管理员身份`set-ExecutionPolicy RemoteSigned`并敲y或a,解决该问题

## 3. 创建一个typescript应用

运行ts文件方式一:

1. 创建一个.ts的文件
2. 进入所在文件夹，使用 `tsc 文件名.ts`编译就会生成.js文件
2. 再用node运行那个js文件即可

运行ts文件方式二:

1. 直接`ts-node 文件名.ts`即可不用编译生成js文件，直接运行ts文件



## 4. 语法

### 1. 声明变量类型:

**变量类型:**

| 类型                   | 值                | 描述                    |
| -------------------- | ---------------- | --------------------- |
| number               | 1, 2             | 数字                    |
| string               |                  |                       |
| boolean              |                  |                       |
| literal              | 1， "a", 1 \| "a" | 代码里给变量赋的任何值，被赋值的变量为常量 |
| any                  | *                | 任意类型                  |
| unknown              | *                | 类型安全的any              |
| void                 | 空值(undefined)    | 没有值(或undefined)       |
| never                | 没有值              | 不能是值                  |
| object               | {a: 'a'}         | 任意的js对象               |
| array                | [1,2]            | 列表                    |
| tuple                | [4,3]            | 固定长度的列表               |
| enum                 |                  |                       |
| （参数名:参数类型...）=>返回值类型 |                  | 表示一个该函数签名的函数类型        |
| class                |                  |                       |

**联合类型**:

变量声明时使用 `|` 分隔两个不同的类型: A和B，表示该变量为A类型或B类型

**如何声明**

```typescript
/*变量名: 变量类型, 示例如下:*/
let a: number
const a: number = 1
function sum(b: number, c: number): number{...}
```

**如何声明一个class**:

```typescript
class 类名 {
    属性名: 类型
    static 属性名: 类型 /*表示静态属性*/
    constructor(参数: 类型){
        this.属性名 = 参数
    }
    
    方法名(){...}
}
```

**获取一个对象的类型,并赋给一个变量**：

```typescript
type myType = {name: string}
const obj: myType = {name: 'sb'}
```

**定义并使用接口**:

```typescript
interface A{
    a: number,
    sayhello(a: number): void
};

interface B {
    b: number,
    sayhi(b: number): void
}
   
let a: A = {a: 1, sayhello: ()=>{console.log('hello')}} 
```

**如何使用泛型**:

1 **泛型定义**：先在变量名右边用一个尖括号囊括用到的泛型字母以此做到声明，然后可以在变量右边的赋值表达式或类体或函数体里像使用类型一样直接使用,

示例一(赋值表达式):

```typescript
type IsExactlyAny<T, S> = boolean extends (T extends S ? true : false) ? true : false;
```

示例二(函数体):

```typescript
function f<T>(a: T): T {return a}
```

示例三(类体):

```typescript
class Component<P, S>{ a:T}
```

限定泛型必须包含C的属性和方法:

```typescript
interface C{a: number};
type IsExactlyAny<T extends C>
```



2 **引用由泛型定义的变量**:

```typescript
let a = IsExactlyAny<son, father>;
f(10);   				/*不指定泛型引用*/
f<string>('hello')		/*指定泛型引用*/   
```



### 2. TS编译选项

+ 监测到ts文件变化后自动化重新编译: `tsc 文件名.ts -w`
+ 使用配置文件(tsconfig.json)编译:
  1. 创建tsconfig.json(示例如下):

```json
{
    /**/
    "compilerOptions": {
        "module": "commonjs", 
        "target": "es5",
        "sourceMap": true
    },
    /*表示希望哪个目录下的.ts文件不被编译*/
    "exclude": [          
        "node_module"
    ],
    /*表示希望那个目录下的.ts文件被编译*/
    "include": ["./src/**/*"],  /*"**"表示任意目录, *表示任意文件*/
    /*表示希望该文件从底下的哪个文件继承*/
    "extends": "./config/base",
    /*表示指定被编译文件列表*/
    "files": ["core.ts"],
    /*compilerOptions子选项如下*/
    "compilerOptions": {
        "target": "ES6",
        "lib": ["ES6", "DOM"],
        ...
    }
}
```

| 选项                             | 可选值                    | 描述                           |
| -------------------------------- | ------------------------- | ------------------------------ |
| target: string                   | "es3"(默认)，"es5", "es6" | ts代码被编译后的目标版本       |
| lib: array[string]               |                           | 指定代码运行时所包含的库       |
| module: string                   | "es5", "commonjs"         | 编译后代码所使用的模块化系统   |
| outdir: string                   | 示例: "./dist"            | 输出目录(默认tsconfig所在目录) |
| outfile: string(常用webpack代替) | "./dist/app.js"           | 将所有代码合并到同一文件       |
| allowJs: boolean                 |                           | 是否将js和ts一起编译           |
| removeComments: boolean          |                           | 是否移除注释                   |
| noEmitOnError: boolean           |                           | 报错时是否继续编译             |

2. 再到.json所在目录使用`tsc`



### 3. Webpack编译ts文件



### 4. 关键字

| static  | export  | export default    | import    |
| ------- | ------- | ----------------- | --------- |
| declare | extends | super             | abstract  |
| const   | let     | type              | interface |
| public  | private | declare namespace |           |
|         |         | declare module    |           |
|         |         |                   |           |

+ extends:

  + 表示继承

  + 表示约束泛型：当extends前面是一个泛型的时候,表示该泛型必须包含extends后的类型的所有属性:

    ```typescript
    function getcnames<T extends{cname: string}>(entities: T[]): string[]{}
    ```

    

### 5. 语法糖

+ 变量后?的使用:

```typescript
box?.addeventlistener("js")  /*表示若box不为null执行addeventlistener,否则，不执行*/
```

+ 变量后!的使用(非空断言操作符: 从变量的值域去除null和undefined)





# 二. 类型大全

+ number
+ string
+ Function
+ any
+ class
+ List

高级类型:

+ class类
+ 类型兼容性
+ 交叉类型
+ 泛型和keyof
+ 索引签名类型和索引查询类型
+ 映射类型



# 三. 类型操作: 交叉与联合

+ 联合: 用于表示一个类型是多个类型的其中某一个, 多个类型间用`|`连接:

  ```typescript
  interface Person {name:string, id: number};
  interface Contact {phone: string, id: number}
  type A = Person | Contact
  ```

+ 交叉: 用于组合多个类型为一个类型, 多个类型间用`&`连接(当`&`前后两个类型出现同名属性但属性类型冲突时, `&`产生的新类型的那个同名属性会是`&`前后两个类型联合类型):

  ```typescript
  interface Person {name:string};
  interface Contact {phone: string}
  type B = Person & Contact
  let obj: B = {
      name: "hi",
      phone: "123456"
  }
  ```

  

# 三. 定义Class和interface和type

interface示例:

```typescript
interface A {
    name: string
}

const a: A = {name: "a"};
```

interface和type大多数情况下一样, 可混用:

```typescript
type Foo = {
    bar: string
}

interface Foo = {
    bar: string
}
```

interface与type关键字的差别:

+ interface可使用extends表示继承,出现子类与父类有同名属性但属性类型冲突时会报错
+ type声明的类型可以用`&`, `|`类型符号, 交叉两个类型时, 当`&`前后两个类型出现同名属性但属性类型冲突时, `&`产生的新类型的那个同名属性会是`&`前后两个类型联合类型
+ interface只能为对象指定类型, 而type可以为任意类型指定别名



# 四. 各种声明类型

方式一(示例):

```typescript
class A {
    name: string
}
const a: A = {name: "a"}
```

方式二(推荐):

```typescript
// 声明一个对象
const a: {name: string} = {name: "a"}

// 声明一个函数:
const b: ()=>string = () => {return "hello"}

// 声明一个混合类型数组:
const c: (number | string)[] = [1, "string", 2]
const d: {name: string}[] = [{name: "d"}]
type E = {name: string};
const e: E[] = [{name: "e"}]

//声明元组: 元组里的每个位置只能是某个特定类型
const f:[string, string, number] = ["hello1", "hello2", 2]
```





# 五. 关键字大全

+ type, 使用示例:

  ```typescript
  type E = {name: string}
  const e:E[] = [{name: "a"}]
  ```

  

# 六. 泛型初步声明

声明一个泛型:

1. 在interface名或class名或函数名旁使用尖括号,尖括号里使用任意的variableName作为泛型名即可声明泛型
2. 在使用函数或创建实例时通过尖括号给泛型传入真实类型,

上述步骤的demo:

**给函数声明泛型一:**

```typescript
// step 1:
function join<T>(first: T, second: T){
    return `${first} ${second}`;
}
// step 2
join<string>("a", "b")
```

**给函数声明泛型二:**

```typescript
const getParam = <T, U>(param1: T: param2: U): [T, U][]
```

**给接口声明泛型:**(注意: 需要显式为泛型指定类型)

```typescript
interface IdFunc<T>{
    id: (value: T) => T,
    ids: () => T[]
}

// 显式为泛型指定number类型
let obj: IdFunc<number> = {
    id: (value: number) => value
    ids: () => []
}
```

**给数组声明泛型：**(注意: 数组其实就是泛型接口，及等同于为接口声明泛型)

**给class声明泛型:** (注意: 形似给接口声明泛型, 不同的是显式为泛型指定类型在这里不是必须的)

```typescript
class A<T>{
    id: T
    constructor(value: T){
        this.id = value;
    }
}

const a = new A<number>(100); //这里<number>可以省略，因为有constructor带入T类型
```



# 七. 泛型约束

当我们在上个section步骤一中声明一个泛型时, 我们在尖括号里除了单纯的传入一个泛型变量,还可以通过一个关键字对泛型变量进行操作,这些统称为泛型约束:

+ `T extends type`(用于表明该泛型必须拥有extends后class或interface或泛型的所有属性和方法):

  ```typescript
  interface A {
      name: string
  }
  
  class AClass<T extends A>{
      constructor(private params: T[]){}
  }
  ```

+ `[k: string]`索引签名类型(用于表示只要是string的属性名称都可以出现在该对象里):

  ```typescript
  interface A {
      [k: number] : string
      //表示A类型的key是一个number类型，值为string类型，且k可以被动态生成
      [n: string]: string
      [o: Symbol]: number
      // js对象的键名属性只能是字符串或数字或Symbol对象的其中一种
  }
  ```

+ `readonly`只读属性:

  ```typescript
  interface A {
      readonly name: string
  }
  ```

+ `K extends keyof T`: 获取所有T的属性名字符串，并将它们结构出来作为联合类型返回

  ```typescript
  interface IPerson {
      name: string,
      age: number,
      sex: 0 | 1
  }
  
  type P1 = keyof IPerson;
  
  interface ITest {
      key: P1 // key的值只能是"name", "age", "sex"三者中的其中一个字符串
  }
  
  let test: ITest = {
      key: "name"  // 可以还可以被赋值为"age"或"sex"
  }
  
  const getProps = <T, K extends keyof T>(object: T, propName: K) => {
      return object[propName] 
      // K类型只能是T的键名称字符串, 即propName的值只能是object的键名称的字符串,
      //因而当T为IPerson类型时, K extends keyof T被转换为了"name" | "age" | "sex",
      // 所以,函数里的propName: K即为propName: "name" | "age" | "sex"
  }
  
  getProps(test, "name")
  ```
  

+ `[k in PropKeys]`映射类型:

  (其中in后面跟的PropKeys表示一个联合类型, 用于表示键名称从PropKey中筛选):

  ```typescript
  type PropKeys = "a" | "b" | "c";
  type T = {[k in PropKeys]: number}
  ```

+ `[k in keyof T]`映射类型:

  ```typescript
  type Props = {a: number, b: string, c: string};
  type P = {[k in keyof Props]: number}
  ```

+ `T[P]`索引查询(访问)类型: 

  当`T[P]`与type关键字结合时, 则表示获取T类型中键为P的属性值类型,出现的场景可以在`Partial<T>`的实现中看到

  ```typescript
  // Partial的实现:
  type Partial<T> = {
      [P in keyof T]?: T[P]
      //这里T[P]表示的是获取T[P]属性所对应的类型，而不是T[P]的对象属性值
  }
  
  //基本使用:
  type Props = {a: number, b: string, c: boolean}
  type TypeA = Props["a"]
  //注意: 必须要有type关键字, Props["a"]才表示访问a属性的类型，否则会被解释为js中访问a属性的值
  ```

+ `T[A | B]`索引查询多个类型:

  当方括号里是一个联合类型时,表示属性名为A的类型联合属性为B的类型,示例:

  ```typescript
  type Props = {a: number, b: string, c: boolean};
  type typeA = Props["a" | "b" | "c"]
  // 等同于 typeA = number | string | boolean
  type typeA = Props[keyof Props]
  ```

  

https://wenku.baidu.com/view/29b29d1664ec102de2bd960590c69ec3d4bbdb43.html

https://blog.csdn.net/web15117716165/article/details/123080349



# 八. 泛型工具类

> 泛型工具类型是基于泛型实现的类，用于操作泛型的关系,且是ts内置的

## 1. Partial

`Partial<T>`用于创建一个新类型,这个新类型将原有的T类型设置为可选, 示例:

```typescript
interface Props {
    id: string
    children: number[]
}

type partialProps = Partial<Props>
```

## 2. Readonly

`Readonly<T>`用于将原有T类型的所有属性设置为只可读:

```typescript
interface Props {
    id: string
    children: number[]
}

type partialProps = Readonly<Props>
```

## 3. Pick

`Pick<T, K>`表示从T类型中选择一组由K指定的属性来构造新类型,示例:

```typescript
interface Props {
    id: string
    title: string
    children: number[]
}
type PickProps = Pick<Props, "id" | "title">
```

## 4. Record

`Record<K, T>`构造一个对象类型, K为属性键, T为属性值且类型为type, 示例:

```typescript
type RecordObj = Record<'a' | 'b' | 'c', string[]>
// 上面创建了RecordObj类型，该类型由a, b, c三个属性，且这三个属性的类型为string[]
let obj: RecordObj = {
    a: ['1'],
    b: ['2'],
    c: ['3']
}
```

https://blog.csdn.net/weixin_44828005/article/details/119720185

# 八. Namespace

将一些class或variable或函数模块化，可以将它们放在一个namespace里，要创建一个namespace,可以用namespace关键字创建, 示例:

```typescript
namespace alpha{
    export class A{
        constructor(){}
    }
}
alpha.A();
```



对于namespace的操作: namespace还可以嵌套,示例:

```typescript
namespace alpha{
    export namespace alpha1{
       export class A{
        constructor(){}
    	} 
    }
}
alpha.alpha1.A()
```

