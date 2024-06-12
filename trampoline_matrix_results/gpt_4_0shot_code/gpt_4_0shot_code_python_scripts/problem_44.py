
from collections import deque

# Define the trampoline park
park = [
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1]
]

# Define the starting and ending positions
start = (2, 1)
end = (10, 9)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue with the starting position
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next position from the queue
    (x, y), jumps, path = queue.popleft()

    # If this is the end position, print the path and break
    if (x, y) == end and jumps == 3:
        print(path)
        break

    # If we have made 3 jumps, continue without adding neighbors
    if jumps == 3:
        continue

    # Add the neighbors to the queue
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 11 and 0 <= ny < 11 and park[nx][ny] == 0:
            queue.append(((nx, ny), jumps + 1, path + [(nx, ny)]))
