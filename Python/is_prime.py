"""
Define a function that takes an integer argument and returns logical value true or false depending on
 if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors
other than 1 and itself.
"""



def is_prime(num):
    if num <= 1 or (num > 3 and num%2==0 ):
        return False
    flag_return = 0
    for n in range(3, num+1, 2):
        if num % n == 0 :
            flag_return +=1
        
    return True if (flag_return == 1 or num ==2 ) else False

print(is_prime(6))