from functools import lru_cache


# # Time: O(2^n) -> O(n)
# # Space: O(n)

# cache = {}

# @lru_cache
# def fib(n):
#     # if n in cache:
#     #     return cache[n]

#     if n <= 2:
#         return 1

#     res = fib(n-1) + fib(n-2)
#     # cache[n] = res 

#     return res


# print(fib(3))
# print(fib(4))
# print(fib(5))
# print(fib(60))


# # Time: O(2 ^ (n + m))  -> O(n * m)
# # Space: O(n+m)

# memo = {}

# # @lru_cache
# def numOfWays(r, c):

#     if (r, c) in memo:
#         return memo[(r, c)]

#     if r == 0 or c == 0:
#         return 0
    
#     if r == 1 and c == 1:
#         return 1
    
#     memo[(r, c)] = numOfWays(r-1, c) + numOfWays(c, r-1)
    
#     return memo[(r, c)]

# print(numOfWays(2, 2)) # 2
# print(numOfWays(3, 3)) # 6
# print(numOfWays(30, 30)) # 30067266499541040


# target = m
# length of array = n
# Time: O(n^m) -> branching factor * height/level of the tree -> O(n * m)
# Space: O(m)

# memo = {}

# # @lru_cache(None)
# def canSum(target, nums):

#     if target in memo:
#         return memo[target]

#     if target == 0:
#         return True

#     for n in nums:
#         if target-n >= 0:
#             if canSum(target-n, nums):
#                 memo[target] = True
#                 return True
            
#     memo[target] = False
            
#     return False
        

# print(canSum(7, (3, 4, 3)))  # True 
# memo = {}
# print(canSum(7, (2,4)))  # False 
# memo = {}
# print(canSum(10, (2, 20))) # True
# memo = {}
# print(canSum(3000, (7, 14)))  # False



# target = m
# length of array = n
# Time: O(n^m) -> branching factor * height/level of the tree -> O(n * m^2)
# Space: O(m) -> O(m^2)


# memo = {}

# # @lru_cache(None)
# def howSum(target, nums):

#     if target in memo:
#         return memo[target]

#     if target == 0:
#         return []
    
#     for n in nums:
#         if target - n >= 0:
#             res = howSum(target-n, nums)
#             if res != None:
#                 res.append(n)
#                 # ret = ret[:] + [n]
#                 memo[target] = res
#                 return res
            
#     memo[target] = None
#     return None



# print(howSum(7, (3, 4, 3)))  # True 
# memo = {}
# print(howSum(7, (2,4)))  # False 
# memo = {}
# print(howSum(10, (2, 20))) # True
# memo = {}
# print(howSum(3000, (7, 14)))  # False


# target = target sum -> 'm'
# length of array = n
# Time: O(n^m * m) -> branching factor * height/level of the tree -> O(n * m^2)
# Space: O(m^2) -> O(m^2)

# memo = {}

# # @lru_cache(None)
# def bestSum(target, nums):
#     if target in memo:
#         return memo[target]

#     if target == 0:
#         return []

#     res = None

#     for n in nums:
#         if target - n >= 0:
#             ret = bestSum(target - n, nums)
#             if ret != None:
#                 if res == None or len(ret) < len(res):
#                     ret = ret[:] + [n]
#                     # ret.append(n)      Lesson -> This cannot work when you are memoizing, you'll face big problems.
#                     res = ret
    
#     memo[target] = res

#     return res

                
# print(bestSum(7, (5, 4, 3, 7)))  # True
# memo = {}
# print(bestSum(8, (2, 3, 5)))  # False
# memo = {}
# print(bestSum(8, (1, 4, 5))) # True
# memo = {}
# print(bestSum(100, (1, 2, 25)))  # True 


# O(n^m * m)  ->  O(n * m^2)
# O(m ^ 2)    ->  O(m ^ 2)

# memo = {}

# # @lru_cache(None)
# def canConstruct(target, wordBank):
#     if target in memo:
#         return memo[target]

