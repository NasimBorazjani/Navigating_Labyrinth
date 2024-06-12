
from collections import deque

def is_valid(pos, grid, visited):
    x, y = pos
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and not visited[x][y]

def get_neighbors(pos):
    x, y = pos
    return [(x+dx, y+dy) for dx in range(-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0)]

def find_path(grid, start, dest):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    queue = deque([(start, [start])])
    while queue:
        pos, path = queue.popleft()
        if pos == dest:
            return path
        for neighbor in get_neighbors(pos):
            if is_valid(neighbor, grid, visited):
                x, y = neighbor
                visited[x][y] = True
                queue.append((neighbor, path + [neighbor]))
    return None

grid = [
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
]

start = (10, 0)
dest = (1, 12)

path = find_path(grid, start, dest)

print(path)
