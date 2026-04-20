'''
Name Initials
Given a full name as a string, return their initials.

Names to initialize are separated by a space.
Initials should be made uppercase.
Initials should be separated by dots.
For example, "Tommy Millwood" returns "T.M.".
'''
def get_initials(name):
    parts = name.split()
    initials = [part[0].upper() for part in parts]
    return '.'.join(initials) + '.'