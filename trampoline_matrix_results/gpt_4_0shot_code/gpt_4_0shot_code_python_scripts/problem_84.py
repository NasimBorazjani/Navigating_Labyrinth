
from collections import deque

# Define the grid
grid = [
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1]
]

# Define the start and end points
start = (9, 0)
end = (3, 13)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the queue with the start point
queue = deque([(start, [start], 0)])

while queue:
    # Pop the next point from the queue
    (x, y), path, diag_count = queue.popleft()

    # If this point is the end point, print the path and exit
    if (x, y) == end and diag_count == 4:
        print(path)
        break

    # Add all possible next points to the queue
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if (0 <= nx < 14 and 0 <= ny < 14 and grid[nx][ny] == 0 and (nx, ny) not in path):
            new_diag_count = diag_count + 1 if dx != 0 and dy != 0 else diag_count
            if new_diag_count <= 4:
                queue.append(((nx, ny), path + [(nx, ny)], new_diag_count))
