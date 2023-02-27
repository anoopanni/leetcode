from functools import lru_cache


# Time: O(2^n) -> O(n)
# Space: O(n)

cache = {}

@lru_cache
def fib(n):
    # if n in cache:
    #     return cache[n]

    if n <= 2:
        return 1

    res = fib(n-1) + fib(n-2)
    # cache[n] = res 

    return res


print(fib(3))
print(fib(4))
print(fib(5))
print(fib(60))
