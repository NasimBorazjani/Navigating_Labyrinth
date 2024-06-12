
from collections import deque

# Define the grid
grid = [
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1]
]

# Define the start and end points
start = (10, 0)
end = (1, 12)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue with the start point
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next point from the queue
    (x, y), jumps, path = queue.popleft()

    # If this point is the end point, print the path and exit
    if (x, y) == end and jumps == 5:
        print(path)
        break

    # Add all possible next points to the queue
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 15 and 0 <= ny < 15 and grid[nx][ny] == 0:
            queue.append(((nx, ny), jumps + 1, path + [(nx, ny)]))
