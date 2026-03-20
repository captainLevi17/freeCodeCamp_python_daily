'''
Array Insertion
Given an array, a value to insert into the array, and an index to insert the value at, return a new array with the value inserted at the specified index.

'''
def insert_into_array(arr, value, index):
    return arr[:index] + [value] + arr[index:]