
from collections import deque

def get_neighbors(pos, grid):
    row, col = pos
    neighbors = [(row-2, col-1), (row-2, col+1), (row-1, col-2), (row-1, col+2), 
                 (row+1, col-2), (row+1, col+2), (row+2, col-1), (row+2, col+1)]
    valid_neighbors = [n for n in neighbors if 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0]) and grid[n[0]][n[1]] == 0]
    return valid_neighbors

def is_valid(pos, grid, visited):
    return (0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and 
            grid[pos[0]][pos[1]] == 0 and pos not in visited)

def bfs(start, destination, grid):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        pos, path = queue.popleft()
        if pos == destination:
            return path
        for neighbor in get_neighbors(pos, grid):
            if is_valid(neighbor, grid, visited):
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

grid = [[0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1],
        [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
        [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1]]

start = (10, 10)
destination = (1, 0)

path = bfs(start, destination, grid)
print(path)
