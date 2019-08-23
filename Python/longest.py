"""
Take 2 strings s1 and s2 including only letters from ato z.
Return a new sorted string, the longest possible, containing distinct letters,

example
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

def longest(s1, s2):
    sr = sorted(s1+s2)
    lst_return = [sr[0]]
    for n in range(1, len(sr)):
        if sr[n-1] != sr[n]:
            lst_return.append(sr[n])
    str_return = "".join(lst_return)
    return str_return    


def longest2(a1, a2):
    return "".join(sorted(set(a1 + a2)))
print(longest(a, b))
print(longest2(a, b))