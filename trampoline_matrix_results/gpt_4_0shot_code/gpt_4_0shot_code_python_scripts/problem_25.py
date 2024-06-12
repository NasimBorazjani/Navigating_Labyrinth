
from collections import deque

# Define the map of the trampoline park
park = [
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1]
]

# Define the starting and ending positions
start = (0, 0)
end = (7, 6)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue for the BFS
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next position from the queue
    (x, y), jumps, path = queue.popleft()

    # If this is the end position, return the path
    if (x, y) == end and jumps == 3:
        print(path)
        break

    # If we have not made 3 jumps yet, try jumping to a new position
    if jumps < 3:
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and park[nx][ny] == 0:
                queue.append(((nx, ny), jumps + 1, path + [(nx, ny)]))
