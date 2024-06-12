
from collections import deque

def is_valid(pos, grid, visited):
    x, y = pos
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1 and not visited[x][y]

def get_neighbors(pos):
    x, y = pos
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]

def bfs(start, end, grid):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    queue = deque([(start, [start], 0)])  # (position, path, diagonal_jumps)
    while queue:
        pos, path, dj = queue.popleft()
        if pos == end:
            return path[1:] if dj == 3 else None  # Exclude start position
        visited[pos[0]][pos[1]] = True
        for neighbor in get_neighbors(pos):
            if is_valid(neighbor, grid, visited):
                new_dj = dj + (neighbor[0] != pos[0] and neighbor[1] != pos[1])  # Increment if diagonal
                queue.append((neighbor, path + [neighbor], new_dj))

grid = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0]
]

start, end = (10, 10), (0, 4)
path = bfs(start, end, grid)
print(path)
