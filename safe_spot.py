def find_landing_spot(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    safest_sum = float('inf')
    safest_pos = None

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                total = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        total += matrix[nr][nc]
                if total < safest_sum:
                    safest_sum = total
                    safest_pos = [r, c]

    return safest_pos

print(find_landing_spot([[1, 0], [2, 0]]))