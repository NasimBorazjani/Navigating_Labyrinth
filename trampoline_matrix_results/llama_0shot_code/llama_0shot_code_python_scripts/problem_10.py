
from collections import deque

grid = [
    [0, 1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0]
]

def is_valid(x, y, visited):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not grid[x][y] and not visited[x][y]

def bfs(start, end):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    queue = deque([(start, [start])])
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited):
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(nx, ny)]))

start, end = (8, 8), (2, 1)
path = bfs(start, end)
print(path)
