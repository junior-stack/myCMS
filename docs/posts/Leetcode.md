---
date:
    created: 2025-10-10
tags:
  - Programming
---
This is my leetcode notes of algorithms and questions I have practiced
<!-- more -->
# 0. Basis
## 0.1 Built-in module
Python:
- Bisect
	- `bisect_left(a, x, lo=0, hi=len(a)):`This function returns an insertion point in `a`that all elements to its left are less than `x`, and all elements to its right are greater than or equal to `x`
	- bisect_right(a, x, lo=0, hi=len(a)):` This function returns an insertion point in `a` that all elements to the left are less than or equal to x, all elements to right are greater than x
- collections
	- deque
	- defaultdict
- heapq
- copy:
	- deepcopy: create deepcopy for objects, including nested list, set and so on
## 0.2 Runtime Analysis
Typical leetcode testcase compute machine can execute operations per second. Normally an optimal solution, with the largest input possible, would take less than seconds to terminate execution. Thus implies the following:

- n = $10^9$
	- O(log n)（Don't think of O(n)) $\Rightarrow$ binary search(if input is sorted), disjointSet, segment tree, heap, AVL tree
- n = $10^4$
	- O(n) $\Rightarrow$ Double pointers, prefix sum, greedy choice, DP with O(n)
	- O(n * logn) $\Rightarrow$ sort then binary search
- n = $10^3$
	- O($n^2$) $\Rightarrow$ 2D array, 2D-DP
- n = $10^2$
	- O($n^3$) $\Rightarrow$ nested tripple loop
- n = 10
	- O($2^n$), O(n!) $\Rightarrow$ DFS, brute force, permutation, backtracing(recursion)
	
# 1. 二分查找
Note:
- 取`arr[i..j]`左中点: `(i + j) // 2`
- 取`arr[i..j]`右中点: `(i + j + 1) // 2`
Template(General template for finding element in sorted array):


```python
def binary_search(lst, target):
	left = 0
	right = len(lst) - 1
	
	while left <= right:
		mid = (left + right) // 2
		
		if lst[mid] == target:
			return mid
		elif lst[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
		
	return -1	   
```

Variant template:
- Find the first or last target in a sorted array that contains duplicate elements
- Find the insert position of target (Note: insert_position may > len(nums - 1)) 
- Find the position of the element in nums that is larger than or equal to target

