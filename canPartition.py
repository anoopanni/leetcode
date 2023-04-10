# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/description/

from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # calculate total sum of input array
        total_sum = sum(nums)

        # check if total sum is odd
        if total_sum % 2 != 0:
            return False

        # calculate target sum
        target_sum = total_sum // 2

        # # initialize dynamic programming table
        # dp = [[False] * (target_sum+1) for _ in range(len(nums)+1)]
        # for i in range(len(nums)+1):
        #     dp[i][0] = True

        # # fill in dynamic programming table
        # for i in range(1, len(nums)+1):
        #     for j in range(1, target_sum+1):
        #         if nums[i-1] <= j:
        #             dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        #         else:
        #             dp[i][j] = dp[i-1][j]

        # # return value in last row and last column of table
        # return dp[len(nums)][target_sum]




        # # cache = {}

        # @lru_cache(None)
        # def top_down_1(i, s):

        #     # if (i, s) in cache:
        #     #     return cache[(i, s)]

        #     if i >= len(nums):
        #         return False

        #     if s == target_sum:
        #         return True

        #     if top_down_1(i+1, s+nums[i]) or top_down_1(i+1, s):
        #         cache[(i, s)] = True
        #         return True

        #     # cache[(i, s)] = False

        #     return False

        # return top_down_1(0, 0)




        # cache = {}

        @lru_cache(None)
        def top_down_2(i, s):

            # if (i, s) in cache:
            #     return cache[(i, s)]

            if i >= len(nums) or s < 0:
                return False

            if s == 0:
                return True

            if top_down_2(i+1, s-nums[i]) or top_down_2(i+1, s):
                # cache[(i, s)] = True
                return True

            # cache[(i, s)] = False

            return False

        return top_down_2(0, target_sum)
      
      

      
# Test Cases 


# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
  
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

