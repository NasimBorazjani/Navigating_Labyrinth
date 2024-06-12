
from collections import deque

# Define the grid
grid = [
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1]
]

# Define the start and end points
start = (2, 11)
end = (8, 1)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Perform a breadth-first search
queue = deque([(start, 0, [start])])
visited = set()
while queue:
    (x, y), diagonal_jumps, path = queue.popleft()
    if (x, y) == end and diagonal_jumps == 4:
        print(path)
        break
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 12 and 0 <= ny < 12 and grid[nx][ny] == 0 and (nx, ny) not in visited:
            visited.add((nx, ny))
            new_diagonal_jumps = diagonal_jumps + 1 if dx != 0 and dy != 0 else diagonal_jumps
            queue.append(((nx, ny), new_diagonal_jumps, path + [(nx, ny)]))
