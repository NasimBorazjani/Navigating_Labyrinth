
from collections import deque

def is_valid(pos, grid, visited):
    x, y = pos
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and not visited[x][y]

def get_neighbors(pos):
    x, y = pos
    return [(x+i, y+j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

def find_path(grid, start, dest):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    queue = deque([(start, [start])])
    visited[start[0]][start[1]] = True

    while queue:
        pos, path = queue.popleft()
        if pos == dest:
            return path
        for neighbor in get_neighbors(pos):
            if is_valid(neighbor, grid, visited):
                visited[neighbor[0]][neighbor[1]] = True
                queue.append((neighbor, path + [neighbor]))

    return None

grid = [
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1]
]

start, dest = (11, 1), (2, 12)
path = find_path(grid, start, dest)
print(path)
