# 518. Coin Change II
# https://leetcode.com/problems/coin-change-ii/description/


from functools import lru_cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # Solution 1 - DFS with memoization 

        # cache = {}

        # # @lru_cache(None)
        # def dfs(i, target):
        #     if (i, target) in cache:
        #         return cache[(i, target)]

        #     if target < 0 or i >= len(coins):
        #         return 0
            
        #     if target == 0:
        #         return 1
            
        #     # take, not_take = 0, 0

        #     take = dfs(i, target-coins[i])
        #     not_take = dfs(i+1, target)

        #     res = take + not_take

        #     cache[(i, target)] = res
            
        #     return res

        # return dfs(0, amount)



        # Solution 2 - Dynamic programming approach - bottom up solution
        

        dp = [[0 for i in range(amount+1)] for j in range(len(coins))]

        for i in range(len(coins)):
            dp[i][0] = 1

        for i in range(len(coins)):
            for j in range(1, amount+1):

                if j - coins[i] >= 0:
                    dp[i][j] += dp[i][j-coins[i]]

                if i-1 >= 0:
                    dp[i][j] += dp[i-1][j]

        return dp[len(coins)-1][amount]






# Example 1:

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1



# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
  
  
  
# Example 3:

# Input: amount = 10, coins = [10]
# Output: 1


