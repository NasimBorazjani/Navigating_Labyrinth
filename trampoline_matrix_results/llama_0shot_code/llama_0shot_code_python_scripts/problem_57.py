
from collections import deque

def is_valid(i, j, visited, grid):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and not visited[i][j] and grid[i][j] == 0

def bfs(start, end, grid):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    queue = deque([(start, 0, 0, [start])])
    visited[start[0]][start[1]] = True
    while queue:
        i, j, diag, path = queue.popleft()
        if (i, j) == end:
            return path
        for x, y in [(i-2, j-1), (i-2, j+1), (i+2, j-1), (i+2, j+1), (i-1, j-2), (i-1, j+2), (i+1, j-2), (i+1, j+2)]:
            if is_valid(x, y, visited, grid) and diag + 1 <= 4:
                queue.append(((x, y), diag + 1, path + [(x, y)]))
                visited[x][y] = True

grid = [
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0]
]

start, end = (11, 2), (3, 10)
print(bfs(start, end, grid))
