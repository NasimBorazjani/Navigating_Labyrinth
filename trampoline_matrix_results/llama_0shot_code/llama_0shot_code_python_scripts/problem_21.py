
from collections import deque

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

def is_valid(x, y, visited):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited.get((x, y)) and grid[x][y] == 0

def get_neighbors(x, y, visited):
    neighbors = []
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-2, 0), (0, -2), (0, 2), (2, 0)]:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, visited):
            neighbors.append((nx, ny))
    return neighbors

def bfs(start, end):
    visited = {start: None}
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            path = []
            while (x, y) is not None:
                path.append((x, y))
                x, y = visited[(x, y)]
            return path[::-1]
        for nx, ny in get_neighbors(x, y, visited):
            queue.append((nx, ny))
            visited[(nx, ny)] = (x, y)

start, end = (1, 9), (5, 0)
print(bfs(start, end))
