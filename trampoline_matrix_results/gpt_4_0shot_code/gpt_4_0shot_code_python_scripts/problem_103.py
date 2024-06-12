
# Define the grid
grid = [
    [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0]
]

# Define the start and end positions
start = (10, 1)
end = (3, 14)

# Define the possible moves
moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# Initialize the stack with the start position and an empty path
stack = [(start, [start])]

# While there are positions to explore
while stack:
    # Get the current position and path
    (x, y), path = stack.pop()

    # If this is the end position
    if (x, y) == end and len(path) == 6:
        # Print the path
        print(path)
        break

    # For each possible move
    for dx, dy in moves:
        # Compute the new position
        nx, ny = x + dx, y + dy

        # If the new position is inside the grid and is not a broken trampoline
        if 0 <= nx < 15 and 0 <= ny < 15 and grid[nx][ny] == 0:
            # Add the new position to the stack
            stack.append(((nx, ny), path + [(nx, ny)]))
