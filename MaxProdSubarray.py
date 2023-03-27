# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/description/


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Brute force approach

        # res = nums[0]

        # for i in range(len(nums)):
        #     prod = nums[i]
        #     if prod > res:
        #             res = prod
        #     for j in range(i+1, len(nums)):
        #         prod *= nums[j]
        #         if prod > res:
        #             res = prod

        # return res


        # Min Max way - dynamic programming
        # time - O(n)
        # Memory - O(1)


        curMin, curMax = 1, 1
        res = nums[0]


        for n in nums:

            if n == 0:
                curMin = 1
                curMax = 1
        
            # If we do it like this on single line, we do not need to store temperory result of curMax and then use it in next line. 
            curMax, curMin = max(n * curMin, n * curMax, n), min(n * curMin, n * curMax, n)  
            res = max(res, curMax)

        return res

      
      
# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
