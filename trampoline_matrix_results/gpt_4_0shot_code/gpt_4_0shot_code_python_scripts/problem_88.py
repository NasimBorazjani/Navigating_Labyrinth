
from collections import deque

# Define the map of the trampoline park
park_map = [
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1]
]

# Define the starting and ending positions
start = (0, 11)
end = (9, 1)

# Define the possible moves (8 directions)
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the queue for BFS
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next position from the queue
    (x, y), diagonal_jumps, path = queue.popleft()

    # If we have reached the end, print the path and break
    if (x, y) == end and diagonal_jumps == 4:
        print(path)
        break

    # Otherwise, add all possible next positions to the queue
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 14 and 0 <= ny < 14 and park_map[nx][ny] == 0:
            new_diagonal_jumps = diagonal_jumps
            if dx != 0 and dy != 0:
                new_diagonal_jumps += 1
            if new_diagonal_jumps <= 4:
                queue.append(((nx, ny), new_diagonal_jumps, path + [(nx, ny)]))
