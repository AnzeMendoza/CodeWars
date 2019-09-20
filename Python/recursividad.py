
def factorial(n):
    return n*factorial(n-1) if (n != 0) else  1
    
def fibonacci(n):
    return fibonacci(n-1)+fibonacci(n-2) if n>=2 else 1

def binario(n):
    if n/2 <=1:
        print(n%2)
        return n%2
    else:
        print(n//2)
        return binario(int(n//2))

binario(10)