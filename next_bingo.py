'''
Next Bingo Number
Given a bingo number, return the next bingo number sequentially.

A bingo number is a single letter followed by a number in its range according to this chart:

Letter	Number Range
"B"	1-15
"I"	16-30
"N"	31-45
"G"	46-60
"O"	61-75
For example, given "B10", return "B11", the next bingo number. If given the last bingo number, return "B1".


'''

def get_next_bingo_number(n):
    letter = n[0]
    number = int(n[1:])

    if letter == 'B':
        if number < 15:
            return f'B{number + 1}'
        else:
            return 'I16'
    elif letter == 'I':
        if number < 30:
            return f'I{number + 1}'
        else:
            return 'N31'
    elif letter == 'N':
        if number < 45:
            return f'N{number + 1}'
        else:
            return 'G46'
    elif letter == 'G':
        if number < 60:
            return f'G{number + 1}'
        else:
            return 'O61'
    elif letter == 'O':
        if number < 75:
            return f'O{number + 1}'
        else:
            return 'B1'