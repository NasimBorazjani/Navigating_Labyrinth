
# Define the grid
grid = [
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1]
]

# Define the start and end positions
start = (9, 9)
end = (2, 0)

# Define the possible moves
moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# Define a recursive function to perform the DFS
def dfs(pos, jumps, path):
    # If we have made 3 jumps and reached the end, return the path
    if jumps == 3 and pos == end:
        return path

    # If we have made 3 jumps but not reached the end, return None
    if jumps == 3:
        return None

    # Try all possible moves
    for move in moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])

        # If the new position is valid, continue the DFS
        if 0 <= new_pos[0] < 11 and 0 <= new_pos[1] < 11 and grid[new_pos[0]][new_pos[1]] == 0:
            result = dfs(new_pos, jumps + 1, path + [new_pos])

            # If the DFS found a valid path, return it
            if result is not None:
                return result

    # If no valid path was found, return None
    return None

# Perform the DFS and print the result
print(dfs(start, 0, [start]))
