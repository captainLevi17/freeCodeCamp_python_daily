'''
Largest Number
Given a string of numbers separated by various punctuation, return the largest number.

The given string will only contain numbers and separators.
Separators can be commas (","), exclamation points ("!"), question marks ("?"), colons (":"), or semi-colons (";").

'''
import re

def largest_number(s):
    numbers = re.findall(r'[+-]?\d+(?:\.\d+)?', s)
    if not numbers:
        return None
    return max(map(float, numbers))
