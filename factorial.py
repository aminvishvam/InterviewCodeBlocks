# import functools

# @functools.lru_cache(maxsize=None)

# The block on the upper side will help to develop the cache on this call


def factorial(n): 
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))