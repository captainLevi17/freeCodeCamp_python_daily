'''
Inverted Matrix
Given a matrix (an array of arrays) filled with two distinct values, return a new matrix where all occurrences of one value are swapped with the other.

For example, given:

[
  ["a", "b"],
  ["a", "a"]
]
Return:

[
  ["b", "a"],
  ["b", "b"]
]


'''

def invert_matrix(matrix):
    if not matrix or not matrix[0]:
        return matrix
    
    value1 = matrix[0][0]
    value2 = None
    
    for row in matrix:
        for cell in row:
            if cell != value1:
                value2 = cell
                break
        if value2 is not None:
            break
            
    if value2 is None:
        return matrix
    
    inverted_matrix = []
    
    for row in matrix:
        inverted_row = []
        for cell in row:
            if cell == value1:
                inverted_row.append(value2)
            else:
                inverted_row.append(value1)
        inverted_matrix.append(inverted_row)
    
    return inverted_matrix

print(invert_matrix([["a", "b"], ["a", "a"]]))