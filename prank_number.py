'''
Prank Number
Given an array of numbers where all but one number follow a pattern, return a new array with the one number that doesn't follow the pattern fixed.

The pattern will be one of:

The numbers increase from one to the next by a fixed amount (addition).
The numbers decrease from one to the next by a fixed amount (subtraction).
For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10].

'''
def fix_prank_number(arr):
    if len(arr) < 3:
        return arr

    # Calculate the differences between consecutive numbers
    differences = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]

    # Determine the common difference (the most frequent one)
    from collections import Counter
    common_diff = Counter(differences).most_common(1)[0][0]

    # Find an index where the difference equals the common difference
    t = None
    for i, d in enumerate(differences):
        if d == common_diff:
            t = i
            break

    # If we can't find any occurrence (shouldn't happen), return as-is
    if t is None:
        return arr

    # Derive the first term of the progression using a known-correct position
    first = arr[t] - t * common_diff

    # Build the expected arithmetic progression and fix the single mismatch
    expected = [first + i * common_diff for i in range(len(arr))]
    for i in range(len(arr)):
        if arr[i] != expected[i]:
            arr[i] = expected[i]
            break

    return arr