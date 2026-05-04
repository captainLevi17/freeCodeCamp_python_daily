'''
Last Letter
Given a string, return the letter from the string that appears last in the alphabet.

If two or more letters tie for the last in the alphabet, return the first one.
Ignore all non-letter characters.

'''

def get_last_letter(s):
    last_letter = ''
    for char in s:
        if char.isalpha():
            if last_letter == '' or char.lower() > last_letter.lower():
                last_letter = char
    return last_letter