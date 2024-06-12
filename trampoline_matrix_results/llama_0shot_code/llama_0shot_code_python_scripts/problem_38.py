
from collections import deque

grid = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0]
]

def is_valid(x, y, dx, dy, visited):
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return False
    if grid[x][y] == 1:
        return False
    if dx != 0 and dy != 0:
        return False
    if (x, y) in visited:
        return False
    return True

def bfs(start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if is_valid(x + dx, y + dy, dx, dy, visited):
                queue.append(((x + dx, y + dy), path + [(x + dx, y + dy)]))
                visited.add((x + dx, y + dy))

start, end = (8, 8), (0, 0)
path = bfs(start, end)
print(path)
