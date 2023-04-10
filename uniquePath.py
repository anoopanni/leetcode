# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/

from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Approach 1 - Top Down with memoization

        # cache = {}
        
        @lru_cache
        def top_down(i, j):
            # if (i, j) in cache:
            #     return cache[(i, j)]

            if i == 0 or j == 0:
                return 0
            
            if i == 1 and j == 1:
                return 1

            res = top_down(i-1, j) + top_down(i, j-1)

            # cache[(i, j)] = res
            return res

        
        return top_down(m, n)


        # # Approach 2 - Bottom Up solution with tabulation

        # table = [[0 for j in range(n)] for i in range(m)]
        # table[0][0] = 1

        # def top_down(r, c):
            
        #     for i in range(r):
        #         for j in range(c):
        #             if i-1 >= 0:
        #                 table[i][j] += table[i-1][j]
        #             if j-1 >= 0:
        #                 table[i][j] += table[i][j-1]

        #     return table[r-1][c-1]

        # return top_down(m, n)
        

        
# Example 1:
        
# Input: m = 3, n = 7
# Output: 28
  
  
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
            



        




