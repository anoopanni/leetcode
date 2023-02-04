# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/description/


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Solution 1 - Brute Force solution. time complexity = O(nlogn) 

        # LEN1 = len(nums1)-1

        # for n in nums2:
        #     nums1[LEN1] = n
        #     LEN1 -= 1
        
        # nums1.sort()


        # Solution 2 - Using extra memory. time complexity = O(m+n)

        # copynum1 = nums1[:]
        # copynum1 = nums1.copy()
        # copynum1 = list(nums1)
        # copynum1 = list()
        # for n in nums1:
        #     copynum1.append(n)

        # print(copynum1, nums1)
        # print(copynum1 is nums1) # Just why there is a problem when i use append() ??

        # p1, p2 = 0, 0
        
        # for p in range(m + n):

        #     if p2 >= n or (p1 < m and copynum1[p1] <= nums2[p2]):
        #         nums1[p] = copynum1[p1]
        #         p1 += 1
        #     else:
        #         nums1[p] = nums2[p2]
        #         p2 += 1

                
        # Solution 3 - O(1) memory and time complexity = O(m+n)

        p1, p2 = m-1, n-1

        for p in range(m+n-1, -1, -1):
            if p2 < 0:
                break

            if p1 < 0 or (p2 >= 0 and nums2[p2] >= nums1[p1]):
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1

                
                
# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
            
        

            


            
            

        







            

        
            





        
        

        

        
