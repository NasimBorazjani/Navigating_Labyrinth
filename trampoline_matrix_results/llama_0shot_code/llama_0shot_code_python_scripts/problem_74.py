
from collections import deque

def is_valid(x, y, n, m, visited, grid):
    return 0 <= x < n and 0 <= y < m and not visited[x][y] and grid[x][y] == 0

def bfs(start, end, grid):
    n, m = len(grid), len(grid[0])
    visited = [[False]*m for _ in range(n)]
    visited[start[0]][start[1]] = True
    queue = deque([(start, [start])])
    while queue:
        x, y = queue.popleft()[0]
        if (x, y) == end:
            return queue.popleft()[1]
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, n, m, visited, grid):
                visited[nx][ny] = True
                queue.append(((nx, ny), queue[-1][1] + [(nx, ny)]))

grid = [
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]
]

start, end = (11, 3), (1, 10)
print(bfs(start, end, grid))
