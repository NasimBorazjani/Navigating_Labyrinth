
from collections import deque

def get_neighbors(grid, row, col, visited):
    neighbors = []
    for r, c in ((row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1)):
        if 0 <= r < len(grid) and 0 <= c < len(grid) and grid[r][c] == 0 and (r, c) != (row, col) and (r, c) not in visited:
            neighbors.append((r, c))
    return neighbors

def is_valid(src, dest):
    dr, dc = dest[0]-src[0], dest[1]-src[1]
    return abs(dr) == abs(dc) and max(abs(dr), abs(dc)) - min(abs(dr), abs(dc)) == 3

def bfs(grid, src, dest):
    visited = set()
    queue = deque([(src, [src])])
    while queue:
        (pos, path) = queue.popleft()
        if pos == dest:
            return path
        visited.add(pos)
        for neighbor in get_neighbors(grid, pos[0], pos[1], visited):
            if is_valid(pos, neighbor):
                queue.append((neighbor, path + [neighbor]))

grid = [[1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 1, 1, 0]]

src, dest = (8, 1), (1, 9)
path = bfs(grid, src, dest)
print(path)
