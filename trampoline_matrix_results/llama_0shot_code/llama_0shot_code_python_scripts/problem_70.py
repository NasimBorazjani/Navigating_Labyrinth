
from collections import deque

grid = [
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0]
]

def is_valid(x, y, px, py):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and (abs(x - px) + abs(y - py)) in [1, 2, 3, 4]

def bfs(start, end):
    queue = deque([(start, [start])])
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-2, 0), (0, -2), (0, 2), (2, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, x, y):
                queue.append(((nx, ny), path + [(nx, ny)]))

start, end = (1, 8), (10, 0)
path = bfs(start, end)
print(path)