#     if target == '':
#         return True

#     for w in wordBank:

#         if target.startswith(w):  # prefix exists
#             if canConstruct(target[len(w):], wordBank): # Remove the prefix from the target
#                 memo[target] = True
#                 return True

#     memo[target] = False

#     return False


# print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
# memo = {}
# print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "board", "e"])) # True
# memo = {}
# print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
# memo = {}
# print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"])) # False 


# O(n^m * m)  ->  O(n * m^2)
# O(m ^ 2)    ->  O(m ^ 2)

# memo = {}

# def countConstruct(target, wordBank):
#     if target in memo:
#         return memo[target]

#     if target == '':
#         return 1    

#     res = 0

#     for w in wordBank:
#         if target.startswith(w):
#             res += countConstruct(target[len(w):], wordBank)

#     memo[target] = res
#     return res


# print(countConstruct("purple", ["pur", "le", "p", "u", "r"])) # True
# memo = {}
# print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
# memo = {}
# print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "board", "e"])) # True
# memo = {}
# print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
# memo = {}
# print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"])) # False



# m = target.length
# n = wordBank.length
# O(n^m * m) time
# O(m) space -> we usually don't include the size of the output/result otherwise it'll also be n^m exponential 


# memo = {}

# # @lru_cache(None)
# def allConstruct(target, wordBank):
#     if target in memo:
#         return memo[target]

#     if target == '':
#         return [[]]
    
#     res = []

#     for w in wordBank:
#         if target.startswith(w):
#             ret = allConstruct(target[len(w):], wordBank)
#             for i in range(len(ret)):
#                 ret[i] = ret[i][:] + [w]
#             res = res[:] + ret[:]

#     memo[target] = res
    
#     return res
            

# print(allConstruct("purple", ("pur", "le", "p", "u", "r"))) # True 
# memo = {}
# print(allConstruct("abcdef", ("ab", "abc", "cd", "def", "abcd"))) # True
# memo = {}
# print(allConstruct("skateboard", ("bo", "rd", "ate", "t", "ska", "sk", "board", "e"))) # True
# memo = {}
# print(allConstruct("enterapotentpot", ("a", "p", "ent", "enter", "ot", "o", "t"))) # True
# memo = {}
# print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeef", ("e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"))) # False





# TABLULATION TECHNIQUE 
# O(n) time
# O(n) space

# def fib(n):
#     Arr = [0] * (n + 1)
#     Arr[1] = 1

#     for i in range(n+1):
#         if i + 1 <= n:
#             Arr[i+1] += Arr[i]

#         if i + 2 <= n:
#             Arr[i+2] += Arr[i]

#     return Arr[n]


# print(fib(6)) # 8
# print(fib(7)) # 13
# print(fib(8)) # 21
# print(fib(50)) #12586269025



# def gridTraveller(r, c):

#     arr = [[0 for j in range(c+1)] for i in range(r+1)]
#     arr[1][1] = 1

#     for i in range(r+1):
#         for j in range(c+1):
#             current = arr[i][j]
#             if i+1 <= r:
#                 arr[i+1][j] += current
#             if j+1 <= c:
#                 arr[i][j+1] += current

#     # print(arr)
#     return arr[r][c]



# print(gridTraveller(2, 2)) # 2
# print(gridTraveller(3, 3)) # 6
# print(gridTraveller(30, 30)) # 30067266499541040



# O(m*n) Time complexity
# O(m) Space complexity

# def canSum(target, arr):
#     table = [False] * (target+1)
#     table[0] = True

#     for i in range(target+1):
#         if table[i] == True:
#             for ele in arr:
#                 if i + ele < (target+1):
#                     table[i+ele] = True
    
#     return table[target]


# print(canSum(7, (3, 4, 3)))  # True 
# print(canSum(7, (2,4)))  # False 
# print(canSum(10, (2, 20))) # True
# print(canSum(3000, (7, 14)))  # False

# m = target.length
# n = wordBank.length
# O(m^2*n) - Time Complexity
# O(m^2) - Space Complexity


