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
		Integer x = 5; // we use Integer as function parameter type
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
let x = 1 // let variable can be reassigned
x = 2
let y = 1.0
let s = "abc"

const b = 1  // cannot be assigned again and must be initialized
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
```Python group:1.4
def helloworld(x):
	print("hello world: ", x)

hello = lambda x: "helloworld: " + x
```
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
arithmetic:
```Python group:1.7.1
 a = 3 + 2
 a = 3 - 2
 a = 3 * 2
 a = 3 / 2
 a = 3 // 2
 a = 3 % 2
```

Comparison:
```Python group:1.7.2
a = {1: "helloworld"}
b = {1: "helloworld"}
a == b
a is b
```
```Javascript group:1.7.2
// == performs type coersion before comparison
0 == false           //return true
1 == "1"             //return true
null == undefined    //return true

// === does not perform type coersion before comparison
0 === false          // return false (different types)
1 === "1"            // return false
null === undefined   // false

// Object.is: determine if two variables refer to the same object
a = {'a': 1}
b = a
Object.is(a, b)      // return true
```

logic:
```Python
x = True
y = False
1 if x else 2
a and y
x or y
```

bitwise:
```Python group:1.7.4
a = 5
print(bin(x))  # print x's binary string
10 & 5         # 1010 AND 0101 = 0000
10 | 5         # 1010 OR 0101 =  1111
3 ^ 5          # 0011 XOR 0101 = 0110
~a             # ~(0101) = 1010 = -6,  ~x = -(x + 1)
a << 2         # (0101 << 2) = 010100, (x << a) = x * 2^a
a >> 2         # (0101 >> 2) = 01
```

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

// ArrayList
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

// Linkedlist: thread-unsafe

// ConcurrentLinkedQueue: thread-safe and lock-free

// ConcurrentLinkedDeque: thread-safe and lock-free

//  CopyOnWriteArrayList

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
```Java group:2.2
// hashset: not thread safe
Set<Integer> a = new HashSet<Integer>();
Set<Integer> b = new HashSet<Integer>(Arrays.asList(1, 2, 3))
Set<Integer> c = new HashSet<Integer>(Arrays.asList(3, 4, 5))

a.add(10);                              // a: {10}
a.contains(10)                          // return true
a.remove(10)                            // a: {}
a.size()                                // 0
// b becomes the intersection of b and c, b: {3}
boolean result = b.retainAll(c)
// b becomes the union of b and c, b: {3, 4, 5}
result = b.addAll(c)
// b becomes b - c, b: {}
result = b.removeAll(c)

// SortedSet: treeset
Set<Integer> treeSet = new TreeSet<>(); //sort in ascending order by default
treeSet.lower(k);  // max element < k, or null if non-exist
treeSet.higher(k); // min element > k, or null if non-exist
treeSet.ceiling(k); // max element <= k, or null if non-exist
treeSet.floor(k);   // min element >= k, or null if non-exist

// CopyOnWriteArraySet

// ConcurrentSkipListSet
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
```Java group:2.3
// 1. HashMap: not thread-safe
Map<Character, Integer> map = new HashMap<Character, Integer>();
map.put('c', 1);       // map: {'c': 1}
map.put('b', 2)        // map: {'b': 2, 'c': 1}
map.get('c')           // return 1
map.getOrDefault('a', -1)  // return -1
map.remove('c')            // map: {'b': 2}
map.containsKey('c')       // false
map.keySet()               // {'b'}
for(Map.Entry<Character, Integer> entry : map.entrySet()){  
 // traverse key-value pair
    entry.getKey();
    entry.getValue();
}
map.forEach((k,v) -> System.out.println("key: "+k+" value:"+v));
map.size()                // return 1

// 2. Hashtable: locks entire table during any operations
Map<Character, Integer> map = new Hashtable<>()

// 3. ConcurrentHashMap: thread-safe without locking the entire table
Map<String, Integer> concurrentMap = new ConcurrentHashMap<>();

// 4. SortedMap: TreeMap based on red-black tree
Map<Character, Integer> treeMap1 = new TreeMap();
// store the key in reverse order
Map<Character, Integer> treeMap2 = new TreeMap(Collections.reverseOrder());
treeMap.lowerKey(k);           // return max key < k
treeMap.higherKey(k);          // return min key > k
treeMap.ceilKey(k);            // return max key <= k
treeMap.floorKey(k);           // return min key >= k
// return portion of treeMap with keys < k
SortedMap<K,V> portionOfTreeMap = treeMap.headMap(k); 
// return portion of treeMap with keys > k
SortedMap<K,V> portionOfTreeMap = treeMap.tailMap(k);

// 5. ConcurrentSkipListMap<

