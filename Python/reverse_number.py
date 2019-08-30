"""
Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

 123 ->  321
-456 -> -654
1000 ->    1
"""

def reverse_number(n):  
    return int(str(n)[::-1] if n >=0 else "-"+str(n)[:0:-1])

print(reverse_number(123))
print(reverse_number(-123))
print(reverse_number(1000))
print(reverse_number(4321234))
print(reverse_number(5))
print(reverse_number(0))
print(reverse_number(98989898))