# def howSum(target, arr):
#     table = [None] * (target+1)
#     table[0] = []

#     for i in range(target+1):
#         if table[i] != None:
#             for n in arr:
#                 if i+n < (target+1):
#                     combi = [x for x in table[i]]
#                     combi.append(n)
#                     table[i+n] = combi

#     return table[target]

    
# print(howSum(7, (3, 4, 3)))  # True 
# print(howSum(7, (2,4)))  # False 
# print(howSum(10, (2, 20))) # True
# print(howSum(3000, (7, 14)))  # False


# O(m^2 * n) Time Complexity
# O(m^2) Space Complexity

# def bestSum(target, arr):
#     table = [None] * (target+1)
#     table[0] = []

#     for i in range(target+1):
#         if table[i] != None:
#             for e in arr:
#                 if i + e < (target+1):
#                     combi = [x for x in table[i]]
#                     combi.append(e)
#                     if table[i+e] == None or len(table[i+e]) > len(combi):
#                         table[i+e] = combi

#     return table[target]


# print(bestSum(7, (5, 4, 3, 7)))  # [7]
# print(bestSum(8, (2, 3, 5)))  # [3, 5]
# print(bestSum(8, (1, 4, 5))) # [4, 4]
# print(bestSum(100, (1, 2, 25)))  # [25, 25, 25, 25] 
# print(bestSum(100, (25, 1, 2)))  # [25, 25, 25, 25]


# O(m^2 * n)
# O(m) space complexity


# def canConstruct(target, wordBank):
#     table = [False] * (len(target)+1)
#     table[0] = True

#     for i in range(len(target)+1):
#         if table[i]:
#             for ele in wordBank:
#                 # if (i + len(ele)) < (len(target) + 1) and target[i:i + len(ele)] == ele:  Does this line improve efficiency ?
#                 if target[i:i + len(ele)] == ele:
#                     table[i+len(ele)] = True
    
#     return table[len(target)]



# print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
# print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "board", "e"])) # True
# print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
# print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"])) # False 


# O(m^2 * n)
# O(m) space complexity

# def countConstruct(target, wordBank):
#     table = [0] * (len(target)+1)
#     table[0] = 1

#     for i in range(len(target)+1):
#         for w in wordBank:
#             if target[i:i+len(w)] == w:
#                 table[i+len(w)] += table[i]

#     return table[len(target)]



# print(countConstruct("purple", ["pur", "le", "p", "u", "r"])) # 2
# print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
# print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "board", "e"])) # 2
# print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # 4
# print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"])) # 0

# O(n^m) time 
# O(n^m) space

def allConstruct(target, wordBank):
    table = [[]] * (len(target) + 1)
    table[0] = [[]]

    for i in range(len(target) + 1):
        if table[i] != None:
            for w in wordBank:
                if target[i: i+len(w)] == w:
                    newCombi = [x + [w] for x in table[i]]
                    for e in newCombi:
                        res = table[i+len(w)] + [e]
                        table[i+len(w)] =  res
    return table[len(target)]



print(allConstruct("purple", ("pur", "le", "p", "u", "r"))) # [['pur', 'p', 'le'], ['p', 'u', 'r', 'p', 'le']]
print(allConstruct("abcdef", ("ab", "abc", "cd", "def", "abcd", "ef"))) # [['abc', 'def'], ['abcd', 'ef'], ['ab', 'cd', 'ef']]
print(allConstruct("skateboard", ("bo", "rd", "ate", "t", "ska", "sk", "board", "e"))) # [['sk', 'ate', 'board'], ['ska', 't', 'e', 'board']]
print(allConstruct("enterapotentpot", ("a", "p", "ent", "enter", "ot", "o", "t"))) # [['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']]
print(allConstruct("aaaaaaaaaf", ("a", "aa", "aaa", "aaaa", "aaaaa"))) # []
print(allConstruct("", ("a", "aa", "aaa", "aaaa", "aaaaa"))) # [[]]
