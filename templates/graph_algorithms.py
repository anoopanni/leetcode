# Brief into about each algorithms and their implementation can be found here:
# https://anshika-bhargava0202.medium.com/revisiting-graph-algorithms-47b08f307255

# BREADTH FIRST SEARCH and DEPTH FIRST SEARCH - RECURSIVE + ITERATIVE O(M + N) | Example problem: Number of Islands
# time: O(M * N) where M is the number of rows and N is the number of columns
# space: O(M * N) where M is the number of rows and N is the number of columns used for the visit set
from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        # DEPTH FIRST SEARCH - RECURSIVE
        def dfs(r, c):

            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for inc_r, inc_c in directions:
                new_r, new_c = r + inc_r, c + inc_c

                if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == "1" and (new_r, new_c) not in visit:
                    visit.add((new_r, new_c))
                    dfs(new_r, new_c)


        # BREADTH FIRST SEARCH and DEPTH FIRST SEARCH - ITERATIVE
        def bfs_dfs(r, c):

            q = deque()
            q.append((r, c))
            visit.add((r, c))
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            while q:
                curr_r, curr_c = q.popleft()  # Change this to pop() for DFS

                for inc_r, inc_c in directions:
                    new_r, new_c = curr_r + inc_r, curr_c + inc_c

                    if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in visit and grid[new_r][new_c] == "1":
                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))

        islands = 0
                    
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == "1":
                    islands += 1
                    bfs_dfs(r, c) 

        return islands
    
solution_obj = Solution()
print("-------------Number of Islands-----------------")
print(solution_obj.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])) # 1
print(solution_obj.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])) # 3


# KAHN'S ALGORITHM - TOPOLOGICAL SORTING O(V + E) |  Example problem: Course Schedule 1 and 2
# time: O(V + E) where V is the number of vertices and E is the number of edges
# space: O(V + E) where V is the number of vertices and E is the number of edges

# Verify inputs: 
# 1. If all the edges are unique or not --> will create a problem with in_degree and adjaceny list
# 2. all the vertices given are in the range of the number of courses -> I need to handle this seperately otherwise

from collections import defaultdict, deque
class Solution:
    def __init__(self):
        self.res = []

    def canFinish(self, crs: int, pre: List[List[int]]) -> bool:

        adj_list = defaultdict(list)
        in_degree = [0] * crs

        for e1, e2 in pre:
            adj_list[e2].append(e1)
            in_degree[e1] += 1

        q = deque()

        for node in range(len(in_degree)):
            if in_degree[node] == 0:
                q.append(node)

        while q:
            
            course_taken = q.popleft()

            crs -= 1 # Decrement the number of courses taken as we are taking a course
            self.res.append(course_taken)


            for dest_edge in adj_list[course_taken]:
                in_degree[dest_edge] -= 1
                if in_degree[dest_edge] == 0:
                    q.append(dest_edge)

        
        if not crs:
            return True

        self.res = []

        return False
    
solution_obj = Solution()
print("-------------Course Schedule 1 and 2-----------------")
print(solution_obj.canFinish(2, [[1,0]]), solution_obj.res) # True
print(solution_obj.canFinish(2, [[1,0],[0,1]]), solution_obj.res) # False


# UNION FIND - DISJOINT SETS O(1) | Example Problem: Graph Valid Tree and Redundant Connection
# NOTE: find(...)'s cost is dependent on how far the node it was searching for is from the root. Using the naïve implementation of union find, this depth could be N(skewed). 
# If this was the case for all of the calls, we'd have a final cost of O(N^2) amortized to O(A. N)

# time: O(N. A. N) where N is the number of nodes and A is the inverse Ackermann function amortized time complexity which is almost constant O(1)
# space: O(N) to store the parent and rank of each node
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.parents = [i for i in range(self.n)]

    def find(self, node):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]] # Path compression
            node = self.parents[node]

        return node

    def union(self, n1, n2):
        node1 = self.find(n1)
        node2 = self.find(n2) 

        if node1 == node2:
            return True 

        if self.rank[node1] >= self.rank[node2]:
            self.parents[node2] = node1 
            self.rank[node1] += 1
        else:
            self.parents[node1] = node2
            self.rank[node2] += 1

        return False
    

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        union_find_obj = UnionFind(n) 

        for e1, e2 in edges:
            if union_find_obj.union(e1, e2):
                return False
            n -= 1

        if n > 1:
            return False

        return True
    

solution_obj = Solution()
print("-------------Graph Valid Tree and Redundant Connection-----------------")
print(solution_obj.validTree(5, [[0,1],[0,2],[0,3],[1,4]])) # True
print(solution_obj.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])) # False