```
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

## 2.6 BlockingQueue

# 3. Files, I/O

## 3.1 Read & Write API
These APIs are commonly used to read from local persistence:
```Java group:3.1 fold
// IO package: blocks in socket I/O and file I/O
// Read:
// 1. read text file character by character
String filePath = "hello.txt"
BufferedReader reader = new BufferedReader(new FileReader(filePath));
reader.readline()     // returns either a string or null
// 2. read binary file bytes by bytes
FileInputStream fis = new FileInputStream("data.bin");
BufferedInputStream bis = new BufferedInputStream(fis); // improve perform
DataInputStream dis = new DataInputStream(bis); // can read types
int intValue = dis.readInt();  
double doubleValue = dis.readDouble();  
String stringValue = dis.readUTF();
// 3. read entire contents of a file
// readAllLines from NIO is a wrapper of BufferReader from IO package
// and do not block, this is not the core of nio package
Path path = Paths.get("myFile.txt");
byte[] bytes = "Some contents".getBytes()
List<String> lines = Files.readAllLines(path);
// write:
// 1. write text file 
BufferedWriter writer = new BufferedWriter(new FileWriter(filePath));
String content = "Hello, Java File I/O!\nThis is a new line.";
writer.write(content);
// 2. write binary file
FileOutputStream fos = new FileOutputStream("data.bin");
DataOutputStream dos = new DataOutputStream(fos);
dos.writeInt(12345);
dos.writeDouble(3.14159);
// 3. write bytes using a method from nio package
// truncate existing contents and append to existing content
Path path = Paths.get("myFile.txt");
byte[] bytes = "Some contents".getBytes()
Files.write(path, bytes, StandardOpenOption.CREATE, \
						 StandardOpenOption.TRUNCATE_EXISTING);
Files.write(filePath, bytes, StandardOpenOption.APPEND);

// NIO: does not block in socket I/O but blocks in file I/O
// FileChannel: operate on byte level and can read/write contents into 
//              buffer, supporting direct memory access and reduce copying
FileChannel readChannel = FileChannel.open("myFile.txt", \
						StandardOpenOption.READ);
FileChannel writeChannel = FileChannel.open("myFile.txt", StandardOpenOption.CREATE, StandardOpenOption.WRITE);
ByteBuffer buffer = ByteBuffer.allocate(1024);
int bytesRead = readChannel.read(buffer);
writeChannel.write(buffer);

// AIO: does not block in socket I/O or file I/O
// using AIO typically means using java.nio.channels.AsynchronousFileChannel
Path filePath = Paths.get("myFile.txt");
AsynchronousFileChannel fileChannel = AsynchronousFileChannel.open(\
 filePath, StandardOpenOption.READ, StandardOpenOption.WRITE);
ByteBuffer buffer = ByteBuffer.allocate(1024);  
Future<Integer> readResult = fileChannel.read(buffer, 0, buffer, new CompletionHandler<Integer, ByteBuffer>() {  
	@Override  
	public void completed(Integer bytesRead, ByteBuffer attachment) {  
	// Handle successful read  
	attachment.flip(); // Prepare for reading from the buffer  
	// ... process data ...  
	}  
  
	@Override  
	public void failed(Throwable exc, ByteBuffer attachment) {  
	// Handle error  
	}  
});

try {
	// get() blocks until read completes
	Integer bytesRead = readResult.get();  
	buffer.flip();  
	// ... process data ...  
} catch (InterruptedException | ExecutionException e) {  
	// Handle error  
}

```
```Javascript group:3.1 fold
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

// readStream, writeStream
// Similar to read/write file line by line instead of their entire contents
// into memory and is memory-eficient
import { createReadStream, createWriteStream}
const readstream = createReadStream('large_file.txt', 'utf8');
readstream.on("data", chunk => {
	// fn is a some kind of function that process each chunk
	// for example, console.log
	fn(chunk)
})
const writeStream = createWriteStream('output.txt');
writeStream.write('This is the first line of text.\n');  
writeStream.write('This is the second line.\n');

readstream.pipe(writeStream)

writeStream.end('This is the final line.');
```

## 3.2 Network Stream
Stream is commonly used to read something from network, while the above section is commonly used to read sth from local persistence
```Java group:3.2
URL url = new URL("http://www.example.com/somefile.txt");
// different from above FileInputStream
InputStream inputStream = url.openStream();
BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
reader.readline();  // return string or null

```
```Javascript group:3.2 fold
// ReadableStream: different from readStream above

//customized ReadableStream
const myReadableStream = new ReadableStream({
	// This function is called when the stream is first created  
	// Enqueue data chunks to be read
	start(controller) {  
		controller.enqueue('Hello, ');  
		controller.enqueue('world!');  
		// Close the stream when all data has been enqueued  
		controller.close();  
	},   
});

