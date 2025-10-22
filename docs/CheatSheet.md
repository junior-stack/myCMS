
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

## 1.4 Define function

## 1.5 define class

## 1.6 if statement

## 1.7 Operator

# 2. Collections

## 2.1 List
```Python group:2.1
arr = [1, 2, 3]

arr.append(4)  # arr becomes [1, 2, 3, 4]
arr.pop()      # arr becomes [1, 2, 3]

arr.insert(2, 5) # arr becomes [1, 2, 5, 3, 4] 
8 in arr         # return False
arr.index(5)     # return 2
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

## 2.2 Set
```Python group:2.2
my_set = {"apple", "banana"}  
my_set.add("cherry") # mySet: {"apple", "banana", "cherry"}
my_set.update(["orange", "mango", "apple"]) 
# mySet: {"apple", "banana", "cherry", "orange", "mango"}
```

## 2.3 Map


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

## 2.5 Multi-set
# 3. Files

# 4. Set up

## 4.1 Project files directory structure

## 4.2 How to debug

# 5. Concurrency

# 6. Feature
## 6.1 Reference

## 6.2 Reflection

## 6.3 Closure

## 6.4 Sync vs Async

## 6.5 Memory Model