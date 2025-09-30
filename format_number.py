def format_number(number):
    #Format a phone number into the format +X (XXX) XXX-XXXX
    code_1 = "+" + number[0]
    code_2 = " ("+number[1:4]+") "
    code_3 = number[4:7] + "-"
    code_4 = number[7:]
    return code_1 + code_2 + code_3 + code_4
