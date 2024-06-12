
# Define the map of the park
park = [
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0]
]

# Define the start and end positions
start = (14, 10)
end = (2, 1)

# Define the eight possible directions for a jump
directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# Define the recursive function
def dfs(pos, jumps, path):
    # Check if we have reached the destination with the correct number of jumps
    if pos == end and jumps == 0:
        return path
    # Check if we have any jumps left
    if jumps > 0:
        # Try to make a jump in each direction
        for d in directions:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            # Check if the new position is within the park and the trampoline is not broken
            if 0 <= new_pos[0] < 15 and 0 <= new_pos[1] < 15 and park[new_pos[0]][new_pos[1]] == 0:
                # Call the function recursively with the new position, the number of jumps left minus one, and the updated path
                result = dfs(new_pos, jumps - 1, path + [new_pos])
                # If a valid path is found, return it
                if result is not None:
                    return result
    # If no valid path is found, return None
    return None

# Call the function with the start position, the number of jumps, and the initial path
path = dfs(start, 5, [start])

# Print the path
print(path)
