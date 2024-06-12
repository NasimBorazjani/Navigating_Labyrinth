
from collections import deque

# Define the grid
grid = [
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
]

# Define the start and end points
start = (1, 1)
end = (10, 8)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the queue with the start point and 0 diagonal jumps
queue = deque([(start, 0, [start])])

# While there are still points to visit
while queue:
    # Get the current point and number of diagonal jumps
    (x, y), diagonals, path = queue.popleft()

    # If we have reached the end point with exactly 4 diagonal jumps
    if (x, y) == end and diagonals == 4:
        # Print the path and stop the search
        print(path)
        break

    # For each possible move
    for dx, dy in moves:
        # Calculate the new point
        nx, ny = x + dx, y + dy

        # If the new point is inside the grid and not a broken trampoline
        if 0 <= nx < 12 and 0 <= ny < 12 and grid[nx][ny] == 0:
            # Calculate the new number of diagonal jumps
            new_diagonals = diagonals + 1 if dx != 0 and dy != 0 else diagonals

            # If we have not made more than 4 diagonal jumps
            if new_diagonals <= 4:
                # Add the new point to the queue
                queue.append(((nx, ny), new_diagonals, path + [(nx, ny)]))

                # Mark the trampoline as visited by setting it to 1
                grid[nx][ny] = 1
