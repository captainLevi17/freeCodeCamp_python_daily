'''
Perfect Cube Count
Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.

The lower number is not garanteed to be the first argument.
A number is a perfect cube if there exists an integer (n) where n * n * n = number. For example, 27 is a perfect cube because 3 * 3 * 3 = 27.
'''
def count_perfect_cubes(a, b):
    
    low = min(a,b)
    high = max(a,b)
    count = 0
    
    if low < 0:
        n = low * 2
    else:
        n = 0

    while True:
        cube = n ** 3
        if cube > high:
            break
        if cube >= low:
            count += 1
        n += 1

    return count