
from collections import deque

# Define the grid
grid = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0]
]

# Define the start and end points
start = (8, 8)
end = (0, 0)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue with the start point
queue = deque([(start, [start])])

while queue:
    # Pop the next node from the queue
    node, path = queue.popleft()

    # If this node is the end point, print the path and exit
    if node == end:
        print(path)
        break

    # Add all reachable nodes to the queue
    for dx, dy in moves:
        x, y = node
        nx, ny = x + dx, y + dy
        if 0 <= nx < 11 and 0 <= ny < 11 and grid[nx][ny] == 0 and (nx, ny) not in path:
            queue.append(((nx, ny), path + [(nx, ny)]))
