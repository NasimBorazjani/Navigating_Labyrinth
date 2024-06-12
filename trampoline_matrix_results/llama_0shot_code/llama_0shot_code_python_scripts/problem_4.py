
from collections import deque

def bfs(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[-1]*cols for _ in range(rows)]
    queue = deque([((8, 1), 0, [])])
    while queue:
        (x, y), jumps, path = queue.popleft()
        if (x, y) == (0, 5):
            if jumps == 3:
                return [(x, y) for x, y in path[::-1]]
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and visited[nx][ny] != jumps+1:
                visited[nx][ny] = jumps+1
                queue.append(((nx, ny), jumps+1, [(nx, ny)] + path))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and visited[nx][ny] != jumps:
                visited[nx][ny] = jumps
                queue.append(((nx, ny), jumps, [(nx, ny)] + path))

grid = [
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 1]
]

print(bfs(grid))
