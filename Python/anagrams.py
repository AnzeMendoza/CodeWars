""" What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
    'abba' & 'baab' == true
    'abba' & 'bbaa' == true
    'abba' & 'abbba' == false
    'abba' & 'abca' == false
"""


def anagrams(word, words):
    word_sorted = ''.join(sorted(word))
    return [ i for i in words if word_sorted == ''.join(sorted(i)) ]

def anagrams_2(word, words):
    return [w for w in words if sorted(word)==sorted(w)]

if __name__ == '__main__':
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

