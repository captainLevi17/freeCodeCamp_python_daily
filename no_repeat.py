'''
No Consecutive Repeats
Given a string, determine if it has no repeating characters.

A string has no repeats if it does not have the same character two or more times in a row.

'''

def has_no_repeats(s):

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True