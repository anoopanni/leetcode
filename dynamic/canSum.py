# target = m
# length of array = n
# Time: O(n^m) -> branching factor * height/level of the tree -> O(n * m)
# Space: O(m)

memo = {}

# @lru_cache(None)
def canSum(target, nums):

    if target in memo:
        return memo[target]

    if target == 0:
        return True

    for n in nums:
        if target-n >= 0:
            if canSum(target-n, nums):
                memo[target] = True
                return True
            
    memo[target] = False
            
    return False
        

print(canSum(7, (3, 4, 3)))  # True 
memo = {}
print(canSum(7, (2,4)))  # False 
memo = {}
print(canSum(10, (2, 20))) # True
memo = {}
print(canSum(3000, (7, 14)))  # False
