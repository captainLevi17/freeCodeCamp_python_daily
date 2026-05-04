'''
Spiral Matrix
Given a 2D matrix, return a flat array with all of its values in clockwise order.

The returned array should have the top-left value first, move right along the top row, then down the right column, then left along the bottom row, then up the left column. Repeat inward for any remaining layers.

For example, given:

[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
Return [1, 2, 3, 6, 9, 8, 7, 4, 5].



'''

def spiral_matrix(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result