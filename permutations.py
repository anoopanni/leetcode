s = "ABC"

def permutations(s: str) -> str:
    res = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            if i!=j:
                res.append(s[i] + s[j])
    return res

print(permutations(s))