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

a = (1, 2, 3)
```
```Java group:1.1
class Main{
	public static void main(String[] args){
		int x = 7;
		Integer x2 = 5; // we use Integer as function parameter type
		float y = 1.0;
		char z = 'a';
		
		String msg = "hello world";
		
		char[] c_arr = {'a', 'b'};
		
		final int a = 1;  // final means `a` can only be assigned once
	}
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
var y = 1.0   //x and y are both Number type
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
```Cpp group:1.2
# include <iostream>
#include <stdio.h>
int main(void){
	// 1. iostream
	std::cout <<< "Hello world";
	
	// 2. stdio.h
	int a = 1;
	double b = 2.0;
	char *msg = "Hello world";
	printf("a=%d, b=%f, %s\n", a, b, msg);
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
```Java group:1.4
class Demo {
	public String fn(String args){
		return args
	}
}

// Runnable is a function that does not return anything
Runnable fn = ()-> {
	System.out.println("helloworld");
}

// Callable is a function that must return something
Callable<String> fn = ()->{
	return "helloworld"
}
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
```Java group:1.5 fold
abstract class A1 {
	public void methodA1;
}

public interface A {
	public void methodA;
}

public class A2 extends A1 implements A {
	// this class can be instantiated from anywhere
	public A2(){}
	
	// this class can only be instantiated by classes within same package
	A2(){}
	
	// this constructor can be accessed by class within same package or
	// by subclasses in any packages
	protected A2(){}
	
	// this constructor can only be accessed within this class, like its
	// static method
	private A2(){}
	
	public void methodA{}
	
	public void methodA1{}
}

final class B {}
```
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

misc:
```Javascript group:1.7.5
// 1. ... is used to disassemble object or array
let x1 = {a1: 1, a2: true}
let x2 = {...x1, a3: false}  // x2: {a1: 1, a2: true, a3: false}

// 2. usage of ...
let [a, ...rest] = [1, 2, 3, 4];
console.log(rest)            // [2, 3, 4]
let rest2 = [...rest]        // rest2: [2, 3, 4]
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
List<Integer> arr3 = new LinkedList<>();

// CopyOnWriteArrayList: thread-safe, for frequent reads
// create copies when add, set, remove happen, so inefficient frequent write
// does not block each thread while reading
// Iterator can only read and each thread reads the version of the array  
// before modification happens when looping
List<Integer> arr4 = new CopyOnWriteArrayList<>(Arrays.asList(1, 2))
Iterator itr = list.iterator();
arr4.add(5);
// this loop prints [1, 2] because itr is obtained before modified(add)
while (itr.hasNext())
    System.out.println(itr.next()); 
// this loop prints [1, 2, 5]
Iterator itr = list.iterator();
while (itr.hasNext())
    System.out.println(itr.next());

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

// Treest: sorted set but not thread-safe
Set<Integer> treeSet = new TreeSet<>(); //sort in ascending order by default
treeSet.lower(k);  // max element < k, or null if non-exist
treeSet.higher(k); // min element > k, or null if non-exist
treeSet.ceiling(k); // max element <= k, or null if non-exist
treeSet.floor(k);   // min element >= k, or null if non-exist

// ConcurrentSkipListSet: sorted treeset, thread-safe & lock-free
Set<Integer> treeSet2 = new ConcurrentSkipListSet<>();

// CopyOnWriteArraySet
Set<Integer> s = new CopyOnWriteArraySet<>();
Iterator<Integer> t = s.iterator();
while(t.hasNext()){
	System.out.println(t.next());
}

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

// 4. TreeMap:  sortedmap based on red-black tree
Map<Character, Integer> treeMap1 = new TreeMap();
// store the key in reverse order
Map<Character, Integer> treeMap2 = new TreeMap(Collections.reverseOrder());
treeMap.lowerKey(k);           // return max key < k
treeMap.higherKey(k);          // return min key > k
treeMap.ceilingKey(k);            // return max key <= k
treeMap.floorKey(k);           // return min key >= k
// return portion of treeMap with keys < k
SortedMap<K,V> portionOfTreeMap = treeMap.headMap(k); 
// return portion of treeMap with keys > k
SortedMap<K,V> portionOfTreeMap = treeMap.tailMap(k);

// 5. ConcurrentSkipListMap: sorted tree map that is thread-safe & lock-free
Map<Character, Integer> treeMap3 = new ConcurrentSkipListMap();

```
```Javascript group:2.3
// Map:
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
---tab Javascript
hello
~~~

## 4.2 How to debug


## 4.3 Module import


# 5. Concurrency

## 5.1 Atomic class

## 5.2 Thread & Thread pool
```Java group:5.2
// 1. Thread-api: use this when want to cutomize behaviour of each thread
//                the signal handler, wait object, or each thread needs to
//                wait each other
public class MyThread extends Thread {
	@Override
	public void run(){
		Thread.sleep(2000); // make curr thread sleep 2 seconds
		System.out.println("curr tid: " + Thread.currentThread().getId());
	}
}
// start new thread
MyThread thread = new MyThread();
thread.start();

// main thread wait for thread to be exited
try{
	thread.join();
} catch(InterruptedException e){
	Thread.currentThread().interrupt();
}

// 2. Executor Service(Preferred): handy way to create and destroy thread
// 2.1 Common ExecutorService
// create exactly one thread for each submitted task and kill it once finish
ExecutorService executor = Executors.newSingleThreadExecutor();
// create a pool of 4 threads and each thread can be reused for new tasks
ExecutorService executor = Executors.newFixedThreadPool(4);
// create a pool of infinite threads and each idle thread can be 
// reused(idle: thread terminated after 60s if unused)
ExecutorService executor = Executors.newCachedThreadPool();

Callable<String> task1 = ()-> { return "task1"; }
Callable<String> task2 = () -> { return "task2"; }
List<Callable<String>> tasks = new ArrayList(Arrays.asList(task1, task2));

// submit the task to be executed and return a Future object
Future<Void> result1 = executor.submit(task1);
// blocks the curr thread, execute a list of Callables<T> that returns the
// same type; once all tasks are completed, return list of Future<T>
List<Future<String>> results = pool.invokeAll(taskList);

// 2.2 ScheduledExecutorService
// a pool with fixed threads and threads execute after delay or periodically
ScheduledExecutorService executor = Executors.newScheduledThreadPool(2);

// 2.3 graceful 2-phase shut down:
// tell the executor not to accept new task but the threads may continue to
// execute submitted tasks
executor.shutdown();
try {  
	if (!executorService.awaitTermination(timeout, unit)) {  
	// Handle the case where termination did not occur within the timeout  
		System.err.println("ExecutorService did not terminate within the specified timeout.");  
	// Optionally, force shutdown if termination is critical  
		executorService.shutdownNow();  
	}  
} catch (InterruptedException e) {  
	// Handle interruption  
	Thread.currentThread().interrupt(); // Re-interrupt the current thread  
	executorService.shutdownNow(); // Force shutdown if interrupted  
}
```

## 5.3 Lock
```Java group:5.3
// wrap non-concurrent collections
List<Integer> list = Collections.synchronizedList( new ArrayList<>(Arrays.asList(4,3,52)));
```
## 5.4 Synchronizer class
CountDownLatch: makes a thread wait for a number of threads, either child or parent; can only be used once
```Java group:5.4.1 fold
// 1. wait for a set of threads instead of one thread; 
int threadCount = 5;
CountDownLatch latch = new CountDownLatch(threadCount);
class Worker extends Thread {
	private final CountDownLatch latch;
	Worker(CountDownLatch latch){
		this.latch = latch;
	}
	
