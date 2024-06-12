
from collections import deque

def get_neighbors(pos, grid):
    neighbors = []
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors

def bfs(start, end, grid):
    queue = deque([start])
    prev = {start: None}
    while queue:
        pos = queue.popleft()
        if pos == end:
            path = []
            while pos is not None:
                path.append(pos)
                pos = prev[pos]
            return path[::-1]
        for neighbor in get_neighbors(pos, grid):
            if neighbor not in prev:
                queue.append(neighbor)
                prev[neighbor] = pos
    return None

grid = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1]
]

start, end = (9, 9), (0, 3)
path = bfs(start, end, grid)
print(path)
