
from collections import deque

# Define the grid with broken and functional trampolines
grid = [
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1]
]

# Define the starting and destination positions
start = (13, 3)
dest = (6, 12)

# Define the possible moves (8 directions)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

# Perform BFS to find the shortest path
def bfs(grid, start, dest):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()

        if current == dest:
            return path

        for dx, dy in directions:
            new_x, new_y = current[0] + dx, current[1] + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append(((new_x, new_y), path + [(new_x, new_y)]))

    return None

# Find the shortest path
shortest_path = bfs(grid, start, dest)
print(shortest_path)
