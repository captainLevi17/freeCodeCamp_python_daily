'''
Captured Chess Pieces
Given an array of strings representing chess pieces you still have on the board, calculate the value of the pieces your opponent has captured.

In chess, you start with 16 pieces:

Piece	Abbreviation	Quantity	Value
Pawn	"P"	8	1
Rook	"R"	2	5
Knight	"N"	2	3
Bishop	"B"	2	3
Queen	"Q"	1	9
King	"K"	1	0
The given array will only contain the abbreviations above.
Any of the 16 pieces not included in the given array have been captured.
Return the total value of all captured pieces, unless...
If the King has been captured, return "Checkmate".

'''

def get_captured_value(pieces):
    total_value = 39
    total_captured = 0
    if "K" not in pieces:
        return "Checkmate"
    for piece in pieces:
        if piece == "K":
            total_captured += 0
        elif piece == "P":
            total_captured += 1
        elif piece == "R":
            total_captured += 5
        elif piece == "N":
            total_captured += 3
        elif piece == "B":
            total_captured += 3
        elif piece == "Q":
            total_captured  += 9


    return total_value - total_captured
