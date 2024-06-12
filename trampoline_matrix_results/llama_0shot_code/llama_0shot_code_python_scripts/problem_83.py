
from collections import deque

def is_valid(x, y, visited, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y] and grid[x][y] == 0

def BFS(start, destination, grid):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    visited[start[0]][start[1]] = True
    queue = deque([(start, [start])])
    while queue:
        x, y = pos := queue.popleft()
        if pos == destination:
            return path[::-1]
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            for _ in range(2):
                nx, ny = x + 2*dx, y + 2*dy
                if is_valid(nx, ny, visited, grid):
                    visited[nx][ny] = True
                    queue.append(((nx, ny), path + [(nx, ny)]))
                dx, dy = dy, -dx
    return None

grid = [
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    # ...
    [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1]
]

start, destination = (13, 10), (4, 0)
result = BFS(start, destination, grid)
print(result)
