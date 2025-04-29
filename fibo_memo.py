# def fib_memoized_dict(n, cache=None):
#     """Calculates Fibonacci using recursion with an explicit memoization cache."""
#     if cache is None:
#         cache = {} # Initialize cache for the first call

#     if n in cache:
#         return cache[n]
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         result = fib_memoized_dict(n - 1, cache) + fib_memoized_dict(n - 2, cache)
#         cache[n] = result # Store the result before returning
#         return result

# Example usage:
# print(fib_memoized_dict(50)) # Much faster than naive recursive

def newFibon(n, cache = None):
    if cache is None:
        cache =  {}

    if n in cache:
        return cache[n]
    if n <= 0 :
        return 0
    elif n == 1:
        return 1
    else:
        result = newFibon(n-1, cache) + newFibon(n-2, cache)
        cache[n] = result
        return result
    
print(newFibon(50))
    

