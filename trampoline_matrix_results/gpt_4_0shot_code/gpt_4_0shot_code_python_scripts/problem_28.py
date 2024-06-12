
# Define the map of the trampoline park
park = [
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 1]
]

# Define the start and end positions
start = (8, 0)
end = (0, 6)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Define a recursive function to perform the depth-first search
def dfs(pos, jumps, path):
    # If we have made 3 jumps and reached the end, return the path
    if jumps == 3 and pos == end:
        return path

    # If we have made 3 jumps but not reached the end, return None
    if jumps == 3:
        return None

    # Try each possible move
    for move in moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])

        # If the new position is within the park and the trampoline is not broken
        if 0 <= new_pos[0] < 10 and 0 <= new_pos[1] < 10 and park[new_pos[0]][new_pos[1]] == 0:
            # Perform a depth-first search from the new position
            result = dfs(new_pos, jumps + 1, path + [new_pos])

            # If a valid path was found, return it
            if result is not None:
                return result

    # If no valid path was found, return None
    return None

# Perform the depth-first search from the start position
path = dfs(start, 0, [start])

# Print the path
print(path)
