'''
Array Sum Finder
Given an array of numbers and a target number, return the first subset of two or more numbers that adds up to the target.

The "first" subset is the one whose elements have the lowest possible indices, prioritizing the earliest index first.
Each number in the array may only be used once.
If no valid subset exists, return "Sum not found".
Return the matching numbers as an array in the order they appear in the original array.
'''
from itertools import combinations, chain

def find_sum(arr, target):
    # Generate all subsets and check in lexicographic order of indices
    all_combos = sorted(chain(*(combinations(range(len(arr)), size) for size in range(2, len(arr) + 1))))
    for indices in all_combos:
        if sum(arr[i] for i in indices) == target:
            return [arr[i] for i in indices]
    return "Sum not found"