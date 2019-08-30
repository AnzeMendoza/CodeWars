"""
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return
true if the string is valid, and false if it's invalid.
This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}.
Thanks to @arnedag for the idea!
All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.
"""
def validBraces(string):
    diccionario = {"(":")", "[":"]", "{":"}"}
    lst_return = []
    lst_return.append(string[0])

    for n in range (1, len(string)):
        if diccionario[lst_return[n-1]] == n:
            lst_return.pop()
        if len (lst_return ) == 0 or len(lst_return) <= 3 : 
            lst_return.append(n)
    
    return True if len(lst_return) == 0 else False
        

print(validBraces( "()" ))
print(validBraces( "([])" ))