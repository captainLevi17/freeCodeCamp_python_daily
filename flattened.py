'''
Flattened
Given an array, determine if it is flat.

An array is flat if none of its elements are arrays.
'''
def is_flat(arr):
    return all(not isinstance(element, list) for element in arr)        