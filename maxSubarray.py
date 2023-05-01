# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Solution 1 - Brute Force O(n^2) Solution

        # curSum = 0
        # maxSum = nums[0]


        # for i in range(0, len(nums)):
        #     for j in range(i, len(nums)):
        #         curSum += nums[j]
        #         maxSum = max(maxSum, curSum)
        #     curSum = 0
            
        # return maxSum


        # Solution 2 - Optimised solution - Sliding window technique 

        # curSum = 0
        # maxSum = nums[0]

        # for n in nums:
        #     if curSum < 0:
        #         curSum = 0
        #     curSum += n
        #     maxSum = max(curSum, maxSum)

        # return maxSum


        # Solution 3 - Kaden's algorithm. Highest max at the index i 


        len_n = len(nums)
 
        if len_n == 1:
            return nums[0]
        
        max_current = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len_n):
            max_current = max(max_current + nums[i], nums[i])
            max_sum = max(max_sum, max_current)
        
        return max_sum




# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
  
  
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
  
  
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.




