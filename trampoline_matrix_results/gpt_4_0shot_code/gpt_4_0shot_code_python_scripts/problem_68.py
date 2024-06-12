
# Define the grid
grid = [
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
]

# Define the start and end positions
start = (11, 5)
end = (0, 12)

# Define the possible moves (diagonal only)
moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# Define a recursive function to perform the DFS
def dfs(pos, end, grid, path, jumps):
    # If we've reached the end, return the path
    if pos == end and jumps == 0:
        return path

    # If we've made too many jumps, return None
    if jumps < 0:
        return None

    # Try each possible move
    for move in moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])

        # If the new position is valid, continue the search from there
        if (0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0]) and
                grid[new_pos[0]][new_pos[1]] == 0):
            result = dfs(new_pos, end, grid, path + [new_pos], jumps - 1)

            # If the search was successful, return the result
            if result is not None:
                return result

    # If no moves were successful, return None
    return None

# Perform the search and print the result
result = dfs(start, end, grid, [start], 4)
print(result)
