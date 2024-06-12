
from collections import deque

# Define the grid
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

# Define the start and end points
start = (10, 10)
end = (0, 4)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Define the BFS function
def bfs(start, end, grid):
    queue = deque([(start, 0, [start])])
    visited = set([start])
    while queue:
        (x, y), d, path = queue.popleft()
        if (x, y) == end and d == 3:
            return path
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append(((nx, ny), d + 1, path + [(nx, ny)]))
                visited.add((nx, ny))
    return None

# Print the shortest path
print(bfs(start, end, grid))
