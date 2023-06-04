# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/

import math

class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31
        MIN = -1 * (2 ** 31) - 1

        res = 0

        while x:
            digit = int(math.fmod(x, 10)) # (python dumb) -1 % 10 = 9 
            x = int(x / 10)               # (python dumb to round of to integer towards zero) -1 // 10 = -1   

            # Check for overflow before it happens. 
            if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX%10)) or (res < MIN // 10 or (res == MIN // 10 and digit <= MIN%10)):
                return 0

            res = (res * 10) + digit 


        return res
      
      

# Example 1:

# Input: x = 123
# Output: 321
  
  
# Example 2:

# Input: x = -123
# Output: -321
  
  
# Example 3:

# Input: x = 120
# Output: 21
