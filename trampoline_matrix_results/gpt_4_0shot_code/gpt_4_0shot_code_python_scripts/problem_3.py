
# Define the map of the trampoline park
park = [
    [0, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0]
]

# Define the initial and final positions
start = (8, 6)
end = (0, 0)

# Define the possible moves (diagonal jumps)
moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# Define a recursive function to perform the DFS
def dfs(pos, jumps, path):
    # If we have made exactly 3 jumps and reached the end, return the path
    if jumps == 3 and pos == end:
        return path

    # If we have made more than 3 jumps, return None
    if jumps > 3:
        return None

    # Try each possible move
    for move in moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])

        # If the new position is within the park and the trampoline is not broken
        if 0 <= new_pos[0] < 9 and 0 <= new_pos[1] < 9 and park[new_pos[0]][new_pos[1]] == 0:
            # Perform the DFS from the new position with one more jump
            result = dfs(new_pos, jumps + 1, path + [new_pos])

            # If a valid path was found, return it
            if result is not None:
                return result

    # If no valid path was found, return None
    return None

# Perform the DFS from the start position with 0 jumps and an empty path
path = dfs(start, 0, [start])

# Print the path
print(path)
