
from collections import deque

# Define the grid
grid = [
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0]
]

# Define the starting and ending points
start = (13, 7)
end = (0, 0)

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
        if 0 <= nx < 14 and 0 <= ny < 14 and grid[nx][ny] == 0 and (nx, ny) not in visited:
            visited.add((nx, ny))
            new_diagonal_jumps = diagonal_jumps
            if dx != 0 and dy != 0:
                new_diagonal_jumps += 1
            queue.append(((nx, ny), new_diagonal_jumps, path + [(nx, ny)]))
