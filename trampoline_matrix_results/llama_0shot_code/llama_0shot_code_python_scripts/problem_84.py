
from collections import deque

grid = [
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1]
]

def is_valid(pos):
    x, y = pos
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

def get_neighbors(pos):
    x, y = pos
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def bfs(start, end):
    queue = deque([(start, [start])])
    while queue:
        pos, path = queue.popleft()
        if pos == end:
            return path
        for neighbor in get_neighbors(pos):
            if is_valid(neighbor):
                queue.append((neighbor, path + [neighbor]))

start, end = (9, 0), (3, 13)
path = bfs(start, end)
print(path)
