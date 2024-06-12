
from collections import deque

def is_valid(i, j, visited):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return False
    if grid[i][j] == 1 or visited[i][j]:
        return False
    return True

def bfs(start, end):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited[start[0]][start[1]] = True
    queue = deque([(start, [start])])
    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        for i, j in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            for k in range(1, 4):
                next_i, next_j = current[0] + k*i, current[1] + k*j
                if is_valid(next_i, next_j, visited):
                    visited[next_i][next_j] = True
                    queue.append(((next_i, next_j), path + [(next_i, next_j)]))

grid = [
    [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1]
]

start, end = (1, 10), (9, 3)
result = bfs(start, end)
print(result)
