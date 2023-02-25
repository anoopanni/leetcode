
from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

    # Solution 1 - DP Memoization <-> top-down approach, escape from backtracking
    
        # res = float('inf')
        # cache = {}

        # @lru_cache(None)
        # def backTracking(amount):

        #     # if amount in cache:
        #     #     return cache[amount]

        #     if amount == 0:
        #         return 0

        #     if amount < 0 :
        #         return float('inf')

        #     res = []
        #     for c in coins:
        #         res.append(1 + backTracking(amount - c))
        #     res = min(res)

        #     # cache[amount] = res
        #     return res
            
        # res = backTracking(amount)

        # if res == float('inf'):
        #     return -1

        # return res


    # Solution 2 - Dynamic Programming - Bottom up approach - real OG dynamic way

        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a-c >= 0:
                    
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        return dp[amount] if dp[amount] != float('inf') else -1
    



        # Understanding between global pass vs step wise pass during dynamic programming recursive functions. If you pass the value as an argument, its going to be globally affected and cannot be memorized but if you add it to return value at each step then it will be a successful case when memomized. 

        # Wrong solution example - > 

        # res = float('inf')

        # cache = {}

        # def backTracking(amount, i):

        #     # if amount in cache:
        #     #         return cache[amount]

        #     if amount == 0:
        #         return i

        #     if amount < 0 :
        #         return float('inf')

        #     res = []
        #     for c in coins:
        #         res.append(backTracking(amount - c, i+1))

        #     res = min(res)

        #     # cache[amount] = res
        #     return res
            
            
        # res = backTracking(amount, 0)

        # if res == float('inf'):
        #     return -1

        # return res

        
        

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
  
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
  
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

            


