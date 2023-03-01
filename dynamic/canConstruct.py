memo = {}

# @lru_cache(None)
def canConstruct(target, wordBank):
    if target in memo:
        return memo[target]

    if target == '':
        return True

    for w in wordBank:

        if target.startswith(w):  # prefix exists
            if canConstruct(target[len(w):], wordBank): # Remove the prefix from the target
                memo[target] = True
                return True

    memo[target] = False

    return False


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
memo = {}
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "board", "e"])) # True
memo = {}
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
memo = {}
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"])) # True
