
from collections import deque

# Define the trampoline park
park = [
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]
]

# Define the starting and ending positions
start = (11, 3)
end = (1, 10)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue with the starting position
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next node from the queue
    (x, y), count, path = queue.popleft()

    # If we have reached the end, print the path and break
    if (x, y) == end and count == 4:
        print(path)
        break

    # If we have made 4 jumps but have not reached the end, continue
    if count == 4:
        continue

    # Add the reachable nodes to the queue
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 13 and 0 <= ny < 13 and park[nx][ny] == 0:
            queue.append(((nx, ny), count + 1, path + [(nx, ny)]))
