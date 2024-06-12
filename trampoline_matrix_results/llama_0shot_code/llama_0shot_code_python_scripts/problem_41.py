
from collections import deque

grid = [
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1]
]

def is_valid(x, y, visited):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not grid[x][y] and not visited[x][y]

def move(x, y, visited):
    visited[x][y] = True
    return (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)

def bfs(start, end):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    queue = deque([(start, [])])
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path + [(x, y)]
        for dx, dy in move(x, y, visited):
            if is_valid(dx, dy, visited):
                queue.append(((dx, dy), path + [(x, y)]))

start, end = (10, 0), (2, 7)
path = bfs(start, end)
print(path[::-1])
