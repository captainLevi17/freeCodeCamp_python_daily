'''
Odd Words
Given a string of words, return only the words with an odd number of letters.

Words in the given string will be separated by a single space.
Return the words separated by a single space.

'''

def get_odd_words(s):
    words = s.split()
    odd_words = [word for word in words if len(word) % 2 == 1]
    return ' '.join(odd_words)