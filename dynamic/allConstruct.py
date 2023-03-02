# m = target.length
# n = wordBank.length
# O(n^m * m) time
# O(m) space -> we usually don't include the size of the output/result otherwise it'll also be n^m exponential 


memo = {}

# @lru_cache(None)
def allConstruct(target, wordBank):
    if target in memo:
        return memo[target]

    if target == '':
        return [[]]
    
    res = []

    for w in wordBank:
        if target.startswith(w):
            ret = allConstruct(target[len(w):], wordBank)
            for i in range(len(ret)):
                ret[i] = ret[i][:] + [w]
            res = res[:] + ret[:]

    memo[target] = res
    
    return res
            

print(allConstruct("purple", ("pur", "le", "p", "u", "r"))) # True 
memo = {}
print(allConstruct("abcdef", ("ab", "abc", "cd", "def", "abcd"))) # True
memo = {}
print(allConstruct("skateboard", ("bo", "rd", "ate", "t", "ska", "sk", "board", "e"))) # True
memo = {}
print(allConstruct("enterapotentpot", ("a", "p", "ent", "enter", "ot", "o", "t"))) # True
memo = {}
print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeef", ("e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"))) # False
