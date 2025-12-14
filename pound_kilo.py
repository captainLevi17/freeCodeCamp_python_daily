'''
Pounds to Kilograms
Given a weight in pounds as a number, return the string "(lbs) pounds equals (kgs) kilograms.".

Replace "(lbs)" with the input number.
Replace "(kgs)" with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
1 pound equals 0.453592 kilograms.
If the input is 1, use "pound" instead of "pounds".
If the converted value is 1, use "kilogram" instead of "kilograms".

'''

def convert_to_kgs(lbs):
    kgs = round(lbs * 0.453592, 2)
    print(kgs)
    if lbs == 1:
        pound_str = "pound"
    else:
        pound_str = "pounds"
    if kgs == 1:
        kilogram_str = "kilogram"
    else:
        kilogram_str = "kilograms"
    return f"{lbs} {pound_str} equals {kgs:.2f} {kilogram_str}."
