
from collections import deque

# Define the grid with broken and functional trampolines
grid = [
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Define the starting and destination positions
start = (0, 9)
dest = (11, 2)

# Define the possible moves (8 adjacent trampolines)
moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

# Perform breadth-first search to find the shortest path
def bfs(start, dest):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()

        if current == dest and len(path) == 9:  # Check if destination is reached with exactly 4 diagonal jumps
            return path

        for move in moves:
            new_pos = (current[0] + move[0], current[1] + move[1])

            if 0 <= new_pos[0] < 12 and 0 <= new_pos[1] < 12 and grid[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited:
                queue.append((new_pos, path + [new_pos]))
                visited.add(new_pos)

    return None

# Find the shortest path
shortest_path = bfs(start, dest)

# Print the shortest path
print(shortest_path)
