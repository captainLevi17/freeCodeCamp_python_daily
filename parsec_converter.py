'''
Parsec Converter
In a distant galaxy, parsecs are used to measure both time and distance. Given an integer number of parsecs, return its equivalent in time or distance.

If the given integer is odd, it represents time. If it's even, it represents distance.
Use these conversion rates:

Parsecs	Time/Distance
1	2 hours
2	6 light years
Return the converted value as an integer.


'''

def convert_parsecs(parsecs):
    if parsecs % 2 == 0:  # Even, represents distance
        return parsecs * 3  # 2 parsecs = 6 light years, so 1 parsec = 3 light years
    else:  # Odd, represents time
        return parsecs * 2  # 1 parsec = 2 hours