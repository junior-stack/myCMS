---
share: true
---

https://github.com/jsjtzyy/LeetCode/blob/master/Java%20cheat%20sheet%20for%20interview
# 1. Basic
## 1.1 Declare variable

```Python group:1.1
x = 1
y = 2.0
z = "abc"
```
```Java group:1.1
class Main{
	public static void main(String[] args){
		int x = 7;
		float y = 1.0;
		char z = 'a';
		
		String msg = "hello world";
		
		char[] c_arr = {'a', 'b'};
	}
}
```
```C group:1.1
int main(void){
	int x = 1;
	double y = 2.0;
	char z = 'a';
}
```
```Cpp group:1.1
int main(void){
	int x = 1;
	double y = 2.0;
	char z = 'a';
}
```
```Javascript group:1.1
// common js
var x = 1
var y = 1.0
var s = "abc"

// ES6
let x = 1
let y = 1.0
let s = "abc"
const b = 1  // cannot be assigned again and must be initialized
x = 1
```

## 1.2 print
```Python group:1.2
print("hello world")

a, b = 1, 2
print(f"a = {a}, b = {b}")

class A:
	a = 1
	def __str__(self):   # we customize class string in __str__ method
		return f"\{a = {self.a}\}"

print(A()) 	
```
```Java group:1.2
import java.util.Arrays;
class Main{
	public static void main(String[] args){
		System.out.println("Hello world");
		
		int a = 1;
		float b = 2.0;
		char[] c_arr = {'a', 'b'};
		System.out.printf("a = %d, b = %f, %s", a, \
		b, Arrays.toString(c_arr));
		
		// print class
		class A {  
		    @Override  
		    public String toString(){  
		        return "a";  
		    }  
		}  	  
		System.out.println(new A());
	}
}
```
```C group:1.2
# include <stdio.h>
int main(void){
	int a = 1;
	double b = 2.0;
	char *msg = "Hello world";
	printf("a=%d, b=%f, %s\n", a, b, msg);
}
```
```Cpp group:1.2
# include <iostream>
#include <stdio.h>
int main(void){
std::cout <<< "Hello world";
}
```
```javascript group:1.2
a = 1;
obj = {a: 1}
console.log(`a: ${a}`);
console.log(`obj: ${JSON.stringify(obj)}`)
```

## 1.3 Loop
```Python group:1.3
lst = [1, 3, 4, 4]

for item in lst:
	print(item)
	
flag = True:
while flag:
	# code below
	print(lst)
```
```Java group:1.3
char[] c_arr = {'a', 'b'};
for(int i = 0; i < c_arr.length; i++){
	System.out.print(c_arr[i]);
}

for(char item:c_arr){
	System.out.println(item)
}

boolean flag = True;
while(flag){
	System.out.print(c_arr[i]);
}
```
```Javascript group:1.3
// for loop 1:
for (let i = 0; i < 3; i++) {  
	console.log("Iteration number: " + i);  
}

// for...in iterates over enumerable properties of an object
const person = { name: "Alice", age: 30 };  
for (const key in person) {  
	console.log(key + ": " + person[key]);  
}

// for...of iterates values of iterable objects
const colors = ["red", "green", "blue"];  
for (const color of colors) {  
	console.log(color);  
}

// while loop
let count = 0;  
while (count < 3) {  
	console.log("Count is: " + count);  
	count++;  
}

// do...while
let x = 0;  
do {  
	console.log("Value of x: " + x);  
	x++;  
} while (x < 0);

```

## 1.4 Define function
```Javascript group:1.4
// normal declare
function helloworld(name){
	console.log(`Hello: ${name}`);
}

// arrow function
const helloworld = (name) => {
	console.log(`Hello: ${name}`);
}
```



## 1.5 define class
```Javascript group:1.5
class A {
	constructor(a1, a2){
		this.a1 = a1;
		this.a2 = a2;
	}
}

class AA extends A{
	constructor(a1, a2, a3){
		super(a1, a2);
		this.a3 = a3;
	}
}
```

## 1.6 if statement

## 1.7 Operator

# 2. Collections

## 2.1 List
```Python group:2.1
arr = [1, 2, 3]
arr[2]         # return 3
arr.append(4)  # arr becomes [1, 2, 3, 4]
arr.pop()      # arr becomes [1, 2, 3]

arr.insert(2, 5) # arr becomes [1, 2, 5, 3, 4] 
8 in arr         # return False
arr.index(5)     # return 2
len(arr)         # returns the arr's length: 5
```
```Java group:2.1
import java.util.ArrayList;  
import java.util.Arrays;  
import java.util.List;


List<Integer> arr = new ArrayList<>();
List<Integer> arr2 = new ArrayList<>(Arrays.asList(1, 2));

arr2.add(3);   // arr: [1, 2, 3]
arr2.add(2, 4)  // arr: [1, 2, 4, 5]

arr2.remove(1) // arr: [1, 4, 5]
arr2.remove(new Integer(1)) // arr: [4, 5]

arr2.contains(new Integer(4));
arr2.indexOf(new Integer(4));

arr2.get(0);      // gives 4
arr2.set(0, 2)    // arr: [2, 5]

```
```Javascript group:2.1
let arr = [1, 2, 3]
arr[2]                 // return 3
arr.push(4)            // arr becomes [1,2,3, 4]
arr.pop(2)             // arr becomes [1, 2, 4]
arr.length             // returns 3

4 in arr               // returns True
// splice(start, deleteCount, item1, item2, ...)
// splice deletes number of elements equal to deleteCount from arr[start]
// inclusively, then add item1, item2, ... before the original arr[start]
// position, then return an array containing deleted items
arr.splice(1, 1)             // arr becomes [1, 4]
arr.splice(1, 0, 3, 4, 5, 6) // arr becomes [1, 3, 4, 5, 6, 4]
arr.splice(1, 1, 5)         // arr becomes [1, 5, 4, 5, 6, 4]
// find method
// Map

// Reduce

// filter

// forEach
```

