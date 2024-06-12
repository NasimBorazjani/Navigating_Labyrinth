
from collections import deque

def is_valid(pos, grid, visited):
    x, y = pos
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and not visited[x][y]

def get_neighbors(pos):
    x, y = pos
    return [(x+dx, y+dy) for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]]

def find_path(grid, start, end):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    queue = deque([(start, [start])])
    visited[start[0]][start[1]] = True

    while queue:
        pos, seq = queue.popleft()
        if pos == end:
            return seq
        if len(seq) < 5:
            for n in get_neighbors(pos):
                if is_valid(n, grid, visited):
                    visited[n[0]][n[1]] = True
                    queue.append((n, seq + [n]))

    return []

grid = [
    [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    # ...
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
]

start, end = (14, 1), (2, 10)
path = find_path(grid, start, end)
print(path)