// common way of obtaining readableStream
const myReadableStream2 = (await fetch("www.example.com")).body

// how to use readable Stream:
async function readStream(myReadableStream) {
	const reader = myReadableStream.getReader();
	let result;  
	let accumulatedData = '';  
	  
	while (!result || !result.done) {  
		result = await reader.read();  
		if (!result.done) {  
			accumulatedData += result.value;  
		}  
	}
}

// create WritableStream to send content to a destination
const writableStream = new WritableStream({  
	write(chunk, controller) {  
	// we use the error function from the controller
		try {  
			// Simulate an operation that might fail  
			if (Math.random() < 0.1) {  
				throw new Error('Simulated write error!');  
			}  
			console.log('Successfully wrote:',chunk.toString());
		} 
		catch (err) {  
			console.error('Error during write:',err.message); 
			// Signal the error to the stream 
			controller.error(err);   
		}  
	},  
});  
  
async function writeData() { 
	const writer = writableStream.getWriter();   
	for (let i = 0; i < 5; i++) {  
		try {  
			await writer.write(`Data chunk ${i}`);  
		} catch (err) {  
			console.log('Stream encountered an error');  
			break;  
		}  
	}  
	writer.close();  
}

```

## 3.3 Socket

Server:
```Java group:3.3 fold
// NIO socket I/O:
// SelectableChannel(not FileChannel) subclasses in NIO packages are non-
// blocking and can be multiplexed by Selector class(epoll-based server).
// SelectableChannel subclasses: SocketChannel, ServerSocketChannel, 
// DatagramChannel, Pipe.SourceChannel, Pipe.SinkChannel
// Selectors class
// Buffers class
Selector selector = Selector.open();
ServerSocketChannel server = ServerSocketChannel.open();
server.configureBlocking(false);
server.bind(new InetSocketAddress(8080));
server.register(selector, SelectionKey.OP_ACCEPT);

while (true) {
    selector.select(); // uses epoll internally on Linux
    for (SelectionKey key : selector.selectedKeys()) {
        if (key.isAcceptable()) {
            SocketChannel client = server.accept();
            client.configureBlocking(false);
            client.register(selector, SelectionKey.OP_READ);
        } else if (key.isReadable()) {
            SocketChannel client = (SocketChannel) key.channel();
            ByteBuffer buffer = ByteBuffer.allocate(1024);
            client.read(buffer);
        }
    }
    selector.selectedKeys().clear();
}

// AIO socket I/O:
AsynchronousServerSocketChannel server = \
AsynchronousServerSocketChannel.open().bind(new \
InetSocketAddress("localhost", 5000));

System.out.println("Server listening on port 5000...");

// Start accepting clients asynchronously
server.accept(null, new CompletionHandler<AsynchronousSocketChannel, Void>() {
	@Override
	public void completed(AsynchronousSocketChannel client, Void att) {
		// Accept next connection (important!)
		server.accept(null, this);

		System.out.println("New connection: " + client);

		ByteBuffer buffer = ByteBuffer.allocate(1024);
		client.read(buffer, buffer, new CompletionHandler<Integer, ByteBuffer>() {
			@Override
			public void completed(Integer bytesRead, ByteBuffer buf) {
				buf.flip();
				String msg = StandardCharsets.UTF_8.decode(buf).toString();
				System.out.println("Received: " + msg);

				// Echo message back
				ByteBuffer response = ByteBuffer.wrap(("Echo: " + msg).getBytes(StandardCharsets.UTF_8));
				client.write(response, null, new CompletionHandler<Integer, Void>() {
					@Override
					public void completed(Integer result, Void att) {
						try { client.close(); } catch (Exception ignore) {}
					}

					@Override
					public void failed(Throwable exc, Void att) {
						exc.printStackTrace();
					}
				});
			}

			@Override
			public void failed(Throwable exc, ByteBuffer buf) {
				exc.printStackTrace();
			}
		});
	}

	@Override
	public void failed(Throwable exc, Void att) {
		exc.printStackTrace();
	}
});

// Keep server alive
Thread.currentThread().join();

```
# 4. Set up

## 4.1 Package Manager

~~~tabs
---tab Python
Native:
- file folder directories:
> src
> > main.py
> 
> requirements.txt
~~~

## 4.2 How to debug


## 4.3 Module import


# 5. Concurrency


# 6. Feature
## 6.1 Reference

## 6.2 Reflection


```Java group:6.2
// core classes related to reflection:
// Class, Field, Method, Constructor
// We reveal following examples:
// 1. Getting a class object 2. Inspecting class members
// 3. invoke methods and access fields dynamically

