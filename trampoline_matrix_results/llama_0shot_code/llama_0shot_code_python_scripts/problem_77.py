
from collections import deque

# Grid of the trampoline park
grid = [
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1]
]

# Function to check if a jump is valid
def is_valid(x, y, visited):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and not visited[x][y]

# Function to find the shortest path using BFS
def bfs(start, end):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    visited[start[0]][start[1]] = True
    queue = deque([(start, [])])
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path + [(x, y)]
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited):
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(x, y)]))

# Start and end positions
start = (0, 13)
end = (8, 1)

# Find the shortest path
path = bfs(start, end)

# Print the path
print(path)
