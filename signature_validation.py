'''
Signature Validation
Given a message string, a secret key string, and a signature number, determine if the signature is valid using this encoding method:

Letters in the message and secret key have these values:
a to z have values 1 to 26 respectively.
A to Z have values 27 to 52 respectively.
All other characters have no value.
Compute the signature by taking the sum of the message plus the sum of the secret key.
For example, given the message "foo" and the secret key "bar", the signature would be 57:

f (6) + o (15) + o (15) = 36
b (2) + a (1) + r (18) = 21
36 + 21 = 57
Check if the computed signature matches the provided signature.
'''
import string
def verify(message, key, signature):
    # iterate through a-z and A-Z to get their corresponding values
    # store in a dictionary
    values = {c: i for i, c in enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1)}
   # compute message and key values
    message_values = 0
    key_values = 0
    # iterate through message and key to get their corresponding values
    for char in message:
        if char in values:
            message_values += values[char]
    for char in key:
        if char in values:
            key_values += values[char]
# compute signature and compare to provided signature
    computed_signature = message_values + key_values
    # return True if computed_signature matches provided signature, else False
    if computed_signature == signature:
        message = True
    else:
        message = False

    return message
