
from collections import deque

# Grid map
grid = [
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
]

# Function to check if a position is valid
def is_valid(x, y, visited):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y] and grid[x][y] == 0

# Function to find the shortest path
def shortest_path(start, end):
    queue = deque([[start]])
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    visited[start[0]][start[1]] = True
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited):
                visited[nx][ny] = True
                queue.append(path + [(nx, ny)])

# Function to convert path to string representation
def path_to_string(path):
    return str(path).replace("),", "),\n").replace("),", ")  ").replace("]", "]  ")

# Start and end positions
start = (13, 1)
end = (4, 13)

# Find the shortest path
path = shortest_path(start, end)

# Print the path
print(path_to_string(path))
