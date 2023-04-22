# 97. Interleaving String
# https://leetcode.com/problems/interleaving-string/description/


from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # Solution 1 - DFS with memoization 

        # cache = {}
        
        # # @lru_cache(None)
        # def dfs(i, j, k):
        #     if (i, j) in cache:
        #         return cache[(i, j)]

        #     if i == len(s1) and j == len(s2) and k == len(s3):
        #         return True

        #     if i < len(s1) and k < len(s3) and s1[i] == s3[k] and dfs(i+1, j, k+1):
        #             return True
        #     if j < len(s2) and k < len(s3) and s2[j] == s3[k] and dfs(i, j+1, k+1):
        #             return True

        #     cache[(i, j)] = False

        #     return False

        # return dfs(0, 0, 0)


        # Solution 2 - Tabulation - bottom up approach.

        m, n = len(s1), len(s2)

        if m+n != len(s3):
            return False

        dp = [[False for j in range(n+1)] for i in range(m+1)]

        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < m and dp[i+1][j] and s1[i] == s3[i+j]:
                    dp[i][j] = dp[i+1][j]
                if j < n and dp[i][j+1] and s2[j] == s3[i+j]:
                    dp[i][j] = dp[i][j+1]
        return dp[0][0]
            


            

            

        

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.


# Example 2:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
  
  
# Example 3:

# Input: s1 = "", s2 = "", s3 = ""
# Output: true
