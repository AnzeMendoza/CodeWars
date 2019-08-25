"""
Welcome.
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.
"""

def alphabet_position(text):
    str_return = "".join( j if ord(j)>=ord("a") and ord(j)<=ord("z") else "" for j in text.lower() )
    return " ".join( str( int(ord (i) - ord("a") + 1)) for i in str_return)

def alphabet_position2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

print (alphabet_position("The narwhal bacons at midnight."))
print (alphabet_position2("The narwhal bacons at midnight."))