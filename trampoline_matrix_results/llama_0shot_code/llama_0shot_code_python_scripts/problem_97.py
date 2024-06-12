
from collections import deque

def is_valid(pos, grid, visited):
    x, y = pos
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and not visited[x][y]

def get_neighbors(pos):
    x, y = pos
    return [(x+dx, y+dy) for dx in range(-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0)]

def find_path(grid, start, dest):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    visited[start[0]][start[1]] = True
    queue = deque([(start, [start])])
    while queue:
        pos, seq = queue.popleft()
        if pos == dest:
            return seq
        for nxt in get_neighbors(pos):
            if is_valid(nxt, grid, visited):
                visited[nxt[0]][nxt[1]] = True
                queue.append((nxt, seq + [nxt]))
    return []

grid = [
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    # ...
    [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1]
]

start, dest = (4, 14), (11, 0)
print(find_path(grid, start, dest))