```python group:1(1)
# lower is true, then find the first target index
# lower is false, then find the last target index
def binarySearch(nums, target, lower):
	left = 0
	right = len(nums) - 1
	ans = len(nums)
	# 5, 5, 6; target = 5
	while left <= right:
		mid = (left + right) // 2
		
		if nums[mid] > target or (lower and nums[mid] >= target):
			right = mid - 1
			# if below line is moved to else block,
			# ans should be initialized to -1
			# return line should be return ans + 1 if lower else ans
			ans = mid 
		else:
			left = mid + 1
	return ans if lower else ans - 1
```
```Java group:1(1)
class Solution {
	//  find first
	// find last lst[mid] <= target
	public int binarySearch(lst: int[], int target, boolean findFirst){
		int left = 0;
		int right = lst.length - 1;
		int ans = lst.length;
		while(left <= right){
			int mid = (left + right) >>> 1；
			
			if(lst[mid] > target || findFirst && lst[mid] >= target){
				right = mid - 1;
				ans = mid;
			}
			else{
				left = mid + 1;
			}
		}
		return ans if findFirst else ans - 1;
	}
	

}
```
- 二分比较条件(思路来源于Search in Rotated Sorted Array， leetcode: #33)
```Python
def binaryCompare(nums):
	l = 0
	r = len(nums) - 1
	mid = (l + r) // 2
	ans = mid
	while l <= r:
		if ...:  # 关于nums[mid]的条件
			l = mid + 1
		elif ...: # 关于nums[mid]的条件
			r = mid - 1
		
		if ...: # 关于nums[mid]的条件
			ans = mid
			break
		
		mid = (l + r) // 2
	return ans	
```

题:
- [Insert Interval](https://leetcode.com/problems/insert-interval/) (leetcode: #57_)
+ Lintcode #483:(ans: https://www.jiuzhang.com/problem/copy-books-ii/, quite similar to server selection under greedy, but not the same problem type)
- Find Peak element(Leetcode: #162)
- Find the range(Leetcode: #34)

```python fold
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInterval]
        
        if len(intervals) == 1:
            if newInterval[0] >= intervals[0][0]:
                if newInterval[0] <= intervals[0][1]:
                    return [[intervals[0][0], max(intervals[0][1], newInterval[1])|intervals[0][0], max(intervals[0][1], newInterval[1])]]
                else:
                    return [intervals[0], newInterval]
            else:
                if newInterval[1] >= intervals[0][0]:
                    return [[newInterval[0], max(newInterval[1], intervals[0][1])|newInterval[0], max(newInterval[1], intervals[0][1])]]
                else:
                    return [newInterval, intervals[0]]
        
        lower_start, upper_start = self.find_position(intervals, newInterval, 0)
        lower_end, upper_end = self.find_position(intervals, newInterval, 1)
        if lower_start == None:
          if upper_end == None:
            return [newInterval]
          if newInterval[1] >= intervals[upper_end][0]:
                return [[newInterval[0], max(newInterval[1], intervals[upper_end][1])|newInterval[0], max(newInterval[1], intervals[upper_end][1])]] + intervals[1:]
          else:
              return [newInterval] + intervals[upper_end:]
        if newInterval[0] <= intervals[lower_start][1]:
            if upper_end == None:
              return intervals[:lower_start] + [[intervals[lower_start][0], newInterval[1|intervals[lower_start][0], newInterval[1]]]
            if newInterval[1] >= intervals[upper_end][0]:
                return intervals[:lower_start] + [[intervals[lower_start][0], intervals[upper_end][1|intervals[lower_start][0], intervals[upper_end][1]]] + intervals[upper_end + 1:]
            else:
                return intervals[:lower_start] + [[intervals[lower_start][0], newInterval[1|intervals[lower_start][0], newInterval[1]]] + intervals[upper_end:]
        else:
            if upper_end == None:
              return intervals[:lower_start + 1] + [newInterval]
            if newInterval[1] >= intervals[upper_end][0]:
                return intervals[:lower_start + 1] + [[newInterval[0], intervals[upper_end][1|newInterval[0], intervals[upper_end][1]]] + intervals[upper_end + 1:]
            else:
                return intervals[:lower_start + 1] + [newInterval] + intervals[upper_end:]
        
    
    def find_position(self, intervals: List[List[int]], newInterval: List[int], index) -> List[int]:
      if newInterval[index] < intervals[0][index]:
        return [None, 0]
      if newInterval[index] > intervals[-1][index]:
        return [len(intervals) - 1, None]
       
      lower = 0
      upper = len(intervals) - 1
      mid = (upper + lower) // 2
      while upper != lower + 1:
          if intervals[mid][index] < newInterval[index]:
              lower = mid
          else:
              upper = mid
          mid = (lower + upper) // 2
      return [lower, upper]
```
Search in Rotated Sorted Array (Leetcode: #33)
```Python fold
# find the first number in nums that is smaller than target
# edge case:
#   nums=[3, 5], target = 1
def binaryFind_num_0(nums, target):
    if nums[0] < nums[-1]:
        return len(nums)

    l = 0
    r = len(nums) - 1
    mid = (l + r) // 2  
    ans = mid
    while l <= r:
        # mid is on the left half
        if nums[mid] > target:
            l = mid + 1

        # mid is on the right half
        elif nums[mid] < target:
            r = mid - 1

        if mid - 1 >=0 and nums[mid - 1] > nums[mid]:
            ans = mid
            break
        mid = (l + r) // 2
    return ans
  

def binaryFind(nums, target):
    l = 0
    r = len(nums) - 1
    ans = len(nums)
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    return ans  

class Solution(object):
    def search(self, nums, target):
        if nums[-1] < nums[0]:
            num_0_pos = binaryFind_num_0(nums[:len(nums) - 1], nums[-1])
            if target == nums[-1]:
                return len(nums) - 1
            elif target > nums[-1]:
                target_pos = binaryFind(nums[:num_0_pos], target)
                return target_pos if target_pos < len(nums) and \
                    nums[target_pos] == target else -1
            else:
                target_pos = binaryFind(nums[num_0_pos:], target) + num_0_pos
                return target_pos if  target_pos < len(nums) and \
                    nums[target_pos] == target else -1
        else:
            target_pos = binaryFind(nums, target)
            return target_pos if target_pos < len(nums) and \
                nums[target_pos] == target else -1  

if __name__ == "__main__":
    nums = [3,5,1]
    target = 5
    print(Solution().search(nums, target))
```


# 2. 滑动窗口

**题目:**

+ leetcode #3
+ Permutation in String, leetcode #567 / Find All Anagrams in a String, leetcode #438
+ Minimum Window Substring， leetcode #76
+ Max Consecutives one III, leetcode #1004

**思想:**

1. 准备两个指针，一个指向窗口左端叫head, 一个指向窗口右端叫tail
2. 准备一个集合，用于装窗口中的所有元素
3. 不断移动尾指针，一旦尾指针指向的元素出现在集合中；先确定该元素在窗口的位置，然后将head移动到该位置的右侧,并将集合里start移动时指向的元素删除, 同时更新尾指针指向元素的最新窗口位置

```python
from collections import defaultdict
def solution(A: List):
    head = 0
    tail = 0
    windowSet = defaultdict(lambda: -1) 
    # key stores the element inside the window, value stores its index in A
    # if the element is not inside the window, its value is -1 
    
    while tail < len(A):
        
        if windowSet[A[tail]] >= 0:
            location = windowSet[A[tail]]
            while head < location + 1:
                windowSet[head] = 0
                head += 1
        windowSet[A[tail]] = tail
        tail += 1
        
```

# 3. Graph

- DFS:
	- detect cycle
		- Leetcode #207
- BFS:
	- level traversal
- topological sort
- Kruskal & Prim algo(Subgraph tree that connects all vertices and with min weight)
- Single-source shortest path

Runtime:
BFS/DFS    < Dijkstra           <  Bellman
O(V + E)       O((V + E) logV)

## 3.1 DFS
Template: (Runtime: O(V + E))
```Python fold
from collections import defaultdict
def dfs(graph, r):
    stack = []
    # store the node and its child node index, return value in base case
    stack.append((r, 0, acc)) 
    vertexState = defaultdict(lambda :0) 
    
    # represent the return result of next recursive call
    last_recur_ret = None

    while stack:
        v, curr_child_index = stack[-1] 
        
        # code block that is executed before recursive call
        # if last_recur_ret is None:
	        # ....
        # code block that is executed after recursive call
        if last_recur_ret is not None:
	        # perform operations on last recursive call result
	        # to have a branch that is done after the first recurse call:
	        # if stack[-1][2] == acc:
	        #    ....
            stack[-1][2] = fn(stack[-1][2],  last_recur_ret[1])
            last_recur_ret = None

        if vertexState[v] == 0:
            vertexState[v] = 1
            
        if curr_child_index < len(graph[v]):
	        if vertexState[graph[v][curr_child_index]] == 0:
		        stack[-1][1] = curr_child_index + 1
		        stack.append((graph[v][curr_child_index], 0))
		        continue

        vertexState[v] = 2
              
        last_recur_ret = stack.pop()
   return last_recur_ret
```

### 3.1.1 Detect Cycle

**思路:**

1. 每次进入recursive call前，将curr_node作为parent node pass进下一个recursive call, 在下次recursive call中先检查neighbour是否为parent, 如果不是，再检查其status是否是1，如果是，直接return True表示有cycle
题:
-  leetcode: #207

## 3.1.2 Topological sort
Q:
- Course Schedule (Leetcode: #207)
- Course Schedule II(Leetcode: #210)



## 3.2 BFS
Runtime: O(V + E)
```Python group:3.2
from collections import deque, defaultdict
def bfs(G, v):
	q = deque([])
	q.append(v)
	
	visited = defaultdict(lambda : False)
	visited[v] = True
	while q:
		v = q.popleft()
		for neighbour in G[v]:
			if not visited[neighbour]:
				q.append(neighbour)
				visited[neighbour] = True
				
```

### 3.2.1 level order traversal
```Python
from collections import deque, defaultdict
def bfs(G, v):
	q = deque([])
	q.append(v)
	
	visited = defaultdict(lambda : False)
	visited[v] = True
	
	while q:
		n = len(q)
		for _ in range(n):
			v = q.popleft():
			# code block 1:
				# ...
			for neighbour in G[v]:
				if not visited[neighbour]:
					visited[neighbour] = True
					q.append(neighbour)
					
```

- Binary Tree ZigZag Level order traversal(Leetcode: #103)
- Populating Next Right Pointers in Each Node（Leetcode: #116)

### 3.2.2 Shortest path
题:
- 单词接龙, leetcode #127
- Sliding Puzzle, leetcode #773

## 3.3 Single-source shortest path
What is the problem:
> Given a graph and a pair of vertices (u, v), we want to find the path from u to v s.t the sum of weights from u to v is minimized

Restriction for Bellman-Ford:
- The graph cannot contain a cycle where the sum of the edges of the cycle is negative and can be reached from starting vertex s
Practice:
- find shortest path on directed/undirected graph
Bellman-Ford `O(VE)`:
```Python
from collections import defaultdict
def relax(u, v, w, short_path):
	if short_path[u] + w < short_path[v]:
		short_path[v] = short_path[u] + w
		return True
	return False
	
def BellmanFord(G, s):
	# Initialize single source and edges
	shortest_path = defaultdict(lambda :float("inf"))
	shortest_path[s] = 0
	
	# relax each edge of u
	for _ in range(len(G) - 1):
		for u in G:
			for v, w in G[u].items():
				if shortest_path[u] != float("inf"):
					relax(u, v, w, shortest_path)
	
	# detect negative cycle
	for u in G:
		for v, w in G[u].items():
			if shortest_path[u] != float("inf") and \
			shortest_path[u] + w < shortest_path[v]:
				return False
	
	return True			
```

Restriction for Dijkstra:
- The graph cannot have negative weight edges
Practice
- find shortest path on directed/undirected graph
Dijkstra's algorithm(`O((V+E)logV)`):
```Python
from collections import defaultdict
from heapq import heappop
def relax(u, v, w, short_path):
	if short_path[u] + w < short_path[v]:
		short_path[v] = short_path[u] + w
		return True
	return False

def dijkstra(G, s):
	# stores the nodes on the shortest path
	# for each node as key, store it distance from s
	shortest_path = defaultdict(lambda : (float("inf")))
	shortest_path[s]= 0
	Q = [(0, s)]
	while Q:
		curr_distance, u = heappop(Q)
		
		if curr_distance > short_path[u]:
			continue
			
		# relax each edge of u
		for v, w in G[u].items():
			if relax(u, v, w, shortest_path):
				heapq.heappush(Q, (shortest_path[v], v))
	return shortest_path
```

题:
- Cheapest flights within K stops (leetcode #787)
- Network Delay time(leetcode #743)
## 3.4 All-pairs shortest path
Floyd-Warshal($O(V^3)$)
- When to use: when |E| > $|V|^2$  
- restriction: the graph cannot contain negative cycles (where the sum of the edges in a cycle is negative)
```Python
def FloydWarshal(G):
	# G must be a |V|x|V| matrix with each entry as the weight value;
	# Otherwise, we will have to loop through each edge of G to construct D,
	# which is not allowed
	num_vertices = len(graph)  
	dist = [row[:] for row in graph] # Create a copy of the graph  
	  
	# Iterate through all possible intermediate vertices 'k'  
	for k in range(num_vertices):  
		# Iterate through all possible source vertices 'i'  
		for i in range(num_vertices):  
			# Iterate through all possible destination vertices 'j'  
			for j in range(num_vertices):  
			# If vertex 'k' is on the shortest path from 'i' to 'j',  
			# then update the distance  
				if dist[i][k] != float('inf') and \
				dist[k][j] != float('inf'):  
					dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])  
	return dist
```

## 3.5 MST
What is MST
> an acyclic tree whose:
> -  edge set is a subset of G
> - connect all vertices
> - sum of weights of all edges are minimized

Kruskal's algorithm`O(E lg(V))`
```Python
# class DisjointSet:

def createMST(G, w):
	A = set()
	
	ds = DisjointSet()
	for v in G.keys():
		ds.makeSet(v)
	
	# sort the edges of G.E into nondecreasing order by weight w
	E = sort(G)
	
	for (u, v) in E:
		if ds.find(u) != ds.find(v):
			A.add((u, v))
			ds.union(u, v)
	return A
		
```

Prim's algorithm: `O(E + V lg(V))`
```Python fold
def prim(graph, start_vertex):
	# graph example: {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': 5}}
	mst = [] # Stores the edges of the Minimum Spanning Tree  
	visited = set() # Keeps track of visited vertices  
	  
	# Priority queue (min-heap) to store edges, ordered by weight  
	# Format: (weight, from_vertex, to_vertex)  
	edges = []  
	  
	# Start with the initial vertex  
	visited.add(start_vertex)  
	for neighbor, weight in graph[start_vertex].items():  
		heapq.heappush(edges, (weight, start_vertex, neighbor))  
	  
	while edges: 
		# Get the edge with the minimum weight 
		weight, u, v = heapq.heappop(edges)  
		  
		if v not in visited:  
			visited.add(v)  
			mst.append((u, v, weight))  
		  
		# Add all edges connected to the newly visited vertex to the heap 
		for neighbor_of_v, weight_to_neighbor in graph[v].items():  
			if neighbor_of_v not in visited:  
				heapq.heappush(edges, \
				(weight_to_neighbor, v, neighbor_of_v))  
	  
	return mst
```

# 4. Greedy choiice

+ Server selection(snow flake OA)
> 把n本书分给k个人复印，想要使每个人复印的总时间的最大值最小化。很明显是一个求最优解的问题，很自然的想到用贪心的思想。因为每本书都是没有差异的，所以可以依次贪心的为每一本书选择k个人中的最优人选。 令times[]表示每个人复印一本书的时间，sum[]表示每个人复印所花的总时间。若此时在判断把第 i 本书给哪个人复印，此时前 (i - 1) 本书被复印的最短时间是minSum。实现过程如下：若把第 i 本书给第 j 个人复印，这时第 j 个人所花的总时间 sum[j] + times[j] ，若这个总时间不大于minSum，说明对答案没影响，那么选其中任意一种即可，结束循环人选； 若把第 i 本书给第 j 个人复印，这时第 j 个人所花的总时间 sum[j] + times[j] ，若这个总时间大于minSum，说明答案会变大，那么我们继续判断下一个人选，选择令答案增加的最少的一种情况；每次选择结束后都要更新一次答案，minSum = max(Minsum, sum[被选择的人]) 。

```pseudocode
sort time from low to high
sum = []
append (lowest time, index of it in times) to sum
let s be the set that contains people are copying at the same time
add the people who has the loest to sum
let s_prime be the complimentary set
for each i = 1 to n:
	find the lowest time tuple in sum
	put the people from the tuple from s to s_prime
	find people with the lowest time in s_prime
	if that people's time plus the time in tuple is greater than some people p1,
		add p1's time and p1 to sum
	else:
		modify the tuple's time and index to that people
	
	
```
- 递增的三元子序列(Leetcode #334)
	- Longest increasing subsequence(Leetcode #300, general version of #334)
	- [Russian Doll Envelopes, leetcode #354](https://leetcode.cn/problems/russian-doll-envelopes/)
- 任务调度器 Leetcode #621
- jump game II, leetcode #45 / jump game, leetcode #55

**递增的三元子序列(Leetcode #334)**
- 思路: loop一边array, 每loop一个元素`array[i]`, 维护两个变量: small和mid, small为`array[0..i]`最小的element, mid为`array[0..i]`中大于`small`最小的element
```Python
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """        
        small = nums[0]
        mid = float("inf")
        
        for i in range(1, len(nums)):
            if nums[i] < small:
                small = nums[i]
            elif nums[i] > small:
                if nums[i] < mid:
                    mid = nums[i]
                elif nums[i] > mid:
                    return True
        return False
```

# 5. DP

+ lintcode 151
+ lintcode1850
+ task scheduling(snowflake OA)
+ Palindrome/substring
	+ Longest Palindrome substring(Leetcode #5)
+ House Robber, Leetcode #198

## 5.1 Palindrome/substring

思路: 准备一个dp的dictionary, dp以(i, j)为key, 其中(i, j)表示`s[i..j]`, `dp[(i, j)]` 表示`s[i..j]`满足某种条件为True/False

 Longest Palindrome substring(Leetcode #5)
(Note: Leetcode sometimes only accept bottom-to-top DP, and does not accept top-to-bottom recursive DP, leetcode #5 is an example)

bottom-to-top DP soln:
```Python fold
from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, s):       
        dp = defaultdict(lambda :-1)
        acc = s[0]
        for i in range(len(s)):
            dp[(i, i)] = True
        
        for i in range(len(s) - 1):
            
            dp[(i, i + 1)] = s[i] == s[i + 1]
            
            if dp[(i, i + 1)] and len(acc) == 1:
                acc = s[i:i+2]
        
        
        for L in range(2, len(s)):
            for i in range(len(s) - L):
                if s[i] != s[i + L]:
                    dp[(i, i + L)] = False
                else:
                    dp[(i, i + L)] = dp[(i + 1, i + L -1)]
                    
                    if dp[(i, i + L)] == True and L + 1 > len(acc):
                        acc = s[i:i + L + 1]
        return acc
```


Top-to-bottom recursive soln(does not work for large input):
```Python fold
from collections import defaultdict
def dp_recursive_helper(dp, s, i, j):
    if i == j:
        dp[(i, j)] = 1
        return True
    
    if j == i + 1:
        dp[(i, j)] = 1 if s[i] == s[j] else 0
    
    if dp[(i, j)] != -1:
        return dp[(i, j)]
    
    if s[i] != s[j]:
        dp[(i, j)] = 0
    else:
        dp[(i, j)] = dp_recursive_helper(dp, s, i + 1, j - 1)
    
    
    return dp[(i, j)]
    
class Solution(object):
	def longestPalindrome(self, s):	
		dp = defaultdict(lambda :-1)
		
		for i in range(len(s)):
			for j in range(i, len(s) - 1):
				is_palindrome = dp_recursive_helper(dp, s, i, j)

                if is_palindrome:

                    if j - i + 1 > len(acc):

                        acc = s[i:j+1]

        return acc				
```

## 5.2 Other

- Coin Change(Leetcode #522)
总结: dp中, 假设一个range为$c * 10^4$ 到$10^5$, 可以作为dp的一个for loop一个一个循环, 如下example, 因而，永远要检查input size
```Python
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = defaultdict(lambda :-1)
        
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                if dp[x - coin] != -1:
                    if dp[x] == -1:
                        dp[x] = dp[x - coin] + 1
                    else:
                        dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount]
```

# 6. backtracing

https://leetcode.cn/problems/combination-sum/solutions/14697/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/

图中为啥4分支在搜索的时候不在考虑2:

WTS: 对所有层，假设第一个使用的candidate是x, 假设第二个使用的candidate是y, target是z, 那么y分支下所有包含x的路径都被x分支包含(即搜y分支不需要考虑x)

- 假设y分支不存在包含x的路径，那么我们也不需要考虑x, 这种case结束

- 假设y分支存在包含x的路径，也就是说z > y + x, 那么x分支下也存在一条路路径包含y, x分支下的y路径的第一个节点(z - x-y)下包含了所有总和为(z - x -y)的路径也就和y分支下包含x的路径节点重合



# 7. Prefix sum & array

什么叫前缀和数组:

> 给一个数组a = [a1, a2, ... aN], a的前缀和数组是 a = [a1, a1 + a2, a1+a2+a3, ... (a1 + a2 +...aN)]

-  House Robber, Leetcode #198
- Maximum Subarray, leetcode #53 
- Maximum Product Subarray, leetcode #152



# 8. 双指针

## 8.1 前后指针
- three sum(K-sum)

```Python group:10.1 fold
def twoSum(nums, startIndex, endIndex, target):
    phead = startIndex
    ptail = endIndex
    acc = []
    while phead < ptail:
        curr_sum = nums[phead] + nums[ptail]
        if curr_sum > target:
            ptail -= 1
        elif curr_sum < target:
            phead += 1
        else:
            acc.append([nums[phead], nums[ptail]])
            
            while phead < ptail and nums[phead] == nums[phead + 1]:
                phead += 1
            phead += 1
            
            while phead < ptail and nums[ptail] == nums[ptail - 1]:
                ptail -= 1 
            ptail -= 1
    return acc
            

class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        acc = []
        for i in range(len(nums) - 2):
            if i <= 0 or nums[i] != nums[i - 1]:
                curr_pairs = twoSum(nums, i + 1, len(nums) - 1, -nums[i])
                for curr_pair in curr_pairs:
                    acc.append([nums[i], curr_pair[0], curr_pair[1]])
        return acc
```
```Javascript group:10.1
console.log()
```

## 8.2 快慢指针
思路: 有四种思路:
- 第一种，维护两个指针，第二个指针在第一个指针k个位置之后作为快指针，同时移动两指针,快指针到达末尾后，满指针到达末尾第k个位置:
	- [Remove Nth Node From End of List, leetcode #19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- 第二种, 维护两个指针, 第二个指针的step为第一个指针移动step的两倍, 同时移动两指针, 当第二个指针到达末尾时, 第一个指针到达中点:
	- [Middle of the Linked List, leetcode #876](https://leetcode.com/problems/middle-of-the-linked-list/)
	- 判断环起点([[Leetcode#11.3 ring start]]), leetcode #141, leetcode #142
- 第三种, 维护两个指针，快指针照常每个iteration前进一个元素, 满指针在每个iteration根据特定条件前进一个元素
- 第四种, 滑动窗口
- Others:
	- Gas staation, leetcode #134

模板:
- 第二张快慢:
```Python
class Solution:
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
	p1 = head
	p2 = p1

	while p2 and p2.next:
		p1 = p1.next
		p2 = p2.next.next
	return p1
```
- 第三种:
```Python
def fn(arr):
	p_slow = 0
	p_fast = 0
	
	while p_fast < n:
		# arr[p_slow] satisfies certain condition, we move p_slow
		if condition(arr[p_slow]):
			p_slow += 1
		p_fast += 1
```
# 9. Tree

## 9.1  traversal

- Construct Binary Tree from Preorder and Inorder Traversal(Leetcode: #105)

## 9.2 AVL Tree
- Convert sorted array to AVL tree(Leetcode #108):
```Python fold
def helper(nums, i, j):
    if j < i:
        return None

    mid = (i + j) // 2
    root = TreeNode(nums[mid])
    root.left = helper(nums, i, mid - 1)
    root.right = helper(nums, mid + 1, j)
    root.height = 0

    if root.left is not None:
        root.height = root.left.height + 1
    if root.right is not None:
        root.height = max(root.height, root.right.height + 1)
    return root

def sortedArrayToBST(nums):
    helper(nums, 0, len(nums) - 1)
```
- convert binary tree to AVL tree(Leetcode #1382):
```Python
def solution(root):
	# step 1: perform in order traversal to the BST to convert it into sorted array
	# use the above template to convert sorted array into AVL tree
```
- AVL Tree implementation
```Python group:9.2 fold
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
	# keyFunc takes a, b as inputs
	# keyFunc returns 1 if a > b, 0 if a == b, -1 if a < b
	def __init__(self, keyFunc):
		self.keyFunc = keyFunc
		self.root = None
	
	def search(self, value):
		curr = self.root
		while curr and self.keyFunc(value, curr.val) != 0:
			if self.keyFunc(value, curr.val) > 0:
				curr = curr.left
			else:
				curr = curr.right
		return curr
	
	def insert(self, value):
		if self.root is None:
			self.root = TreeNode(val=value)
			return self.root
		
		curr = self.root
		stack = []
		while curr:
			if self.keyFunc(value, curr.val) >= 0:
				stack.append((curr, 1))
				curr = curr.right
			else:
				stack.append((curr, 0))
				curr = curr.left
		
		leaf, side = stack[-1]
		if side == 1:
			leaf.right = TreeNode(val=value)
		else:
			leaf.left = TreeNode(val=value)
		
		lastBalancedNode = balanceTree(stack)
		if lastBalanceNode:
			self.root = lastBalanceNode
		return self.root
	
	def delete(self, value):
		if self.root is None:
			return None
		
		curr = self.root
		stack = []
		while curr:
			if self.keyFunc(value, curr.value) > 0:
				stack.append((curr, 1))
				curr = curr.right
			elif self.keyFunc(value, curr.value) < 0:
				stack.append((curr, 0))
				curr = curr.left
			else:
				if curr.left is None or curr.right is None:
					break
				# when the deleted node has both children
				# replace deleted node with the leftmost leaf in 
				# right subtree
				else:
					successor = curr.right
					while successor.left:
						successor = successor.left
					curr.val, success.val = successor.val, curr.val
					stack.append((curr, 1))
					curr = curr.right
		
		# case: value does not exist in tree
		if curr is None:
			return None
		
		# case: when value is at the root and root only has one child
		if len(stack) == 0:
			self.root = curr.right if curr.left is None else curr.left
			return curr
		
		parent, side = stack[-1]
		if side == 0:
            parent.left = curr.right if curr.left is None else curr.left
        else:
            parent.right = curr.right if curr.left is None else curr.right
		
		lastBalancedNode = balanceTree(stack)
		if lastBalancedNode:
			self.root = lastBalancedNode
		
		return curr
		


def getHeight(x: TreeNode):
	return x.height if x else 0
	
def leftRotate(x: TreeNode):
	R = x.right
	RL = R.left
	
	# Makes x becomes the root of R's left subtree
	x.right = RL
	R.left = x
	
	# adjust height of R and x
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    R.height = 1 + max(getHeight(R.left), getHeight(R.right))
    
    return R
    
def rightRotate(x: TreeNode):
	L = x.left
    LR = L.right

    x.left = LR
    L.right = x 

    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    L.height = 1 + max(getHeight(L.left), getHeight(L.right))

    return L

def balance(x: TreeNode):
    balance = getHeight(x.left) - getHeight(x.right)
    L = x.left
    R = x.right

    if balance > 1:
        leftbalance = getHeight(L.left) - getHeight(L.right)
        if leftbalance >= 0:
            return left_Rotate(x) 
        else:
            x.left = left_Rotate(L)
            return right_Rotate(x)
    elif balance < -1:
        rightbalance = getHeight(R.left) - getHeight(R.right)
        if rightbalance <= 0:
            return left_Rotate(x)
        else:
            x.right = right_Rotate(R)
            return left_Rotate(x)
    else:
        return x

def balanceTree(stack):
    prev = None
    while stack:
        curr, side = stack.pop() 

        if prev is not None:
            if side == 0:
                curr.left = prev
            else:
                curr.right = prev
            prev = None

        curr.height = 1 + max(getHeight(curr.left), getHeight(curr.right))
        
        heightdiff = getHeight(curr.left) - getHeight(curr.right)  
        if heightdiff > 1 or heightdiff < -1:
            prev = balance(curr)
    return prev
```

# 10. Heap

Heap operation templates:
```Python group:10 fold
# swap larger element between parents and one of its children from ith node to the leaf, below is max-heap
# Effect: makes arr[i:n] a heap, also called heapify
def sift_down(arr, n, i):
    curr_parent = i  

    while curr_parent < n:
        next_parent = curr_parent
        left_child = 2 * curr_parent + 1
        right_child = 2 * curr_parent + 2

        if left_child < n and arr[left_child] > arr[next_parent]:
            next_parent = left_child

        if right_child < n and arr[right_child] > arr[next_parent]:
            next_parent = right_child

        if next_parent != curr_parent:
            arr[curr_parent], arr[next_parent] = arr[next_parent], arr[curr_parent]
            curr_parent = next_parent
        else:
            break

def sift_up(arr, i):
	curr_i = i	
	while curr_i > 0:
		parent_i = (curr_i - 1) >> 1
		if arr[curr_i] > arr[parent_i]:
			arr[curr_i], arr[parent_i] = arr[parent_i], arr[curr_i]
		else:
			break

def heappush(arr, item):
	arr.append(item)
	sift_up(arr, len(arr) - 1)

def heappop(arr):
	tailItem = arr.pop()
	if len(heap) == 0:
		return tailItem	
	headItem = arr[0]
	
	arr[0] = tailItem
	sift_down(arr, len(arr), 0)
	return headItem

def heappushpop(arr, item):
	if len(arr) == 0:
		return item
	if arr[0] > item:	
		return heappoppush(arr, item)
	else:
		return item

def heappoppush(arr, item)
	if len(arr) == 0:
		raise Error("err")
	# replace the head of the heap with new item, then heapify
	headItem, arr[0] = arr[0], item
	sift_down(arr, len(arr), 0)
	return headItem
```

- heapSort
	- Non-inplace
```python group:10(1)
from heapq import heappush, heappop
def sort(nums):
	h = []
	for value in nums:
		heappush(h, value)

    return [heappop(h) for i in range(len(h))]
```
```Javascript group:10(1)
```

- Inplace sort:
```python group:10(2)
def sort(nums):
	n = len(nums) 
	# build max heap that extract max key
	for i in range(n // 2 - 1, -1, -1):
		heapify(nums, n, i)
	
	for i in range(n - 1, 0, -1):
		# moves the largest element to the end of the array
		nums[0], nums[i] = nums[i], nums[0]
		# Keeps arr[:n-1] (excluding the last element) a heap
		heapify(nums, i, 0)
```


- K items comparison(Min-heap):
	- Merge K sorted List(Leetcode #23)
-  sort Interval:
	- 252 Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
	+ [253 Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
	+ [435 Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

# 11. LinkedList
Template:
- dummy node
	- 合并LinkedList
```python
curr = ListNode()
while ...:
	curr.next = ...	
	curr = curr.next
```


## 11.1 MergeLinkedList
- 思路:
![[1.gif]]

- [合并两个有序链表, leetcode #21](https://leetcode.cn/problems/merge-two-sorted-lists/)
```Python fold
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        acc = ListNode()
        p = acc
        p1, p2 = list1, list2

        while p1 and p2:
            if p1.val <= p2.val:                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next  

        if p1:
            while p1:
                p.next = p1
                p = p.next
                p1 = p1.next

        if p2:
            while p2:
                p.next = p2
                p = p.next
                p2 = p2.next
        return acc.next
```

- [合并K个升序链表, leetcode #23](https://leetcode.cn/problems/merge-k-sorted-lists/)
	- 思路: 有用到heap

## 11.2 Last K position of mid point of linked list

## 11.3 ring start
![[Pasted image 20250930192654.png]]

# 12. Disjoint Set
Operations:

+ find(`O(α(n))`)
+ union(`O(α(n))`)
+ makeSet(`O(α(n))`)
`α(n)`is the **inverse Ackermann function** (which grows slower than log)

Data structure:

```python fold
class DisjointSet:
    def __init__(self, lst):
        self.parent = {}
        self.rank = {}  # the height of each node
    
    def makeSet(self, x):
    """Add a new element as its own set."""
	    if x not in self.parent:
		    self.parent[x] = x
		    self.rank[x] = 0
	
	def find(self, x):
	"""Find the root of x with path compression"""
		if x not in self.parent:
			self.makeSet(x)
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]
	
	def union(self, x, y):
		"""Union the sets containing x and y"""
	    root_x = self.find(x)
	    root_y = self.find(y)
	    
	    if root_x == root_y:
		    return False
		
		if self.rank[root_x] < self.rank[root_y]:
			self.parent[root_x] = root_y
		elif self.rank[root_y] < self.rank[root_x]:
			self.parent[root_y] = root_x
		else:
			self.parent[root_y] = root_x
			self.rank[root_x] += 1     

```

# 13. Trie(前缀树)

**题目**: Leetcode #208

**应用**: 搜索查询时,搜索引擎通过用户的输入作为前缀从数据库的高频词汇中召回所有以该用户的输入为前缀的词汇

用于存储字符串:

```python group:14
class Trie:
    # 比比较通用的模板 #
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = dict()
        self.isword = False  #表示该Trie node是否为一个字符串的结尾

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        rt= self  #相当于c++的this指针！！！
        for w in word:
            if w not in self.child:     #没有，就新建
                self.child[w] = Trie()
            rt = rt.child[w]          #往下走
        rt.isword = True        #标记位


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        rt= self  #相当于c++的this指针！！！
        for w in word:
            if w not in rt.child:     #有字母不在这条path上，断了
                return False
            rt = rt.child[w]          #沿着path往下走
        return rt.isword == True    #看isword位

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        rt = self  #相当于c++的this指针！！！
        for w in prefix:
            if w not in rt.child:     #path断了
                return False
            rt = rt.child[w]
        return True
```
```Java group:14
```


# 14. MonoStack

https://itnext.io/monotonic-stack-identify-pattern-3da2d491a61e

What is a monoStack:

> A monostack is a stack whose elements are monotonically non-decreasing or non-increasing. The monstack has two operations: pop and push(varied based on the type of monostack) to maintain this property. There are 2 types of mono stack:
>
> - mono-decreasing:
>   - pop: pop out the item at the top of the stack(tail of the array)
>   - push(item):
>     1. while stack not empty and stack.top < item:
>        1. pop(stack.top)
>     2. insert(stack, item)
> - mono-increasing:
>   - pop: pop out the item at the top of the stack
>   - push(item):
>     1. while stack not empty and stack.top > item:
>        1. pop(stack.top)
>     2. insert(stack, item)



Application of mono-stack:

1. Find Next-Great-Element and Prev-Great-Element of each array element

> For mono nondecreasing stack:
>
> we define the following(for each array element `arr[i]`):
>
> - Next-Great-Element(arr[i]): the first value that is greater than `arr[i]` on the right of `arr[i]` 
> - Prev-Great-Element(arr[i]): the last value that is greater than `arr[i]` on the left of `arr[i]`
>
> We usually load the array content into a mono stack as above by consistently pushing the element of the array. During the push(item), for each element `arr[i]` that is popped, Next-Great-Element(arr[i]) is the  newly inserted `item` and Prev-Great-Element(arr[i]) is the element that is before `arr[i]` in stack(i.e: the stack top after we pop `arr[i]`). If we need to use Next-Great-Element(arr[i]) or Prev-Great-Element(arr[i]) of each element `arr[i]` to solve the problem, consider monostack

2. find the smallest combination of array element in the array

   > After loading all elements into the stack, the stack exhibits the following property:
   >
   > - the array element of the stack is in sequential order, where the i^th^ element of the stack must be before the j^th^ element of the stack in original array if i < j
   > - Among all sub-sequences from the array that is in sequential order, the sequence in the stack has the smallest lexicographical order comparing with any sequence of the same length(smallest lexicographical order refers to "A string `a` is **lexicographically smaller** than a string `b` if in the first position where `a` and `b` differ, string `a` has a letter that appears earlier in the alphabet than the corresponding letter in `b`.If the first `min(a.length, b.length)` characters do not differ, then the shorter string is the lexicographically smaller one.")
   >
   > Application: leetcode: #316
   
# 15. Divide & Conquer
- Search a 2D Matrix II, leetcode #240


# 16. Segment Tree
why do we need Segment Tree:
> When we want to sum an array, the worst runtime is O(n) and update it, the runtime is O(1)
> If we have equal number of two operations, the total runtime is O(n)
> However, the update and get sum for a range for segment tree are both `O(log n)`. A segment tree is an array that exhibits a tree structure

```Python
def build(arr):
	n = len(arr)
	tree = [0] * (2 * n)
	
	for i in range(n):
		tree[n + i] = arr[i]
	
	for i in range(n - 1, 0, -1):
		tree[i] = tree[i << 1] + tree[i << 1 | 1]

# n is the length of arr, update arr[p]
def updateTreeNode(n, p, value):
	i = p + n
	tree[i] = value
	
	while i > 1:
		# i is odd, then i ^ 1 is even, both i and i ^ 1 are children
		# i is even, then i ^ 1 is odd, both i and i ^ 1 are children
		tree[i >> 1] = tree[i] + tree[i ^ 1]
		i >>= 1

# query the sum on interval [l, r), n is the length of arr
def query(arr, start, end):
	res = 0
	l = start + n
	r = end + n
	
	while l < r:
	    # l is odd, odd position in tree is always the right child of parent
	    # l += 1, l becomes the left child of the next parent
		if l & 1:
			res += tree[l]
			l += 1
		
		# r is odd
		if r & 1:
			r -= 1
			res += tree[r]
		l >>= 1
		r >>= 1
	return res
```


# 17. Line sweep

What is the problem:
> Given a set of line segments(e.g: `[[x1, y1], [x2, y2]]`) which are represented by the x, y coordinates of their endpoints, we want to find the total set of intersection points

## 17.1 Cross Product application
Computing cross product lies at the heart of many line segments problem. Here are the problems that can be applied:
1. Given 2 directed segments $P_0P_1$ and $P_0P_2$, is $P_0P_1$ clockwise from $P_0P_2$ w.r.t $P_0$?
2. Given $P_0P_1$ and point $P_2$, is $P_2$ on the left side or right side of $P_0P_1$ ?
3. Do $P_1P2$ and $P_3P_4$ intersect?


> 1. Clockwise Problem
> We have the following property:
> let $P_0$ be (0, 0):
> -  if $P_1$ X $P_2$ > 0,   $P_1$ is clockwise from $P_2$ w.r.t $P_0$
> -  if $P_1$ X $P_2$ < 0,  $P_1$ is counter-clockwise from $P_2$ w.r.t $P_0$
> -  if $P_1$ X $P_2$ = 0, $P_1$ is parallel to $P_2$

> 2. Left-side problem
> Equivalent to determining angle $\angle P_0P_1P_2$ is counter-clockwise or not:
> ![[Pasted image 20251015202219.png]]
> 

>3. Intersection
>To determine intersection, check either of the following:
>- both endpoints of $P_1P_2$ are on both sides of $P_3P_4$ and both endpoints of $P_3P_4$ are on both sides of $P_1P_2$
>- an endpoint of one segment lies on the other segment

```Python fold
def crossProduct(v1, v2):
	x1, y1 = v1
	x2, y2 = v2
	return x1 * y2 - x2 * y1
	
def side(segment, p):
	p1, p2 = segment
	return crossProduct(p - p1, p - p2)

def onSegment(segment, p):
	p1, p2 = segment
	x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
	x, y = p
	
	return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)

def intersection(P1P2, P3P4):
	P1, P2 = P1P2[0], P1P2[1]
	P3, P4 = P3P4[1], P3P4[1]
	
	P1_side = side(P3P4, P1)
	P2_side = side(P3P4, P2)
	P3_side = side(P1P2, P3)
	P4_side = side(P1P2, P4)
	
	# first case:
	if ((P1_side > 0 and P2_side < 0) or (P1_side < 0 and P2_side > 0)) and\
		((P3_side > 0 and P4_side < 0) or (P3_side < 0 and P4_side > 0)):
		return True
	elif P1_side == 0 and onSegment(P3P4, P1):
		return True
	elif P2_side == 0 and onSegment(P3P4, P2):
		return True
	elif P3_side == 0 and onSegment(P1P2, P3):
		return True
	elif P4_side == 0 and onSegment(P1P2, P4):
		return True
	else:
		return False
		
```


## 17.2 Line sweep algorithm
Assumption(both assumptions can be relaxed by more advanced algor, these assumptions are just for standard line sweep):
- there are no vertical segments
- only two segments intersect at an intersection
Runtime(`O(n lg n)`): 

```Python fold
# segment: [[[x1, y1], [x2, y2|x1, y1], [x2, y2]], [[x1', y1'], [x2', y2'|x1', y1'], [x2', y2']]]
# each segment is represented as a [[], [|], []], where the first [] 
# contains the (x, y) of left endpoint p1 and the second [] has 
# the right endpoint p2
def lineSweep(lineSegments):
    T = AVLTree(segmentOrder)  # need AVL tree from 9.2
    events = sortEndpoints(lineSegments)
    acc = []
    for p in events:
        segmentID = p[3]
        s = lineSegments[segmentID]
        up = above(T, s)
        down = below(T, s)

        if p[2] == 0:
            T.insert(s)
            if up and intersection(up, s):
                acc.append([up, s])

            if down and intersection(down, s):
                acc.append([down, s])
        else:
            if up and down and intersection(up, down):
                acc.append([up, down])
            T.delete(s)
    return acc


# return 1 if a is above b, 0 if a is at b, -1 if a is below b
def segmentOrder(a, b, x0):
    intersect = intersection(a, b)
    if not intersect:
	    # a is the left segment
        if a[0] <= b[0]:
	        return side(a, b[0])
	    else:
		    return side(b, a[0]) * (-1)
    else:
        # x be the intersection point of a & b
        # x0 > x
        Right_to_intersection = ((a[1][0] - a[0][0]) * (b[1][0] - b[0][0]) * (b[0][1] - a[0][1]) - (a[1][0] - a[0][0]) * (b[1][1] - b[0][1]) * b[0][0] + (b[1][0] - b[0][0]) * (a[1][1] - a[0][1]) * a[0][0])  < \

        ((b[1][0] - b[0][0]) * (a[1][1] - a[0][1]) * x0  - (a[1][0] - a[0][0]) * (b[1][1] - b[0][1]) * x0)
        if Right_to_intersection:
            return a[1][1] - b[1][1]
        else:
            return a[0][1] - b[0][1]

def sortEndpoints(lineSegments):
    acc = []
    for i in range(len(lineSegments)):
        # x-coord, y-coord, left/right, segmentID
        acc.append((lineSegments[i][0][0], lineSegments[i][0][1], 0, i))
        acc.append((lineSegments[i][1][0], lineSegments[i][1][1], 1, i))

    n = len(acc)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(acc, n, i)

    for i in range(n - 1, 0, -1):
        acc[0], acc[i] = acc[i], acc[0]
        sift_down(acc, i, 0)
    return acc
  

def above(T: AVLTree, s):
    return T.predecessor(s)
  

def below(T: AVLTree, s):
    return T.successor(s)

  
# return True if e1 > e2
def comparison(e1, e2):
    if e1[0] > e2[0]:
        return True
    elif e1[0] < e2[0]:
        return False
    else:
        if e1[2] > e2[2]:
            return True
        elif e1[2] < e2[2]:
            return False
        else:
            return e1[1] > e2[1]
  

def sift_down(h, n, i):
    curr_p = i
    while curr_p < n:
        next_p = curr_p
        l = 2 * curr_p + 1
        r = 2 * curr_p + 2

        if l < n and comparison(h[next_p], h[l]):
            next_p = l
        if r < n and comparison(h[next_p], h[r]):
            next_p = r
        if curr_p != next_p:
            h[curr_p], h[next_p] = h[next_p], h[curr_p]
            curr_p = next_p
        else:
            break
  

```

# 18. Bit operation
bit operations:
```Python group:18
a = 4 ^ 5  # a: 1(4 XOR 5 bitwise)
a = a >> 1 # a: 0 (a // 2)
a = a << 1 # a: 2 (a * 2)
a = 4 & 5  # a: 4 (a AND 5 bitwise)
a = 4 | 5  # a: 5 (a OR 5 bitwise)
a = ~5     # a: -6 (reverse every bit of the number)
```

application:
加减:

# 19. MergeSort
In-place template:
```Python fold
def Merge(arr, l, m, r):
	# create 2 temporary backup arrays
	larr = arr[l:m + 1]
	rarr = arr[m+1:r + 1]
	
	lsize, rsize = len(larr), len(rarr)
	pleft, pright = 0, 0
	curr = l
	
	while pleft < lsize and pright < risze:
		if larr[pleft] <= rarr[pright]:
			arr[curr] = larr[pleft]
			pleft += 1
		else:
			arr[curr] = rarr[pright]
			pright += 1
		curr += 1
	
	while pleft < lsize:
		arr[curr] = larr[pleft]
		pleft += 1
		curr += 1
	
	while pright < rsize:
		arr[curr] = rarr[pright]
		pright += 1
		curr += 1
	
	


def MergeSort(arr):
	n = len(arr)
	
	subArraySize = 1
	while subArraySize <= n - 1:
		
		# Merge every pair of subarrays in arr
		l = 0
		while l < n - 1:
			mid = min(l + subArraySize - 1, n - 1)
			r = min(l + 2 * subArraySize - 1, n - 1)
			
			merge(arr, l, mid, r)
			l += 2 * subArraySize
		subArraySize *= 2
```

# 20. QuickSelect
QuickSelect:
- assumption: all elements in `arr` must be distinct
- average runtime: O(n)
- worst runtime: O($n^2$), when the `arr` is sorted
```Python fold
# transform arr[l..r] and moves elemenets <= pivot to left and 
# elements > pivot to right, return pivot position
def partition(arr, l, r):
	pivot = arr[r]
	i = l # i marks the progressing pivot position
	for j in range(l, r):
		# loop arr and moves elements that <= pivot to arr[1..i-1]
		if arr[j] <= pivot:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[i], arr[r] = arr[r], arr[i]
	return i

# select the kth smallest elements from arr[l..r], k starts with 1
def quickSelect(arr, l, r, k):
	pivot = partition(arr, l, r)
	# pivot matches the pivot element position in the sorted array
	# thus, if pivot is k -1, then the pivot element is the kth smallest
	
	if pivot - l == k - 1:
		return arr[pivot]
	elif pivot - l > k - 1:
		return quickSelect(arr, l, pivot - 1, k)
	else:
		return quickSelect(arr, pivot + 1, r, k - (pivot - l + 1))	
```

QuickSort:


Q:
- Kth smallest element in a sorted matrix (leetcode #378)

# 21. String Matching