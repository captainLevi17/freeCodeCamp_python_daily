def has_exoplanet(readings): 
    # Create a mapping for letters to their corresponding values
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_values = {}
    # Populate the dictionary with letter values
    for i,l in enumerate(letters):
            letter_values[l] = i + 10
    new_list = []

    # Convert readings to their integer values
    for char in readings:
        if char.isalpha():
            new_list.append(letter_values[char.upper()])
        else:
            new_list.append(int(char))
    # Calculate 80% of the average
    average = (sum(new_list) / len(new_list)) * .80
    
    # Check if any reading is less than or equal to 80% of the average
    for i in new_list:
        if i <= average:
            return True
    return False

# Given a string of sensor readings, determine if there is an exoplanet.
# An exoplanet is detected if any reading is 20% less than the average of
# all readings. The function should return True if an exoplanet is detected,
# and False otherwise.
# Each character in the string represents a single reading and should be
# treated as an integer value.
# For example, given the string "665544554", the average of the readings
# is 5.33. Since 20% less than the average is approximately 4.26, and there
# are readings of 4, the function should return True.
# However, given the string "999999", the average is 9, and 20% less than
# the average is 7.2. Since there are no readings of 7 or less, the function
# should return False.
# Letters A-Z represent values 10-35 respectively.