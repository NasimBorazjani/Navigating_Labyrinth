
from collections import deque

# Define the grid
grid = [
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]
]

# Define the start and end points
start = (14, 13)
end = (2, 5)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Define the BFS function
def bfs(start, end):
    queue = deque([(start, 0, [start])])
    visited = set([start])
    while queue:
        (x, y), d, path = queue.popleft()
        if (x, y) == end and d == 5:
            return path
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 15 and 0 <= ny < 15 and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), d + (dx != 0 and dy != 0), path + [(nx, ny)]))
    return None

# Print the shortest path
print(bfs(start, end))
