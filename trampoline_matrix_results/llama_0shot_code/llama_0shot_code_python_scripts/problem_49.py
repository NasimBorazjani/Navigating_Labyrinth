
from collections import deque

def get_neighbors(pos, grid):
    x, y = pos
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
    valid_neighbors = []
    for n in neighbors:
        if 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0]) and grid[n[0]][n[1]] == 0 and n != pos:
            valid_neighbors.append(n)
    return valid_neighbors

def bfs(start, end, grid):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        pos, path = queue.popleft()
        if pos == end:
            return path
        for n in get_neighbors(pos, grid):
            if n not in visited:
                visited.add(n)
                queue.append((n, path + [n]))

grid = [
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
]

start = (6, 11)
end = (0, 0)
path = bfs(start, end, grid)
print(path)
