import functools

@functools.lru_cache(maxsize=None)
def fiboCache(n):
    if(n <= 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fiboCache(n-1) + fiboCache(n-2)
    
print(fiboCache(50))


# def fib_iterative(n):
#     """Calculates the n-th Fibonacci number using iteration."""
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1

#     # Initialize the first two Fibonacci numbers
#     a, b = 0, 1
#     # Loop n-1 times because we already have F(1)
#     for _ in range(n - 1):
#         # Calculate the next Fibonacci number and update a, b
#         a, b = b, a + b
#     return b

# # Example usage:
# # print(fib_iterative(50)) # Fast and memory efficient