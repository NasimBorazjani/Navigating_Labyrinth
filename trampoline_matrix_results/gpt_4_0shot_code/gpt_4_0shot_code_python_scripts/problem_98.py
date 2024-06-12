
from collections import deque

# Define the trampoline park
park = [
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0]
]

# Define the starting and ending positions
start = (1, 2)
end = (12, 11)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue with the starting position
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next position from the queue
    (x, y), count, path = queue.popleft()

    # If this is the end position, print the path and exit
    if (x, y) == end and count == 5:
        print(path)
        break

    # Add all possible next positions to the queue
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 15 and 0 <= ny < 15 and park[nx][ny] == 0:
            queue.append(((nx, ny), count + 1, path + [(nx, ny)]))
