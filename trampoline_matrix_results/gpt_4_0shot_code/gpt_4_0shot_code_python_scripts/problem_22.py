
from collections import deque

# Define the map
trampoline_map = [
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0]
]

# Define the starting and ending points
start = (8, 1)
end = (1, 9)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue with the starting point
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next point from the queue
    (x, y), jumps, path = queue.popleft()

    # If this is the end point, print the path and break
    if (x, y) == end and jumps == 3:
        print(path)
        break

    # If we have made 3 jumps, continue to the next point
    if jumps == 3:
        continue

    # Add all possible moves to the queue
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 10 and 0 <= ny < 10 and trampoline_map[nx][ny] == 0:
            queue.append(((nx, ny), jumps + 1, path + [(nx, ny)]))
