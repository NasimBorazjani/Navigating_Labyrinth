
from collections import deque

# Define the grid
grid = [
    [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1]
]

# Define the start and end points
start = (0, 13)
end = (13, 5)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue with the start point
queue = deque([(start, 0, [start])])

while queue:
    (x, y), d, path = queue.popleft()
    if (x, y) == end and d == 5:
        print(path)
        break
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 15 and 0 <= ny < 15 and grid[nx][ny] == 0:
            queue.append(((nx, ny), d + 1, path + [(nx, ny)]))
