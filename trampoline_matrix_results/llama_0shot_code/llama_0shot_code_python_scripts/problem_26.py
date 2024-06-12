
from collections import deque

def get_neighbors(r, c):
    return [(r-1, c-2), (r-1, c+2), (r+1, c-2), (r+1, c+2), (r-2, c-1), (r-2, c+1), (r+2, c-1), (r+2, c+1)]

def is_valid(r, c, grid, visited):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
        return False
    if grid[r][c] == 1:
        return False
    if visited[r][c]:
        return False
    return True

def find_path(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([((8, 6), [(8, 6)])])
    visited = [[False]*cols for _ in range(rows)]
    destination = (0, 1)

    while queue:
        current_position, path = queue.popleft()
        r, c = current_position
        if current_position == destination:
            if len(path) == 4:  # 1 initial position + 3 jumps
                return path
        for nr, nc in get_neighbors(r, c):
            if is_valid(nr, nc, grid, visited):
                visited[nr][nc] = True
                new_path = list(path)
                new_path.append((nr, nc))
                queue.append(((nr, nc), new_path))

    return "No valid path found"

grid = [
    [1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
]

print(find_path(grid))
