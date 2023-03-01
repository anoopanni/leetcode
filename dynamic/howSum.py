# target = m
# length of array = n
# Time: O(n^m) -> branching factor * height/level of the tree -> O(n * m^2)
# Space: O(m) -> O(m^2)


memo = {}

# @lru_cache(None)
def howSum(target, nums):

    if target in memo:
        return memo[target]

    if target == 0:
        return []
    
    for n in nums:
        if target - n >= 0:
            res = howSum(target-n, nums)
            if res != None:
                res.append(n)
                memo[target] = res
                return res
            
    memo[target] = None
    return None



print(howSum(7, (3, 4, 3)))  # True 
memo = {}
print(howSum(7, (2,4)))  # False 
memo = {}
print(howSum(10, (2, 20))) # True
memo = {}
print(howSum(3000, (7, 14)))  # False
