'''
Digit Rotation Escape
Given a positive integer, determine if it, or any of its rotations, is evenly divisible by its digit count.

A rotation means to move the first digit to the end. For example, after 1 rotation, 123 becomes 231.

Check rotation 0 (the given number) first.
Given numbers won't contain any zeros.
Return the first rotation number if one is found, or "none" if not.

'''

def get_rotation(n):
    s = str(n)
    rotations = [s[i:] + s[:i] for i in range(len(s))]
    print(rotations)
    print(len(s))
    
    for i, rotation in enumerate(rotations):
        if int(rotation) % len(s) == 0:
            return i
    
    return "none"