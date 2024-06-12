
from collections import deque

# Define the grid
grid = [
    [0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0]
]

# Define the start and end points
start = (1, 0)
end = (5, 8)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue with the start point
queue = deque([(start, 0, [start])])

while queue:
    (x, y), jumps, path = queue.popleft()
    if (x, y) == end and jumps == 3:
        print(path)
        break
    if jumps < 3:
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 9 and 0 <= ny < 9 and grid[nx][ny] == 0:
                queue.append(((nx, ny), jumps + 1, path + [(nx, ny)]))
