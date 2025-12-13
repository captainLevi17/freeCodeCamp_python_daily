'''
Game of Life
Given a matrix (array of arrays) representing the current state in Conway's Game of Life, return the next state of the matrix using these rules:

Each cell is either 1 (alive) or 0 (dead).
A cell's neighbors are the up to eight surrounding cells (vertically, horizontally, and diagonally).
Cells on the edges have fewer than eight neighbors.
Rules for updating each cell:

Any live cell with fewer than two live neighbors dies (underpopulation).
Any live cell with two or three live neighbors lives on.
Any live cell with more than three live neighbors dies (overpopulation).
Any dead cell with exactly three live neighbors becomes alive (reproduction).
For example, given:

[
  [0, 1, 0],
  [0, 1, 1],
  [1, 1, 0]
]
return:

[
  [0, 1, 1],
  [0, 0, 1],
  [1, 1, 1]
]
Each cell updates according to the number of live neighbors. For instance, [0][0] stays dead (2 live neighbors), [0][1] stays alive (2 live neighbors), [0][2] dies (3 live neighbors), and so on.

'''

def game_of_life(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    # Create a copy of the grid to store the next state
    next_state = [[grid[r][c] for c in range(cols)] for r in range(rows)]

    # Directions for the 8 neighbors
    directions = [(-1, -1), (-1, 0), (-1,
                    1), (0, -1),          (0, 1),
                    (1, -1), (1, 0), (1, 1)]
    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0
            # Count live neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    live_neighbors += grid[nr][nc]
            # Apply the Game of Life rules
            if grid[r][c] == 1:  # Cell is currently alive
                if live_neighbors < 2 or live_neighbors > 3:
                    next_state[r][c] = 0  # Cell dies
            else:  # Cell is currently dead
                if live_neighbors == 3:
                    next_state[r][c] = 1  # Cell becomes alive
    return next_state

