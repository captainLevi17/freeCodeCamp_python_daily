def is_spam(number):
    # I separated each number codes (country, area, local)
    country = number.split(" ")[0]
    area = number.split(" ")[1]
    local = number.split(" ")[2]
    # I also need to separate the local number further into two parts
    # the first part is the sum of the digits before the hyphen
    # the second part is the digits after the hyphen
    local_num1 = sum([int(n) for n in local.split("-")[0]])
    local_num2 = local.split("-")[1]
    # I also need to get only the digits from the number
    digits_only = "".join([n for n in number if n.isdigit()])

    #spam conditions are as follows:
    
    #The country code is greater than 2 digits long or doesn't begin with a zero (0).
    if len(country) > 3 or int(country[1]) != 0:
        return True
    #The area code is greater than 900 or less than 200.
    if int(area[1:-1]) > 900 or int(area[1:-1]) < 200:
        return True
    #The sum of first three digits of the local number appears within last four digits of the local number.
    if str(local_num1) in local_num2:
        return True
    #The number has the same digit four or more times in a row (ignoring the formatting characters).
    for i in digits_only:
        if digits_only.count(i) >= 4:
            print(i * 4)
            if i * 4 in digits_only:
                
                print(i)
                return True
    return False
    