// 1. get class:
// get class given the class name
Class<?> myClass1 = Class.forName("Java.lang.String");
// get class from an instance
String myString = "Hello world";
Class<?> myClass2 = myString.getClass();
// get class from the object class
Class<?> myClass3 = Integer.class;
System.out.println("class Name " + myClass.getName());

// 2. get Methods and fields
import java.lang.reflect.Method;
import java.lang.reflect.Field;
Method[] methods = myClass2.getDeclaredMethods();
Field[] fields = myClass2.getDeclaredFields();
for (Method mtd: methods) {
	System.out.println("Method: " + method.getName());
	System.out.println("Field: " + field.getName());
}

// 3
// invoke method
methods.get(0).invoke(myString, arg1)
// get and set a field
Field fieldA = fields.get(0);
fieldA.setAccessible(true);
String name = (String) fieldA.get(obj);
System.out.println("Name: " + name);  
nameField.set(person, "Jane Doe")
```
```Javascript group:6.2
// Object:
// Object.assign(target, source)
// Object.create(proto, [propertiesObject])
// Object.entries(obj)
// Object.keys(obj)
// Object.values(obj)

// Function:
// call(thisArg, arg1, arg2, ...)
// apply(thisArg, [argsArray])
// bind
```

## 6.3 Closure
In programming language like javascript, Java, Python, C, it uses lexical scope(static scope) meaning that the scope of a variable is determined by where it's defined in the code, not where it's called. On the other hand, dynamic scope means the scope of a variable is determined by where it's called.

**How does lexical scope work:**
Lexical scope is implemented by creating a scope chain that links a function to its parent scopes based on the physical structure of the code, allowing a variable lookup to begin in the innermost scope and repeat moving outward until a match is found. When a function is defined, a closure is created that holds a reference to its parent scope, establishing this chain.

Use Cases: 
- allow functions to maintain state between calls
- create private variables that are only accessible by inner functions

```Javascript group:6.3
function createCounter() {  
	let count = 0; // 'count' is in the outer scope  
	// 'increment' is the inner function, forming a closure
	function increment() {   
		count++;  
		console.log(count);  
	}  
	return increment; // Return the inner function  
}  
  
const counter1 = createCounter(); 
counter1(); // print 1   
counter1(); // print 2
```

## 6.4 Sync vs Async

Promise API:
Promise in javascript is used to wrap the calling of function that takes a lot of time to execute and return a result; the code inside promise is executed synchrounously, but the code in then or catch method is executed after all jobs in event queue are executed; Thus, inside promise we usually place a task at the end of the event queue and the then method will get the result of that task and process the result 
```Javascript group:6.4(1)
// create customized promise
let x = getRandomInt(0, 1)
let myPromise = new Promise((resolve, reject) => {
	// the function inside is executed synchronously
	if(x == 0)
		// resolve just passes "hello world" to parameter of 
		// value in then method
		// You can also pass another promise object into resolve
		resolve("hello world") 
	else
		reject("destroy world")
}).then(value => {
	// the function inside then is executed asynchrounously
	console.log(value)
}).catch(err => {
	// the function inside catch is executed asynchrounously
	console.error(err)
})

const promise1 = fetch('https://api.example.com/data')
const promise2 = readFile('./myFile.txt', { encoding: 'utf8' })
Promise.all([promise1, promise2])
	.then((results) => console.log(results))
	.catch((err) => console.error(err))
```

Common Asynchronous operations that can be wrapped in Promise:
```Javascript group:6.4(2)
// 1. setTimeout, setInterval
new Promise((resolve) => {
	setTimeout(()=>{
		resolve(1)
	}, 0)
}).then((value) => console.log(value))

// return result of asynchronous function that returns promise
new Promise((resolve) =>{
	resolve(readFile('./myFile.txt', { encoding: 'utf8' }))
}).then((value) => console.log(value))
// above is equivalent to:
//readFile('./myFile.txt', { encoding: 'utf8' })
//.then((value) => console.log(value))
```

async/await syntax: 
- async wraps the function inside a promise object and pass the return value of that function into resolve in promise
- await must be used within an asyn function. It is placed before an expression that returns a promise object and is used to capture the resolved value of promise. When js executes the await line, it will executes the code inside the promise object after `await`, then it will jump outside to the parent stack to execute the rest of the code. After the promise object after await is resolved, it will continue to execute the lines after the await line in that async function
```Javascript group:6.4(3)
async function f(){
	const data = await readFile('./myFile.txt', 
	{ encoding: 'utf8' })
	console.log(data)
}

// helloworld is printed first, then the content of myFile.txt
f()
console.log("helloworld);
```

asyn/await mannual implementation: https://blog.csdn.net/weixin_50789156/article/details/124199482
## 6.5 Memory Model


## 6.6 Generic


