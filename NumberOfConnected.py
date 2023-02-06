# 323. Number of Connected Components in an Undirected Graph
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Solution 1 - Using DFS. O(V) + O(E) + O(n) time complexity. Space : O(n) + O(E)


        # if n == 1:
        #     return 1

        # seen = set()
        # adjList = dict()
        # res = 0

        # for i in range(n):
        #     adjList[i] = []

        # for e in edges:
        #     adjList[e[0]].append(e[1])
        #     adjList[e[1]].append(e[0])


        # def dfs(node):
        #     if node in seen:
        #         return

        #     seen.add(node)

        #     for n in adjList[node]:
        #         dfs(n)

        
        # for i in range(n):
        #     if i not in seen:
        #         dfs(i)
        #         res += 1

        # return res


        # Solution 2 - Find and Union Method. Best solution 

            
        par = []
        ranks = [1] * (n)

        for i in range(n):
            par.append(i)
        

        def find(n):

            while n != par[n]:
                n = par[n]
                par[n] = par[par[n]] # Compression step for extra optimization 

            return n

        

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False

            if ranks[p1] >= ranks[p2]:
                par[p2] = p1
                ranks[p1] += 1
            else:
                par[p1] = p2
                ranks[p2] += 1

            return True

        

        for e in edges:
            if union(e[0], e[1]):
                n -= 1
            
        
        return n
        





# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2



# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
