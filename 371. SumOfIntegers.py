# https://leetcode.com/problems/sum-of-two-integers/description/
# 371. Sum of Two Integers


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        carry = True

        while carry:
            res = a ^ b
            carry = (a & b) << 1
            a, b = res & mask, carry & mask
        
        # A 32-bit signed integer is positive if the 32nd bit is a 0 and is negative if the 32nd bit is a 1. If we divide our mask (0xffffffff) by 2, we will get the binary number 0b0111111111111111111111111111111, which has 31 1's. This number is the greatest value we can have before the 32nd bit becomes a 1. Therefore, if our answer a > mask // 2(mask >> 1), it is negative. Otherwise, it is positive and we can just return a itself. 
        if res > (mask >> 1): # mask >> 1(31 bits is the highest number we can store in 32 bits)
            return ~(res ^ mask)

        return res

      
      
# Example 1:

# Input: a = 1, b = 2
# Output: 3
  
# Example 2:

# Input: a = 2, b = 3
# Output: 5
