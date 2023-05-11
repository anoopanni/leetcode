50. Pow(x, n)
https://leetcode.com/problems/powx-n/description/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Solution 1 : Brute Force - Times out O(n) times

        # res = 1

        # for i in range(abs(n)):
        #     res *= x

        # if n >= 0:
        #     return res

        # return 1/res



        # Solution 2 - Recursive with divide and conquer
        # Time - O(Log(n))

        def backTrack(n):
            # Handling two base cases
            if n == 0:
                return 1
            if x == 0:
                return 0

            res = backTrack(n//2)
            res *= res
            # Handling if n is odd then you need multiple one more x
            return x * res if n%2 else res

        if n >= 0:
            return backTrack(abs(n))
        else:
            return 1/backTrack(abs(n))


# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
  
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
  
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25


        
