# def fib(n):
#     if(n<=0):
#         return n
#     elif n==1:
#         return 1
#     else: 
#         return fib(n-1) + fib(n-2)
    
# print(fib(10))


def newFibo(n):
    if(n <= 0 ):
        return 0
    elif(n == 1):
        return 1
    else: 
        return newFibo(n-1) + newFibo(n-2)
    
print(newFibo(6))
