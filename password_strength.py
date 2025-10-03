def check_strength(password):
    counter = 0
    special_characters = ["!","@","#","$","%","^","&","*"]
    has_upper = False
    has_lower = False
    both_case = False
    has_number = False
    has_symbol = False
    if len(password) >= 8:
        counter +=1
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
    if has_upper and has_lower:
        both_case = True
    eval_rules = [both_case,has_number,has_symbol]
    for rule in eval_rules:
        if rule:
            counter += 1
    if counter < 2:
        return "weak"
    if counter >= 2 and counter < 4:
        return "medium"
    if counter == 4:
        return "strong"
 
print(check_strength("S3cur3P@ssw0rd"))