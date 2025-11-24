'''
Message Validator
Given a message string and a validation string, determine if the message is valid.

A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
Letters are case-insensitive.
Words in the message are separated by single spaces.
'''

def is_valid_message(message, validation):
    words = message.split(" ")
    if len(words) != len(validation):
        return False
    for i in range(len(words)):
        if words[i][0].lower() != validation[i].lower():
            return False
    return True

#Pseudocode:
# Split the message into words
# Check if the length of words matches the length of validation string
# For each word and corresponding letter in validation string:
#    Check if the first letter of the word (lowercased) matches the letter (lowercased)
# If all match, return True, else return False