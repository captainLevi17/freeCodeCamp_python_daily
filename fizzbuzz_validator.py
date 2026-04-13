'''
FizzBuzz Validator
Given an array of sequential integers, with multiples of 3 and 5 replaced, determine if it's a valid FizzBuzz sequence.

In a valid FizzBuzz sequence:

Multiples of 3 are replaced with "Fizz".
Multiples of 5 are replaced with "Buzz".
Multiples of both 3 and 5 are replaced with "FizzBuzz".
All other numbers remain as integers.

'''

def is_fizz_buzz(arr):
    def expected(n):
        if n % 15 == 0:
            return "FizzBuzz"
        if n % 3 == 0:
            return "Fizz"
        if n % 5 == 0:
            return "Buzz"
        return n

    if not arr:
        return True

    start = None
    for index, value in enumerate(arr):
        if isinstance(value, int):
            start = value - index
            break

    if start is not None:
        return all(value == expected(start + index) for index, value in enumerate(arr))

    for start_candidate in range(1, 16):
        if all(arr[index] == expected(start_candidate + index) for index in range(len(arr))):
            return True

    return False

