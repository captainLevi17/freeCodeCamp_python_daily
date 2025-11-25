'''
FizzBuzz
Given an integer (n), return an array of integers from 1 to n (inclusive), replacing numbers that are multiple of:

3 with "Fizz".
5 with "Buzz".
3 and 5 with "FizzBuzz".

'''

def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

#Pseudocode
# Create an empty list to store the results
# Loop through numbers from 1 to n (inclusive)
# For each number, check the following conditions:
# If the number is divisible by both 3 and 5, append "FizzBuzz" to the list
# If the number is divisible by 3, append "Fizz" to the list
# If the number is divisible by 5, append "Buzz" to the list
# If none of the above conditions are met, append the number itself to the list
# Return the list containing the results