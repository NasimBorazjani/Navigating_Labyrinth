
from collections import deque

# Define the grid map
grid = [
    [1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1]
]

# Define the starting and destination positions
start = (0, 9)
dest = (6, 0)

# Define the possible diagonal jumps
diagonal_jumps = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Perform breadth-first search to find the shortest path
def bfs(start, dest):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()

        if current == dest and len(path) == 4:
            return path

        for dx, dy in diagonal_jumps:
            new_pos = (current[0] + dx, current[1] + dy)

            if 0 <= new_pos[0] < 11 and 0 <= new_pos[1] < 11 and grid[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited:
                queue.append((new_pos, path + [new_pos]))
                visited.add(new_pos)

    return None

# Find the shortest path
shortest_path = bfs(start, dest)

# Print the shortest path
print(shortest_path)
