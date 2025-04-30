# def is_prime(number):
#     if number <= 1:
#         False
#     for i in range(2,number): 
#         if number % 2 == 0: 
#             return False
#     return True

# print(is_prime(5))


# import math

# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             return False
#     return True

# number = int(input("Enter a number: "))
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

def checkIsPrime(n):
    if(n <= 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(checkIsPrime(10))