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

        n = len(nums)

        goal = n-1

        for i in range(n-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i 

        return goal == 0


        # Solution 4 - Greedy approach 2

#         a = 0
#         for val in nums:
#             if a < 0:
#                 return False
#             a = max(a, val)
#             a -= 1
#         return True








        




