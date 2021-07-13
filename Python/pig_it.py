"""Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
"""

def is_word(word):
    return bool(word>='a' and word <='z') or (word>='A' and word <='Z')


def pig_it(text):
    return ' '.join([ word[1::]+word[0]+'ay' if is_word(word) else word for word in text.split(' ')])

def pig_it_2(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

if __name__ == '__main__':
    print(pig_it('Pig latin is cool !'))
