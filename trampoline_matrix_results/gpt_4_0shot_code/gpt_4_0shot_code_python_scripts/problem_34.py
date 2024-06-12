
from collections import deque

# Define the grid
grid = [
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Define the start and end points
start = (10, 10)
end = (5, 0)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the queue with the start point
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next point from the queue
    (x, y), diagonal_jumps, path = queue.popleft()

    # If this is the end point, print the path and exit
    if (x, y) == end and diagonal_jumps == 3:
        print(path)
        break

    # Add all possible next points to the queue
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 11 and 0 <= ny < 11 and grid[nx][ny] == 0:
            new_diagonal_jumps = diagonal_jumps + 1 if dx != 0 and dy != 0 else diagonal_jumps
            if new_diagonal_jumps <= 3:
                queue.append(((nx, ny), new_diagonal_jumps, path + [(nx, ny)]))
