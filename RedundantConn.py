# 684. Redundant Connection
# https://leetcode.com/problems/redundant-connection/description/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # Solution 1 - Union and find algorithm. very efficient with compression step. 

        par = [i for i in range(len(edges)+1)]
        ranks = [1] * (len(edges) + 1)

        # find the parent of the node
        def find(n):

            while n != par[n]:
                par[n] = par[par[n]] # Compression step -> optimization++
                n = par[n]
            return n
        

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False
            
            if ranks[p1] > ranks[p2]:
                par[p2] = p1
                ranks[p1] += 1
            else:
                par[p1] = p2
                ranks[p2] += 1

            return True


        for e in edges:
            if not union(e[0], e[1]):
                return e


# Example 1:

# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]

# Example 2:

# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
