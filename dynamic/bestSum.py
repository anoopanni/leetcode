# target = target sum -> 'm'
# length of array = n
# Time: O(n^m * m) -> branching factor * height/level of the tree -> O(n * m^2)
# Space: O(m^2) -> O(m^2)

memo = {}

# @lru_cache(None)
def bestSum(target, nums):
    if target in memo:
        return memo[target]

    if target == 0:
        return []

    res = None

    for n in nums:
        if target - n >= 0:
            ret = bestSum(target - n, nums)
            if ret != None:
                if res == None or len(ret) < len(res):
                    ret = ret[:] + [n]
                    # ret.append(n)      Lession -> This cannot work when you are memoizing, you'll face big problems.
                    res = ret
    
    memo[target] = res

    return res

                
print(bestSum(7, (5, 4, 3, 7)))  # True
memo = {}
print(bestSum(8, (2, 3, 5)))  # False
memo = {}
print(bestSum(8, (1, 4, 5))) # True
memo = {}
print(bestSum(100, (1, 2, 25)))  # True 
