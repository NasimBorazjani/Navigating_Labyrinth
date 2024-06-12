
from collections import deque

# Define the grid
grid = [
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1]
]

# Define the start and end points
start = (3, 0)
end = (9, 11)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Perform a breadth-first search
queue = deque([(start, 0, [start])])
visited = set()
while queue:
    (x, y), diagonals, path = queue.popleft()
    if (x, y) == end and diagonals == 4:
        print(path)
        break
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 13 and 0 <= ny < 13 and grid[nx][ny] == 0 and ((nx, ny), diagonals + (dx != 0 and dy != 0)) not in visited:
            queue.append(((nx, ny), diagonals + (dx != 0 and dy != 0), path + [(nx, ny)]))
            visited.add(((nx, ny), diagonals + (dx != 0 and dy != 0)))
