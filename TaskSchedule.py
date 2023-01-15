# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/description/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int: 
        import heapq
        from collections import defaultdict

        freq = defaultdict(int)

        for t in tasks:
            freq[t] += 1

        maxHeap = [-v for v in freq.values()]

        heapq.heapify(maxHeap)
        q = collections.deque()
        time = 0

        while q or maxHeap:
            time += 1

            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time
      
      
# Example 1:

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: 
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.

# Example 2:

# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.

# Example 3:

# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation: 
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
