# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        # Solution 1 - Dfs with memoization 

        # cache = {}

        # @lru_cache
        # def dfs(i, canBuy):
        #     # if (i, canBuy) in cache:
        #     #     return cache[(i, canBuy)]

        #     if i >= len(prices):
        #         return 0

        
        #     res = dfs(i+1, canBuy)

        #     if canBuy:
        #         res = max(dfs(i+1, not canBuy) - prices[i], res)
        #     else:
        #         res = max(dfs(i+2, not canBuy) + prices[i], res)

        #     # cache[(i, canBuy)] = res

        #     return res

        # return dfs(0, True)


        # Solution 2 - Dynamic programming (Bottom up) approach with tabulation 
        n = len(prices)

        stock = [0] * (n)
        no_stock = [0] * (n)
        sold = [0] * (n)

        stock[0] = -prices[0]


        for i in range(1, n):
            stock[i] = max(stock[i-1], no_stock[i-1] - prices[i])
            no_stock[i] = max(no_stock[i-1], sold[i-1])
            sold[i] = stock[i-1] + prices[i]

        return max(sold[n-1], no_stock[n-1])


        # Solution 3 - Space optimisation. You would only need three variables to hold previous state and nothing else hence space can be optimised to be constant. 

        # n = len(prices)

        # stock = -prices[0]
        # no_stock = 0
        # sold = 0

        # for i in range(1, n):
        #     prev_stock = stock
        #     stock = max(stock, no_stock - prices[i])
        #     no_stock = max(no_stock, sold)
        #     sold = prev_stock + prices[i]


        # return max(sold, no_stock)



        

        
# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
  
# Example 2:

# Input: prices = [1]
# Output: 0








