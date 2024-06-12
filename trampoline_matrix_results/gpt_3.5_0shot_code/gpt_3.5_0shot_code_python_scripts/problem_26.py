
from collections import deque

# Define the grid map
grid = [
    [1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
]

# Define the starting and destination positions
start = (8, 6)
dest = (0, 1)

# Define the possible diagonal jumps
diagonal_jumps = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Perform breadth-first search
queue = deque([(start, [start])])
visited = set([start])

while queue:
    current, path = queue.popleft()

    if current == dest and len(path) == 4:
        print(path)
        break

    for dx, dy in diagonal_jumps:
        new_pos = (current[0] + dx, current[1] + dy)

        if 0 <= new_pos[0] < 10 and 0 <= new_pos[1] < 10 and grid[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited:
            queue.append((new_pos, path + [new_pos]))
            visited.add(new_pos)
