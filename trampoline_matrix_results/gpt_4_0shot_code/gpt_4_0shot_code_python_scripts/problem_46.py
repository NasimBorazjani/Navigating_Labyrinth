
from collections import deque

# Define the grid
grid = [
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1]
]

# Define the start and end points
start = (1, 0)
end = (7, 11)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue with the start point
queue = deque([(start, [start])])

while queue:
    # Pop the next point from the queue
    (x, y), path = queue.popleft()

    # Check each possible move
    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        # If the move is within the grid and the trampoline is not broken
        if 0 <= nx < 12 and 0 <= ny < 12 and grid[nx][ny] == 0:
            # If we've reached the end point, print the path and exit
            if (nx, ny) == end and len(path) == 5:
                print(path + [(nx, ny)])
                exit(0)

            # Otherwise, add the new point to the queue
            queue.append(((nx, ny), path + [(nx, ny)]))
