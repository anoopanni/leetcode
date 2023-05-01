# 678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/description/

from functools import lru_cache

class Solution:
    def checkValidString(self, s: str) -> bool:

        # Solution 1 - DFS with memoization - Dynamic approach O(n^3)

        # cache = {}

        # @lru_cache(None)
        # def dfs(i, left):

        #     # if (i, left) in cache:
        #     #     return cache[(i, left)]

        #     if i == len(s) and left == 0:
        #         return True

        #     if left < 0 or i >= len(s):
        #         return False

        #     if s[i] == '(':
        #         if dfs(i+1, left+1):
        #             return True
        #     elif s[i] == ")":
        #         if dfs(i+1, left-1):
        #             return True
        #     elif s[i] == "*":
        #         if dfs(i+1, left+1) or dfs(i+1, left-1) or dfs(i+1, left):
        #             return True
            
        #     # cache[(i, left)] = False
            
        #     return False

        # return dfs(0, 0)



        # Solution 2 - Greedy approach - O(n)


        leftmin, leftmax = 0, 0

        for c in s:
            if c == "(":
                leftmin += 1
                leftmax += 1
            elif c == ")":
                leftmin -= 1
                leftmax -= 1
            else:
                leftmin -= 1
                leftmax += 1

            if leftmax < 0:
                return False
            
            if leftmin < 0:
                leftmin = 0

        return leftmin == 0
      
      

# Example 1:

# Input: s = "()"
# Output: true
  
# Example 2:

# Input: s = "(*)"
# Output: true
  
# Example 3:

# Input: s = "(*))"
# Output: true
