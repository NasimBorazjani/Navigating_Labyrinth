
from collections import deque

# Define the grid
grid = [
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]
]

# Define the start and end points
start = (12, 2)
end = (3, 13)

# Define the possible moves (diagonal only)
moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# Initialize the queue with the start point
queue = deque([(start, [start])])

while queue:
    # Pop the next point from the queue
    (x, y), path = queue.popleft()

    # Check each possible move
    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        # If the move is within the grid and the trampoline is not broken
        if 0 <= nx < 15 and 0 <= ny < 15 and grid[nx][ny] == 0:
            next_point = (nx, ny)

            # If we've reached the end point, print the path and exit
            if next_point == end and len(path) == 5:
                print(path + [next_point])
                exit(0)

            # Otherwise, add the point to the queue
            queue.append((next_point, path + [next_point]))
