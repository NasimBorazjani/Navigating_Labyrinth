
from collections import deque

def is_valid(i, j, visited):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return False
    if visited[i][j] or grid[i][j] == 1:
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
        for i, j in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-2, 0), (2, 0), (0, -2), (0, 2)]:
            next_pos = (current[0] + i, current[1] + j)
            if is_valid(next_pos[0], next_pos[1], visited):
                visited[next_pos[0]][next_pos[1]] = True
                queue.append((next_pos, path + [next_pos]))

grid = [
    [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0]
]

start = (10, 1)
end = (3, 14)

path = bfs(start, end)
print(path)
