
# Define the grid
grid = [
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
]

# Define the start and end positions
start = (1, 12)
end = (8, 2)

# Define the possible moves
moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# Initialize the shortest path as None
shortest_path = None

# Define the DFS function
def dfs(pos, path, jumps):
    global shortest_path
    # If we have made 4 jumps and reached the end, update the shortest path
    if jumps == 4 and pos == end:
        if shortest_path is None or len(path) < len(shortest_path):
            shortest_path = path
        return
    # If we have made 4 jumps but not reached the end, return
    if jumps == 4:
        return
    # Try all possible moves
    for move in moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])
        # If the new position is valid and not broken, continue the DFS
        if 0 <= new_pos[0] < 13 and 0 <= new_pos[1] < 13 and grid[new_pos[0]][new_pos[1]] == 0:
            dfs(new_pos, path + [new_pos], jumps + 1)

# Start the DFS
dfs(start, [start], 0)

# Print the shortest path
print(shortest_path)
