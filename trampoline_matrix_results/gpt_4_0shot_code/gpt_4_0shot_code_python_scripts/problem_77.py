
from collections import deque

# Define the grid
grid = [
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1]
]

# Define the start and end points
start = (0, 13)
end = (8, 1)

# Define the possible moves
moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

# Initialize the queue with the start point
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next point from the queue
    (x, y), diagonal_jumps, path = queue.popleft()

    # If this is the end point, print the path and break
    if (x, y) == end and diagonal_jumps == 4:
        print(path)
        break

    # Add all possible next points to the queue
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 14 and 0 <= ny < 14 and grid[nx][ny] == 0:
            new_diagonal_jumps = diagonal_jumps
            if dx != 0 and dy != 0:
                new_diagonal_jumps += 1
            if new_diagonal_jumps <= 4:
                queue.append(((nx, ny), new_diagonal_jumps, path + [(nx, ny)]))
                grid[nx][ny] = 1  # Mark as visited
