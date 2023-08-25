

# my code solution 1

from functools import cache


# def outer(a):
#     freq = [0] * (max(a)+1)

#     for it in a:
#         freq[it] += it

#     @cache
#     def dfs(i):

#         if i >= len(freq):
#             return 0
        
#         return max(freq[i] + dfs(i+2), dfs(i+1))
    

#     return dfs(1)



# my code solution 2

def solution(a):

    cache = {}
    
    # @cache
    def dfs(i, prev):
        if (i,prev) in cache:
            return cache[(i, prev)]

        if i >= len(a):
            return 0

        sum1 = 0
        sum2 = dfs(i+1, prev)

        if (a[i] != (prev + 1)) and (a[i] != (prev - 1)):
           sum1 = a[i] + dfs(i+1, a[i])

        res = max(sum1, sum2)

        cache[(i, prev)] = res

        return res
    
    return dfs(0, -1)





# Working code

def maxComputingPower(power):
    freq = [0] * (max(power) + 2)


    # print(freq)
    
    for p in power:
        freq[p] += p

    # print(freq)
    
    dp = [0] * len(freq)
    dp[1] = freq[1]
    
    for i in range(2, len(freq)):
        dp[i] = max(dp[i-1], dp[i-2] + freq[i])
    
    return dp[-1]


# Test case 1

a = [3, 3, 3, 4, 4, 1, 8]
print(maxComputingPower(a))
# print(outer(a))
print(solution(a))

# ans: 18


# Test case 2

b = [1, 2, 3, 4, 5]
print(maxComputingPower(b))
# print(outer(b))
print(solution(b))

# ans: 9

# Test case 3

c = [1, 1, 1, 2]
print(maxComputingPower(c))
# print(outer(c))
print(solution(c))

# ans: 3






