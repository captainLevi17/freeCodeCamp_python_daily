'''
Reverse Sentence
Given a string of words, return a new string with the words in reverse order. For example, the first word should be at the end of the returned string, and the last word should be at the beginning of the returned string.

In the given string, words can be separated by one or more spaces.
The returned string should only have one space between words.

'''

def reverse_sentence(sentence):
    # Split the sentence into words using split() which handles multiple spaces
    words = sentence.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed list of words into a single string with a single space
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence