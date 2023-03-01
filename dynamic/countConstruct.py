# O(n^m * m)  ->  O(n * m^2)
# O(m ^ 2)    ->  O(m ^ 2)

memo = {}

def countConstruct(target, wordBank):
    if target in memo:
        return memo[target]

    if target == '':
        return 1    

    res = 0

    for w in wordBank:
        if target.startswith(w):
            res += countConstruct(target[len(w):], wordBank)

    memo[target] = res
    return res


print(countConstruct("purple", ["pur", "le", "p", "u", "r"])) # True
memo = {}
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
memo = {}
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "board", "e"])) # True
memo = {}
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
memo = {}
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"])) # False
