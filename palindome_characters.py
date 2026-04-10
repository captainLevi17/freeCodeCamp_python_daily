'''
Palindrome Characters
Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).

A palindrome is a string that is the same forward and backward.
If it's not a palindrome, return "none".

'''

def palindrome_locator(s):
    print(s[::-1])
    if s == s[::-1]:
        mid = len(s) // 2
        if len(s) % 2 == 0:
            return s[mid - 1:mid + 1]
        else:
            return s[mid]
    else:
        return "none"
    
palindrome_locator("racecar")