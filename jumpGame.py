# 55. Jump Game
# https://leetcode.com/problems/jump-game/description/

from functools import lru_cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Solution 1 - DFS with caching

        # n = len(nums)

        # @lru_cache(None)
        # def dfs(i):

        #     if i == n-1:
        #         return True

        #     if i >= n or nums[i] == 0:
        #         return False

        #     for j in range(i+1, i+nums[i]+1):
        #         if dfs(j):
        #             return True
        #     return False
        # return dfs(0)


        # Solution 2 - DP Approach 
        # dp = [False] * len(nums)
        # dp[-1] = True
        # # fill in dynamic programming table
        # for i in range(len(nums)-2, -1, -1):
        #     for j in range(i+1, min(i+nums[i]+1, len(nums))):
        #         if dp[j]:
        #             dp[i] = True
        #             break
        # # return value in first cell of table
        # return dp[0]


        # Solution 3 - Greedy approach 

        # n = len(nums)

        # goal = n-1

        # for i in range(n-2, -1, -1):
        #     if i + nums[i] >= goal:
        #         goal = i 

        # return goal == 0


        # Solution 4 - Greedy approach 2

        # a = 0
        # for val in nums:
        #     if a < 0:
        #         return False
        #     a = max(a, val)
        #     a -= 1
        # return True


        # Solution 5 - Greedy approach 3

        n = len(nums)
        reachable = 0

        for i in range(n):

            if reachable < i:
                return False

            reachable = max(reachable, nums[i]+i)

        return True



# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.






        




