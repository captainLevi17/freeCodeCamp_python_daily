'''
Capitalize It
Given a string title, return a new string formatted in title case using the following rules:

Capitalize the first letter of each word.
Make all other letters in each word lowercase.
Words are always separated by a single space.
'''
def title_case(title):
    words = title.split(' ')
    capitalized_words = []
    for i in words:
        word = i[1:].lower()
        capitalized_words.append(i[0].capitalize() + word)
    return ' '.join(capitalized_words)
