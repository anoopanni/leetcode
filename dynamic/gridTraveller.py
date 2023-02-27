from functools import lru_cache

# Time: O(2 ^ (n + m))  -> O(n+m)
# Space: O(n+m)

memo = {}
# @lru_cache
def numOfWays(r, c):

    if (r, c) in memo:
        return memo[(r, c)]

    if r == 0 or c == 0:
        return 0
    
    if r == 1 and c == 1:
        return 1
    
    memo[(r, c)] = numOfWays(r-1, c) + numOfWays(c, r-1)
    
    return memo[(r, c)]

print(numOfWays(2, 2))
print(numOfWays(3, 3))
print(numOfWays(30, 30))
