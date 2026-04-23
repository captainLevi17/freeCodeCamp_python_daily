'''
Sorted Array Swap
Given an array of integers, return a new array using the following rules:

Sort the integers in ascending order
Then swap all values whose index is a multiple of 3 with the value before it.
'''

def sort_and_swap(arr):
    sorted_arr = sorted(arr)
    for i in range(3, len(sorted_arr), 3):
        sorted_arr[i], sorted_arr[i - 1] = sorted_arr[i - 1], sorted_arr[i]
    return sorted_arr