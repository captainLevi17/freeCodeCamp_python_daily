'''
String Math
Given a string with numbers and other characters, perform math on the numbers based on the count of non-digit characters between the numbers.

If the count of characters separating two numbers is even, use addition.
If it's odd, use subtraction.
Consecutive digits form a single number.
Operations are applied left to right.
Ignore leading and trailing characters that aren't digits.
For example, given "3ab10c8", return 5. Add 3 and 10 to get 13 because there's an even number of characters between them. Then subtract 8 from 13 because there's an odd number of characters between the result and 8.

'''

def do_math(s):
    import re
    
    # Extract numbers with their positions and original lengths
    numbers = [(int(m.group()), m.start(), len(m.group())) for m in re.finditer(r'\d+', s)]
    
    if not numbers:
        return 0  # No numbers found, return 0
    
    result = numbers[0][0]  # Start with the first number
    for i in range(1, len(numbers)):
        prev_num, prev_pos, prev_len = numbers[i - 1]
        curr_num, curr_pos, _ = numbers[i]
        
        # Count non-digit characters between the two numbers
        non_digit_count = curr_pos - (prev_pos + prev_len)
        
        if non_digit_count % 2 == 0:  # Even count, use addition
            result += curr_num
        else:  # Odd count, use subtraction
            result -= curr_num
            
    return result