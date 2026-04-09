'''
Capitalized Fibonacci
Given a string, return a new string where each letter is capitalized if its index is a Fibonacci number, and lowercased otherwise.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

The first character is at index 0.
If the index of non-letter characters is a Fibonacci number, leave it unchanged.

'''

def capitalized_fibonacci(s):
    # Generate Fibonacci numbers until we exceed the length of the string
    fibs = set()
    a, b = 0, 1
    while a < len(s):
        fibs.add(a)
        a, b = b, a + b

    # Build the new string with appropriate capitalization
    result = []
    for i, char in enumerate(s):
        if i in fibs and char.isalpha():
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)
