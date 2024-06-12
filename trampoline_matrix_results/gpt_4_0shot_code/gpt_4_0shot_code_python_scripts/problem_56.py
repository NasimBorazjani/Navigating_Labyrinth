
from collections import deque

# Define the grid
grid = [
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0]
]

# Define the start and end points
start = (11, 7)
end = (2, 0)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Perform a breadth-first search
queue = deque([(start, 0, [start])])
visited = set()
while queue:
    (x, y), d, path = queue.popleft()
    if (x, y) == end and d == 4:
        print(path)
        break
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 12 and 0 <= ny < 12 and grid[nx][ny] == 0 and (nx, ny) not in visited:
            visited.add((nx, ny))
            nd = d + 1 if dx != 0 and dy != 0 else d
            queue.append(((nx, ny), nd, path + [(nx, ny)]))
