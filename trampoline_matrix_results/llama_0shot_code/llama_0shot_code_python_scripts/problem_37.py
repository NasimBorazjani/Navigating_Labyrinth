
from collections import deque

grid = [
    [1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1]
]

def is_valid(x, y, visited):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y] and grid[x][y] == 0

def bfs(start, diagonals):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    visited[start[0]][start[1]] = True
    queue = deque([(start, [])])
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == (6, 0):
            return path + [(x, y)]
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-2, -2), (-2, 2), (2, -2), (2, 2)]:
            if abs(dx) + abs(dy) == 3 and is_valid(x + dx, y + dy, visited):
                visited[x + dx][y + dy] = True
                queue.append(((x + dx, y + dy), path + [(x, y)]))

print(bfs((0, 9), 3))