import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # PRIM'S ALGORITHM - MINIMUM SPANNING TREE (N + E log V) | Example Problem: Min Cost to Connect All Points
        # Time complexity: O(N + E^2 log V) where E is the number of edges; if we use distance [] then it will reduce to O(E^2)
        # Space complexity: O(N + E^2) worst case we push N(N-1) edges in the heap; optimised distance [] will reduce it to O(N)

        n = len(points)

        adj_list = {i:[] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adj_list[i].append([cost, j])
                adj_list[j].append([cost, i])


        visit = set()
        minCost = [[0, 0]]
        res = 0

        while len(visit) != n:
            cost, p = heapq.heappop(minCost)

            if p in visit:
                continue

            res += cost
            visit.add(p)

            for neig in adj_list[p]:
                if neig[1] not in visit:
                    heapq.heappush(minCost, neig)
                
        return res
    

        # Kruskal's Algorithm - Minimum Spanning Tree (N + E log E) | Example Problem: Min Cost to Connect All Points
        # Time complexity: O(N + E log E) where n is the number of points; for sorting all the edges
        # Space complexity: O(E + N) to store the parent and rank of each node

        n = len(points)
        union_find = UnionFind(n)
        edges = []
        res = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(1, n):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                edges.append((i, j, cost))

        edges = sorted(edges, key=lambda x: x[2])

        for e1, e2, cost in edges:
            if not union_find.union(e1, e2):
                res += cost

        return res
    

solution_obj = Solution()
print("-------------Min Cost to Connect All Points-----------------")
print(solution_obj.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])) # 20
print(solution_obj.minCostConnectPoints([[3,12],[-2,5],[-4,1]])) # 18



# DIJKSTRA'S ALGORITHM - SHORTEST PATH O(E log V) | Example Problem: Network Delay Time
# time: O(N + Elog(V)) where N is the number of vertices; for each vertex we are visiting all the edges
# space: O(N + E) where N is the number of vertices; for the adjacency list
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i:[] for i in range(1, n+1)}

        for t in times:
            adjList[t[0]].append([t[2], t[1]])

        visit = set()

        minCost = [(0, k)]

        while minCost:

            cost, p_node = heapq.heappop(minCost)

            if p_node in visit:
                continue

            visit.add(p_node)

            if len(visit) == n:
                return cost

            for neig in adjList[p_node]:
                if neig[1] not in visit:
                    heapq.heappush(minCost, (cost+neig[0], neig[1]))

        return -1
    
solution_obj = Solution()
print("-------------Network Delay Time-----------------")
print(solution_obj.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)) # 2
print(solution_obj.networkDelayTime([[1,2,1]], 2, 2)) # -1


# Bellman Ford Algorithm - Shortest Path O(V * E) | Example Problem: Cheapest Flights Within K Stops
# time: O(N * E) where N is the number of vertices and E is the number of edges
# space: O(N) where N is the number of vertices

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        shortest_dist = [float('inf')] * n
        shortest_dist[src] = 0 

        for _ in range(k+1):
            temp = shortest_dist.copy()
            
            for source, destination, price in flights:
                if shortest_dist[source] + price < temp[destination]:
                    temp[destination] = shortest_dist[source] + price
                
            shortest_dist = temp

        return shortest_dist[dst] if shortest_dist[dst] != float('inf') else -1
    

        # Improved Dijkstra's Algorithm - Shortest Path O(E log V) | Example Problem: Cheapest Flights Within K Stops
        # time: O(E log V) where E is the number of edges and V is the number of vertices
        # space: O(N + E) where N is the number of vertices

        import heapq
        from collections import defaultdict
        adj_list = defaultdict(list)
        stops = [float('-inf')] * n

        for s, d, price in flights:
            adj_list[s].append((d, price))

        min_heap = []
        min_heap.append((0, src, k))

        while min_heap:

            cost_till_now, node, remain_stops = heapq.heappop(min_heap)

            if node == dst:
                return cost_till_now

            # If we have already reached this node with lesser remain_stops and less price then ignore
            if (remain_stops < 0) or (remain_stops <= stops[node]):
                continue

            stops[node] = remain_stops

            for neigh, price in adj_list[node]:
                heapq.heappush(min_heap, (cost_till_now+price, neigh, remain_stops-1))

        return -1

solution_obj = Solution()
print("-------------Cheapest Flights Within K Stops-----------------")
print(solution_obj.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)) # 200
print(solution_obj.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)) # 500


# Union-find is only for undirected graph; the data structure doesn't support it; when we say union(a, b) then it means a is connected to b and b is connected to a.
# Dijkstra's algorithm is used to find the single source shortest path in a directed graph.
# Dijkstra's doesn't work for negative weights; Bellman Ford works for negative weights.

# Bellman Ford is used to find the single source shortest path in a directed graph and undirected graph with negative weights.
# Kruskal's algorithm is used to find the minimum spanning tree in an undirected graph with negative weights.
# Prim's algorithm is used to find the minimum spanning tree in an undirected graph with negative weights.


# Summary:

# Union-Find: Applicable for undirected graphs. Supports operations like union(a, b) to signify bidirectional connection between 'a' and 'b'.
# Dijkstra's Algorithm: Finds the shortest path from a single source in a directed graph without negative weights.
# Bellman-Ford Algorithm: Capable of finding the shortest path from a single source in directed or undirected graphs, including those with negative weights.
# Kruskal's Algorithm: Identifies the minimum spanning tree (MST) in an undirected graph; effective even with negative weights.
# Prim's Algorithm: Also calculates the MST in undirected graphs with negative weights.


# Dijkstra's Algorithm finds the shortest path between a given node (which is called the "source node") and all other nodes in a graph.