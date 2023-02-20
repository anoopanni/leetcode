# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):
            
            res += self.NumberOfPalindrome(i, i, s)
            res += self.NumberOfPalindrome(i, i+1, s)
        
        return res


    def NumberOfPalindrome(self, l, r, s):
        n = len(s)
        res = 0

        # while l >=0 and r < n and s[l] == s[r]:
        #     res += 1

        #     l -= 1
        #     r += 1

        # return res

        # Just wanted to change the logic for fun
        if l < 0 or r >= n:
            return res

        while s[l] == s[r]:
            res += 1
            if l-1 >= 0 and r+1 < n:
                l -= 1
                r += 1
            else:
                break

        return res


# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
    
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


