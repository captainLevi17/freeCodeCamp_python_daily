'''
Camel to Snake
Given a string in camel case, return the snake case version of the string using the following rules:

The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
Every uppercase letter in the camel case string starts a new word.
Convert all letters to lowercase.
Separate words with an underscore (_).
'''
def to_snake(camel):
    snake = ""
    for char in camel:
        if char.isupper():
            
            snake += "_" + char.lower()
        else:
            snake += char
    return snake

#Pseudo Code
# 1. Initialize an empty string to hold the snake case result. 
# 2. Loop through each character in the input camel case string.
#    a. If the character is uppercase:
#       i. Append an underscore (_) to the result string.
#       ii. Convert the uppercase character to lowercase and append it to the result string.
#    b. If the character is lowercase, append it directly to the result string.
# 3. Return the resulting snake case string.