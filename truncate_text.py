'''
Truncate the Text
Given a string, return it as-is if it's 20 characters or shorter. If it's longer than 20 characters, truncate it to the first 17 characters and append "..." to the end of it (so it's 20 characters total) and return the result.
'''

def truncate_text(text):

    return text if len(text) <= 20 else text[:17] + "..."