	@Override
	public void run(){
		Thread.sleep(2000);
		latch.countDown();
	}
};
for(int i = 0; i < threadCount; i++){
	new Worker(latch).start();
};
// use latch to block the current thread and wait for all threads that 
// possess the latch and block
latch.await();

// 2. child thread wait for parent thread, where join() mtd can't do
int threadCount = 10;
CountDownLatch startGate = new CountDownLatch(1);
for(int i = 0;i < threadCount; i++){
	new Thread(()->{
		try {
			startGate.await();
			// Similate the duration of any task
			Thread.sleep(100);		
		}catch (InterruptedException ignored) {
        }finally {
            endGate.countDown();
        }
	}).start();
}
startGate.countDown();
```
CyclicBarrier: make a set of threads to stop at a certain moment and then start at the same time
```Java group:5.4.2
int threadCount = 4;
ExecutorService pool = Executors.newFixedThreadPool(threadCount);
CyclicBarrier barrier = new CyclicBarrier(threadCount);

for(int i = 0; i < threadCount - 1; i++){
	pool.submit(()=>{
		try {
			// block the thread until threadCount threads call await
			barrier.await();
			fn()
		} catch(InterruptedException | BrokenBarrierException e){
			e.printStackTrace();
		}
	})
}

try{
	barrier.await();
} catch (InterruptedException | BrokenBarrierException e) {
	e.printStackTrace();
}
barrier.reset();
pool.shutdown();

```
Phaser:


Semaphore:

## 5.5 Pipes
These classes can be used as pipes between threads or processes
~~~tabs
---tab Java
ConcurrentLinkedQueue:
- add: insert element at tail, throws exception when fail
- offer: insert element at tail, return False when fail
- peek: retrieve but do not remove the head of the queue; return null when empty
- poll: retrieve and remove the head of the queue

BlockingQueue:
- put: insert element at tail, block the thread until queue is available(add/offer does not block)
- take: Retrieves and removes the head of this queue, waiting if necessary until an element becomes available

ConcurrentLinkedQueue vs BlockingLinkedQueue(2 distinctions):
1. ConcurrentLinkedQueue spins and retries modification when multiple concurrent modifications happen. It does not switch thread, thus, does not block. On the other hand, BlockingLinkedQueue waits to grab the ReentrantLock inside the blockingqueue and switches thread when concurrent modifications happen. Thus, this blocks the thread when concurrent modifications happen
2. BlockingLinkedQueue has 2 extra methods: put and take. These 2 methods additionally block thread when queue is full or empty

~~~
APIs:
```Java group:2.6
// ConcurrentLinkedQueue: thread-safe and lock-free, non blocking
Queue<Integer> q = new ConcurrentLinkedQueue<>();
q.add(10);     // q: [10]
q.offer(20);   // q: [10, 20]
q.peek();      // return 10
q.poll();      // return 10, q:[20]

// ConcurrentLinkedDeque: 
Queue<Integer> q2 = new ConcurrentLinkedDeque<>();
q2.addFirst(10);   // q2: [10]
q2.addLast(20);    // q2: [10, 20]
q2.offerFirst(30); // q2: [30, 10, 20]
q2.offerLast(40);  // q2: [30, 10, 20, 40]
q2.peekFirst();    // 30, q2: [30, 10, 20, 40]
q2.peekLast();     // 40, q2: [30, 10, 20, 40]
q2.pollFirst();    // 30, q2: [10, 20,40]
q2.pollLast();     // 40, q2: [10, 20]

// LinkedBlockingQueue: thread-safe but uses lock, may block(park)
BlockingQueue<Integer> bq = new LinkedBlockingQueue<>();
BlockingQueue<Integer> bq = new LinkedBlockingQueue<>(4); // with capacity:4
bq.put(5);     // bq: [5]
bq.take();     // return 5, bq: []

// LinkedBlockingDeque:
BlockingDeque<Integer> bq2 = new LinkedBlockingDeque<>();
bq2.putFirst(5);   // bq2: [5]
bq2.putLast(6);    // bq2: [5, 6]
bq2.takeFirst();   // return 5, bq2: [6]
bq2.takeLast();    // return 6, bq2: []
```

useCases:
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
// 1. Object: internal implementation of Object is hashtable 
//         whose key type can only be string or Symbol type
let obj = {k1: 1, k2: {x: 1}}
// obj: {k1: 1, k2: {x: 1}, k3: "ab"}
Object.defineProperty(obj, "k3", {
	value: "ab",
	writable: true,       // this property can be changed through `=`
	configurable: true,
	enumerable: false
})
// return all keys of an object regardless of enumerable
// ["k1", "k2", "k3"]
Object.getOwnPropertyNames(obj)
// return all enumerable keys of an object, ["k1", "k2"]
Object.keys(obj)
// return the descripor values of a key, 
// {value: 1, writable: true, configurable: true, enumerable: true}
Object.getOwnPropertyDescriptor(obj, "k1")
// Object.assign copies all enumerable properties of a source object 
// to target
obj2 = {}
Object.assign(obj2, obj) // obj2: {k1: 1, k2: {x: 1}, k3: "ab"}
// seal, freeze, extend
Object.preventExtensions(obj) // obj can no longer add new properties
Object.isExtensible(obj)      // return False
Object.seal(obj)              // obj cannot add or delete properties
Object.isSealed(obj)          // return true
Object.freeze(obj)            // obj cannot add, delete or modify properties
Object.isFrozen(obj)          // return True

// 2. Function:
function greet(greeting, punc){
	return greeting + this.name + punc;
}
// call: replace `this` with a specified object and invoke the method
// apply: replace `this` with a specified object and invoke the method with 
//        an array of args (Note: cannot work on arrow function)    
greet.call({name: "Tom"}, "hello ", "!")  
greet.apply({name: "Tom"}, ["hello ", "!"]) // return "hello Tom!"
// bind: return a new func whose this is permanently set to specified
const greet2 = greet.bind({name: "Tom"})
greet2("hello ", "!")   // return "hello Tom!"
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
```Java group:6.4.1
// 1. create CompletableFuture object
// 1.1 runAsync takes a function that does not return value
CompleteableFuture<Void> future1 = CompleteableFuture.runAsync(()->{
	// the function inside Future object is run in a separate thread
	System.out.println("hello world");
})
// 1.2 supplyAsync takes a function that can return value
final int x = 1;
final int y = 2;
CompleteableFuture<Integer> future2 = CompleteableFuture.supplyAsync(()->{
	// the variables from the parent scope must be final
	return x + y;
})

// 1.3 result from ExecutorService
ExecutorService executor = Executors.newFixedThreadPool(1);
Callable<String> = () -> {
	return Files.readAllLines(Paths.get("myFile.txt")).get(0);
}
Future<String> future = executor.submit(task);

// 2. then & exceptionally callback
// 2.1 exceptionally & thenRun:
// thenRun cannot get result from last Future object and return 
// CompleteableFuture<Void>
future2.exceptionally(ex -> return ex.getMessage())\\
	.thenRun(());

// 2.2 thenAccept: get result from last Future object and return 
// CompleteableFuture<Void>
future2.thenAccept(s -> System.out.println("result: " + s))

// 2.3 thenApply: get result from last Future object and return sth in 
// its returned Future object 
Future<Integer> future3 = future2.thenApply(s -> return (1 + s));

// 2.4 whenComplete: takes a function that returns void as input and return Future object that has wrapped value from last Future object
Future<Integer> future3 = future2.whenComplete((result, ex) -> {
	if(ex != null){
		System.err.println("Error: " + ex.getMessage());
	} else{
		System.out.println(result)
	}
})

```
```Javascript group:6.4.1
// 1. create customized promise
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

// 2. Promise.all
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
```Java group:6.4.3
// get() on Future object:
// get() acts as await in javascript
ExecutorService executor = Executors.newFixedThreadPool(1);
Callable<String> = () -> {
	return Files.readAllLines(Paths.get("myFile.txt")).get(0);
}
Future<String> future = executor.submit(task);
// blocks the thread until future is resolved
String result = future.get();
```
```Javascript group:6.4.3
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

~~~tabs
---tab Javascript
https://blog.csdn.net/sjhcake/article/details/123856054
~~~


## 6.6 Generic
```Java group:6.6
<? super E>
Collection<? extends E> c
```

## 6.7 Iterator & Seq Generator

```Python group:6.7
# yield, generator function
```
```Java group:6.7
// Iterator

// Stream Interface and IOStream
```
```Javascript group:6.7
// Generator function & yield
```


## 6.8 Signal handler
