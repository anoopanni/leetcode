# Question from citadel OA
# In order to increase their computing efficiency, a cloud services platform added n new processors, where the i th processor provides them a compute of power[i]. However, not all processors can be used to execute a process. If a processor with computing power of power[i] is used, then all processors that have (power[i] + 1) or (power[i]- 1) cannot be used for execution. A processor can only be used once

# Find the maximum possible sum of computing powers of chosen processors.
        
# Example

# Consider n = 7, power= [3, 3, 3, 4, 4, 1, 8]

# One optimal way to choose the processors is:
# Choose the 7th (1-based) processor with computing power 8.
# the 6th, power 1
# the 1st, power 3; now, all the processors with power 4 cannot be chosen.
# the 2nd, power 3
# the 3rd power 3
# The sum of computing powers = 8+ 1 + 3 + 3 +3= 18, which is the maximum possible. So, the answer
# 18.

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






