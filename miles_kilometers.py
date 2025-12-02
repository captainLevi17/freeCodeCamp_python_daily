'''
Miles to Kilometers
Given a distance in miles as a number, return the equivalent distance in kilometers.

The input will always be a non-negative number.
1 mile equals 1.60934 kilometers.
Round the result to two decimal places.
'''

def convert_to_km(miles):
    kilometers = round(miles * 1.60934, 2)
    return kilometers

#Pseudocode
# Define a function named convert_to_km that takes one parameter, miles.
# Inside the function, multiply the miles by 1.60934 to convert it to kilometers.
# Round the result to two decimal places using the round() function.
# Return the rounded result.