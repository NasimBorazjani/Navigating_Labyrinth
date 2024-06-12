
from collections import deque

# Grid of the trampoline park
grid = [
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1]
]

# Function to check if a position is valid
def is_valid(x, y, visited):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and not visited[x][y]

# BFS to find the shortest path
def bfs(start, end):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    visited[start[0]][start[1]] = True
    queue = deque([(start, 0, [start])])  # (position, diagonal_jumps, path)
    while queue:
        x, y, d, path = queue.popleft()
        if (x, y) == end and d == 3:
            return path
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Diagonal movements
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited):
                visited[nx][ny] = True
                queue.append(((nx, ny), d+1, path + [(nx, ny)]))

# Call BFS and print the result
start, end = (0, 0), (7, 6)
path = bfs(start, end)
print(path)
