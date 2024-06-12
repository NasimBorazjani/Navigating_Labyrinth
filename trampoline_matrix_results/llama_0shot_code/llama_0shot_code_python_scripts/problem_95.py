
from collections import deque

def is_valid(pos, visited, grid):
    x, y = pos
    return (0 <= x < len(grid) and 0 <= y < len(grid[0]) and 
            grid[x][y] != 1 and not visited[x][y])

def get_neighbors(pos):
    x, y = pos
    return [(x+dx, y+dy) for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), 
                                         (-2, 0), (0, -2), (0, 2), (2, 0)]]

def find_path(grid, start, end):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    queue = deque([(start, [start], 0)])  # (position, path, diagonal_jumps)
    while queue:
        pos, path, d_jumps = queue.popleft()
        if pos == end and d_jumps == 5:
            return path[1:]  # exclude the starting position
        for neighbor in get_neighbors(pos):
            if is_valid(neighbor, visited, grid):
                visited[neighbor[0]][neighbor[1]] = True
                queue.append((neighbor, path + [neighbor], d_jumps + 1))

grid = [
    [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1]
]

start, end = (0, 13), (13, 5)
path = find_path(grid, start, end)
print(path)
