
from collections import deque

def is_valid(pos, grid, visited, current):
    x, y = pos
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 1 or visited[x][y] or pos == current:
        return False
    return True

def get_neighbors(pos):
    x, y = pos
    return [(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1), (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)]

def find_path(grid, start, dest):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    queue = deque([(start, [start])])
    while queue:
        pos, path = queue.popleft()
        if pos == dest:
            return path
        for neighbor in get_neighbors(pos):
            if is_valid(neighbor, grid, visited, pos):
                visited[neighbor[0]][neighbor[1]] = True
                queue.append((neighbor, path + [neighbor]))
    return None

grid = [
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    # ...
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

start = (12, 2)
dest = (3, 13)

path = find_path(grid, start, dest)
print(path)
