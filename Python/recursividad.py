def factorial(n):
    return n*factorial(n-1) if (n != 0) else  1
    
def fibonacci(n):
    return fibonacci(n-1)+fibonacci(n-2) if n>=2 else 1


for n in range(10):
    print(fibonacci(n))
    