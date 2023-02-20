# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/description/


class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.dynamic(nums[:-1]), self.dynamic(nums[1:]))


    def dynamic(self, nums):
        rob1, rob2 = 0, 0


        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
      
      
 
# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
  
  
# Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
