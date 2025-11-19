'''
100 Characters
Welcome to the 100th Daily Coding Challenge!

Given a string, repeat its characters until the result is exactly 100 characters long. If your repetitions go over 100 characters, trim the extra so it's exactly 100.
'''

def one_hundred(chars):
    result = ""
    while len(result) < 100:
        result += chars
    if len(result) > 100:
        result = result[:100]
    return chars
