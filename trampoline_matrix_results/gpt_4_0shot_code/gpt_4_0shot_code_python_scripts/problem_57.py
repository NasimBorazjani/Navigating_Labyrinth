
from collections import deque

# Define the grid
grid = [
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0]
]

# Define the start and end points
start = (11, 2)
end = (3, 10)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Define the BFS function
def bfs(start, end):
    queue = deque([(start, 0, [start])])
    visited = set([start])
    while queue:
        (x, y), step, path = queue.popleft()
        if (x, y) == end and step == 4:
            return path
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 12 and 0 <= ny < 12 and grid[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append(((nx, ny), step + 1, path + [(nx, ny)]))
                visited.add((nx, ny))
    return None

# Print the shortest path
print(bfs(start, end))
