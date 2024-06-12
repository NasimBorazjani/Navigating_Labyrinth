
from collections import deque

# Define the grid
grid = [
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1]
]

# Define the start and end points
start = (1, 9)
end = (5, 0)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue with the start point
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next point from the queue
    (x, y), jumps, path = queue.popleft()

    # If this is the end point, return the path
    if (x, y) == end and jumps == 3:
        print(path)
        break

    # If we've made too many jumps, continue
    if jumps > 3:
        continue

    # Add all possible next moves to the queue
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 10 and 0 <= ny < 10 and grid[nx][ny] == 0:
            queue.append(((nx, ny), jumps + 1, path + [(nx, ny)]))
