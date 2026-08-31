'''
Hex Generator
Given a named CSS color string, generate a random hexadecimal (hex) color code that is dominant in the given color.

The function should handle "red", "green", or "blue" as an input argument.
If the input is not one of those, the function should return "Invalid color".
The function should return a random six-character hex color code where the input color value is greater than any of the others.
Example of valid outputs for a given input:
Input	Output
"red"	"FF0000"
"green"	"00FF00"
"blue"	"0000FF"


'''

def generate_hex(color):
    import random

    if color == "red":
        r = random.randint(128, 255)
        g = random.randint(0, 127)
        b = random.randint(0, 127)
    elif color == "green":
        r = random.randint(0, 127)
        g = random.randint(128, 255)
        b = random.randint(0, 127)
    elif color == "blue":
        r = random.randint(0, 127)
        g = random.randint(0, 127)
        b = random.randint(128, 255)
    else:
        return "Invalid color"

    return f"{r:02X}{g:02X}{b:02X}"