
# Define the grid
grid = [
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Define the start and end positions
start = (11, 11)
end = (0, 6)

# Define the possible moves
moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# Define the DFS function
def dfs(pos, grid, path, jumps):
    # If we have made 4 jumps and reached the end, return the path
    if jumps == 4 and pos == end:
        return path

    # If we have made 4 jumps and not reached the end, return None
    if jumps == 4:
        return None

    # Try all possible moves
    for move in moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])

        # If the new position is valid and the trampoline is not broken
        if 0 <= new_pos[0] < 12 and 0 <= new_pos[1] < 12 and grid[new_pos[0]][new_pos[1]] == 0:
            # Add the new position to the path and increase the number of jumps
            new_path = path + [new_pos]
            new_jumps = jumps + 1

            # Recursively call the DFS function with the new position, path and number of jumps
            result = dfs(new_pos, grid, new_path, new_jumps)

            # If a valid path is found, return it
            if result is not None:
                return result

    # If no valid path is found, return None
    return None

# Call the DFS function with the start position, grid, path and number of jumps
path = dfs(start, grid, [start], 0)

# Print the path
print(path)
