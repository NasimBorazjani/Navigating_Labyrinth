
from collections import deque

# Define the grid map
grid = [
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1]
]

# Define the starting and destination positions
start = (0, 3)
dest = (14, 11)

# Define the possible moves (8 directions)
moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

# Perform breadth-first search
def bfs():
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()

        if current == dest and len(path) == 16:
            return path

        for move in moves:
            new_pos = (current[0] + move[0], current[1] + move[1])

            if 0 <= new_pos[0] < 15 and 0 <= new_pos[1] < 15 and grid[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited:
                new_path = path + [new_pos]
                queue.append((new_pos, new_path))
                visited.add(new_pos)

    return None

# Find the shortest path
shortest_path = bfs()

# Print the shortest path
print(shortest_path)
