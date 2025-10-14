'''
String Count
Given two strings, determine how many times the second string appears in the first.

The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two.
'''

import re

def count(text, parameter):
    # Use a lookahead to find overlapping occurrences
    return len(re.findall(f'(?={re.escape(parameter)})', text))

print(count('101010101010101010101', '101'))
