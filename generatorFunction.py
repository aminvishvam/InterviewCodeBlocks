def fibonacci_generator(limit=None):
    a, b = 0, 1
    while limit is None or a < limit:
        yield a
        a, b = b, a + b

# Example usage:
fib_gen = fibonacci_generator(50)
for number in fib_gen:
    print(number)