## 2.2 Set
```Python group:2.2
my_set = {"apple", "banana"} 
my_set2 = {"apple", "grape"}
my_set.add("cherry") # mySet: {"apple", "banana", "cherry"}
my_set.update(["orange", "mango", "apple"]) 
# mySet: {"apple", "banana", "cherry", "orange", "mango"}
union_set = my_set.union({"pear"})
# union_set: {"apple", "banana", "cherry", "orange", "mango", "pear"}
intersect_set = my_set.intersection(my_set2)
# intersect_set: {"apple"}
diff_set = my_set2.difference(my_set)
# diff_set: {"grape"}
```
```Javascript group:2.2
let b = new Set()
let a = new Set([2])    

a.add(1)           // a becomes {1, 2}
3 in a             // return False
a.delete(2)        // a becomes {1}

b.add(3)
b.add(1)
const unionSet = a.union(b)         //unionSet: {1, 3}
const intersect = a.intersection(b) //intersect: {1}
const diff = b.difference(a)        // diff: {3}
```

## 2.3 Map

```Javascript group:2.3
const myMap = new Map()
myMap.has("a")            // return False because key "a" does not exist
myMap.set("a", 1)         // myMap becomes {"a": 1}
myMap.get("a")            // return 1
myMap.delete("a")         // myMap becomes
```

## 2.4 String
```Python group:2.4
# immutale string
s = "abc"
```
```Java group:2.4
// String class: immutable strings
String s = "abcab";

s.charAt(1);          // gives 'b'
s.compareTo("bcd");   // return -1 because "a" < "b" and differ by 1
s.compareTo("cd");    // return -2 because "a" < "c" and differ by 2
s.contains("bc");     // return True
s.substring(0, 2) ;   // return "ab"
s.substring(1);       // return "bca"
s.indexOf("ab");      // 0, return the location of first substring "ab" in s
s.indexOf("ab", 2);   // 3, return the location of "ab" after s[2] inclusive
// Return "ttctt", replace all occurrences of "ab" with "tt"
s.replace("ab", "tt");  
// Return char array: {'a', 'b', 'c', 'a', 'b'}
char[] arr = s.toCharArray();       
// Return "a*b*c", join the list of <String> into one string connected by
// delimiter
String.join("*", new ArrayList<>(Arrays.asList("a", "b", "c")));
// Return True iff a string character is alnum
Character.isLetterOrDigit(str.charAt(0))


// StringBuffer class: mutable & thread-safe
StringBuffer sb = new StringBuffer();
sb = new StringBuffer("abced");
sb.append("ab");       // sb becomes "abcedab"
sb.insert(0, "zx");    // sb becomes "zxabceddab"
sb.deleteCharAt(0);    // sb becomes "xabceddab"
sb.setCharAt(0, 'c')   // sb becomes "cabceddab"
sb.reverse()           // sb becomes its reverse

// StringBuilder class: mutable, fast but thread-unsafe
// has same methods and use as StringBuffer

// CharSequence interface: implemented by String, StringBuffer, StringBuilder; seen in the parameter type of replace and some methods
```
```Javascript group:2.4
s = "abc"

s.slice(0,2)        // returns[0:2] which is "ab"
s.indexOf("bc", 0)  // return 1
s.includes("ab", 0) // return True
s + "bcd"           // return "abcbcd"
```

## 2.5 Multi-set
# 3. Files
```Javascript group:3
// ES syntax
// asynchronous read & write
import { readFile, writeFile } from 'node:fs/promises';  
  
async function asyncFileExample() {  
	try {  
		const data = await readFile('./myFile.txt', { encoding: 'utf8' });  
		console.log('File content:', data); 
		
		const content = 'This is some content to write to the file.'; 
		await writeFile('./myNewFile.txt', content, { encoding: 'utf8' });
		console.log('File written successfully!');
	} catch (error) {  
		console.error('Error:', error);  
	}  
}

// synchronous read & write
import { readFileSync, writeFileSync } from 'node:fs';
try{
	const content = fs.readFileSync('myFile.txt', 'utf-8');  
	console.log(content);
	
	await fs.writeFile(filePath, data);  
	console.log('File written successfully!');
} catch(err) {
	console.error(err)
}
```

# 4. Set up

## 4.1 Project files directory structure

## 4.2 How to debug


## 4.3 Module import

# 5. Concurrency

# 6. Feature
## 6.1 Reference

## 6.2 Reflection

## 6.3 Closure

## 6.4 Sync vs Async

## 6.5 Memory Model