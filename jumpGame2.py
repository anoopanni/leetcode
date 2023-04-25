# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/description/


from functools import lru_cache

class Solution:
    def jump(self, nums: List[int]) -> int:

        # Solution 1 - Dynamic programming approach, O(n^2) i guess
#         n = len(nums)

#         @lru_cache(None)
#         def dfs(i):

#             if i == n-1:
#                 return 1
            
#             if i >= n or nums[i] == 0:
#                 return 0
            
#             res = float("inf")

#             for j in range(i+1, i+1+nums[i]):
#                 if dfs(j):
#                     res = min(res, 1 + dfs(j))
            
#             return res

#         return dfs(0)-1



        # Solution 2 - Greedy approach

        l, r = 0, 0
        res = 0
        farthest = 0

        while r < len(nums)-1:
            for i in range(l, r+1):
                farthest = max(farthest, i+nums[i])
            l = r+1
            r = farthest
            res += 1
        return res
      
      

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
  
  
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2
