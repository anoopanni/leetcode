# 198. House Robber
# https://leetcode.com/problems/house-robber/description/

class Solution:

    def rob(self, nums: List[int]) -> int:

        # Solution 1 - in straight order

        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2



        # Solution 2 - In reverse order

        # rob1, rob2 = 0, 0


        # for num in nums[::-1]:
        #     temp = max(rob1 + num, rob2)
        #     rob1 = rob2
        #     rob2 = temp

        # return rob2
        
        
  
# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
