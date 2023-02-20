# https://leetcode.com/problems/longest-palindromic-substring/
# 5. Longest Palindromic Substring


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Solution 1 - search from inner index

        n = len(s)

        res = ()
        resLen = 0

        for i in range(n):

            # for odd length  

            l, r = i, i

            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r-l+1
                    res = (l, r+1)
                l -= 1
                r += 1
            
            # for even length
            l, r = i, i+1

            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r-l+1
                    res = (l, r+1)
                l -= 1
                r += 1

        return s[res[0]: res[1]]


        # Solution 2 - Dynamic solution 


        





# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.


# Example 2:

# Input: s = "cbbd"
# Output: "bb"
            
            





