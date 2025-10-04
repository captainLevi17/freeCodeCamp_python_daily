def check_strength(password):
    # Evaluates the strength of a given password.
    # Returns "weak", "medium", or "strong".
    # counter to keep track of how many rules are met
    counter = 0
    # list of special characters to check against
    special_characters = ["!","@","#","$","%","^","&","*"]
    #
    has_upper = False
    has_lower = False
    both_case = False
    has_number = False
    has_symbol = False
    # Check length
    if len(password) >= 8:
        counter +=1

    # Check for uppercase, lowercase, number, and special character
    for char in password:
        if char.isupper():
            has_upper = True
            continue
        if char.islower():
            has_lower = True
            continue
        if char.isdigit():
            has_number = True
            continue
        if char in special_characters:
            has_symbol = True
            continue
    # Check if both upper and lower case are present
    if has_upper and has_lower:
        both_case = True
    # Evaluate the rules
    eval_rules = [both_case,has_number,has_symbol]
    for rule in eval_rules:
        if rule:
            counter += 1
    # Determine strength based on counter
    if counter < 2:
        return "weak"
    if counter >= 2 and counter < 4:
        return "medium"
    if counter == 4:
        return "strong"