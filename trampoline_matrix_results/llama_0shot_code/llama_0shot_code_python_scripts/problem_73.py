
from collections import deque

def is_valid(pos, grid, visited):
    x, y = pos
    return (0 <= x < len(grid) and 0 <= y < len(grid[0]) and 
            grid[x][y] == 0 and pos not in visited)

def get_neighbors(pos):
    x, y = pos
    return [(x+dx, y+dy) for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
                                        (0, 1), (1, -1), (1, 0), (1, 1)]]

def bfs(start, end, grid):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        pos, path = queue.popleft()
        if pos == end:
            return path
        for neighbor in get_neighbors(pos):
            if is_valid(neighbor, grid, visited):
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

grid = [[1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]]

start, end = (1, 12), (8, 2)
path = bfs(start, end, grid)
print(path)
