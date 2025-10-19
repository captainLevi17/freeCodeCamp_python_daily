'''
HTML Attribute Extractor
Given a string of a valid HTML element, return the attributes of the element using the following criteria:

You will only be given one element.
Attributes will be in the format: attribute="value".
Return an array of strings with each attribute property and value, separated by a comma, in this format: ["attribute1, value1", "attribute2, value2"].
Return attributes in the order they are given.
If no attributes are found, return an empty array.
'''


import re

def extract_attributes(element):
    # Regular expression to match attributes in the form attribute="value"
    pattern = r'(\w+)\s*=\s*"([^"]*)"'
    
    # Find all matches (returns a list of tuples)
    matches = re.findall(pattern, element)
    result = []
    #Unpack tuples and append to result list
    for match in matches:
        pair = match[0] + ", " + match[1]
        result.append(pair)

    
    return result

