
from collections import deque

def is_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def bfs(grid, start, end):
    n, m = len(grid), len(grid[0])
    visited = [[False]*m for _ in range(n)]
    visited[start[0]][start[1]] = True
    queue = deque([(start, [], 0, 0)])  # (position, path, diagonal jumps, straight jumps)
    while queue:
        i, j, path, d_jumps, s_jumps = queue.popleft()
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if is_valid(x, y, n, m) and not visited[x][y] and grid[x][y] == 0:
                visited[x][y] = True
                new_path = path + [(x, y)]
                if (x, y) == end:
                    return new_path[1:]  # exclude the starting point
                queue.append(((x, y), new_path, d_jumps + (abs(x-i) + abs(y-j) == 2), s_jumps + (abs(x-i) + abs(y-j) == 1)))
        for x, y in [(i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)]:
            if is_valid(x, y, n, m) and not visited[x][y] and grid[x][y] == 0:
                visited[x][y] = True
                new_path = path + [(x, y)]
                queue.append(((x, y), new_path, d_jumps + 1, s_jumps + (abs(x-i) + abs(y-j) == 1)))
    return None

grid = [
    [0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0]
]

start, end = (1, 0), (5, 8)
print(bfs(grid, start, end))
