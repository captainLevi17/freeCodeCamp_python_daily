'''
Trail Traversal
Given an array of strings representing your trail map, return a string of the moves needed to get to your goal.

The given strings will contain the values:

"C": Your current location
"G": Your goal
"T": Traversable parts of the trail
"-": Untraversable parts of the map
Return a string with the moves needed to follow the trail from your location to your goal where:

"R" is a move right

"D" is a move down

"L" is a move left

"U" is a move up

There will always be a single continuous trail, without any branching, from your current location to your goal.

Each trail location will have a maximum of two traversable locations touching it.

For example, given:
[
  "-CT--",
  "--T--",
  "--TT-",
  "---T-",
  "---G-"
]
Return "RDDRDD".
'''

def navigate_trail(map):
    rows, cols = len(map), len(map[0])
    
    # Find starting point
    for r in range(rows):
        if "C" in map[r]:
            c = map[r].index("C")
            break

    directions = [
        (0, 1, "R"),
        (1, 0, "D"),
        (0, -1, "L"),
        (-1, 0, "U")
    ]
    
    solution = ""
    prev = None
    
    while True:
        for dr, dc, move in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) == prev:
                    continue
                
                if map[nr][nc] in ("T", "G"):
                    solution += move
                    prev = (r, c)
                    r, c = nr, nc
                    
                    if map[r][c] == "G":
                        return solution
                    
                    break
