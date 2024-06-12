
# Define the grid
grid = [
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
]

# Define the start and end positions
start = (6, 11)
end = (0, 0)

# Define the possible moves
moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# Define a recursive function to perform the DFS
def dfs(pos, grid, path, jumps):
    # If we have made 4 jumps and reached the end, return the path
    if pos == end and jumps == 4:
        return path

    # If we have made 4 jumps and not reached the end, return None
    if jumps == 4:
        return None

    # Try each possible move
    for move in moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])

        # If the new position is valid, continue the DFS
        if 0 <= new_pos[0] < 12 and 0 <= new_pos[1] < 12 and grid[new_pos[0]][new_pos[1]] == 0:
            result = dfs(new_pos, grid, path + [new_pos], jumps + 1)

            # If the DFS found a valid path, return it
            if result is not None:
                return result

    # If no valid path was found, return None
    return None

# Perform the DFS and print the result
result = dfs(start, grid, [start], 0)
print(result)
