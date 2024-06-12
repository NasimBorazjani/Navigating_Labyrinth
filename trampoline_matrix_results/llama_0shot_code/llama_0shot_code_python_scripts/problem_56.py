
from collections import deque

# Grid of the trampoline park
grid = [
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0]
]

def is_valid(x, y, dx, dy, grid):
    # Check if within grid
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return False
    # Check if it's a broken trampoline
    if grid[x][y] == 1:
        return False
    # Check if it's a diagonal move
    if dx != 0 and dy != 0:
        return True
    return False

def bfs(start, end, grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    queue = deque([(start, [start])])
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return queue.pop()[1]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, dx, dy, grid):
                queue.append(((nx, ny), queue[-1][1] + [(nx, ny)]))

start, end = (11, 7), (2, 0)
result = bfs(start, end, grid)
print(result)
