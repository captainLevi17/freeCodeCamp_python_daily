'''
Evenly Divisible
Given two integers, determine if you can evenly divide the first one by the second one.

'''

def is_evenly_divisible(a, b):
    if b == 0:
        return False
    return a % b == 0