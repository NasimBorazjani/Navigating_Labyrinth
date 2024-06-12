
from collections import deque

def is_valid(i, j, n, m, visited, grid):
    if i < 0 or j < 0 or i >= n or j >= m or visited[i][j] or grid[i][j] == 1:
        return False
    return True

def bfs(start, end, k, grid):
    n, m = len(grid), len(grid[0])
    visited = [[False]*m for _ in range(n)]
    visited[start[0]][start[1]] = True
    q = deque([(start, 0, 0, [])])
    while q:
        x, y, di, path = q.popleft()
        if (x, y) == end and di == k:
            return path + [(x, y)]
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            for _ in range(2):
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, n, m, visited, grid):
                    visited[nx][ny] = True
                    q.append(((nx, ny), di+1, path + [(x, y)]))
                dx, dy = dy, -dx
    return []

grid = [
    [1, 1, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 0, 0]
]

start, end, k = (8, 7), (0, 3), 3
print(bfs(start, end, k, grid))
