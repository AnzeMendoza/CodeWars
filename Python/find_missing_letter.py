"""
#Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be
at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
"""

def find_missing_letter(chars):
    lst_rtn =list(map(lambda x: chr(x) , range(ord(chars[0]), ord(chars[-1]),1)))
    return  list(set(lst_rtn)-set(chars))[0]

def find_missing_letter2(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))

def find_missing_letter(c):
    return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))


print(find_missing_letter(['a','b','c','d','f']))


#print(list (map(lambda x: chr(x) , range(ord('a'), ord('z')))))
