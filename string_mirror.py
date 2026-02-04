'''
String Mirror
Given a string, return a new string that consists of the given string with a reversed copy of itself appended to the end of it.
'''
def mirror(s):
    return s + s[::-1]