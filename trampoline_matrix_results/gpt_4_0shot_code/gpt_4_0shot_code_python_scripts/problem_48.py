
from collections import deque

# Define the grid
grid = [
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0]
]

# Define the start and end points
start = (0, 9)
end = (10, 0)

# Define the possible moves
moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

# Initialize the queue with the start point and 0 diagonal jumps
queue = deque([(start, 0, [start])])

while queue:
    (x, y), diagonals, path = queue.popleft()
    if (x, y) == end and diagonals == 4:
        print(path)
        break
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 12 and 0 <= ny < 12 and grid[nx][ny] == 0:
            new_diagonals = diagonals
            if dx != 0 and dy != 0:
                new_diagonals += 1
            if new_diagonals <= 4:
                queue.append(((nx, ny), new_diagonals, path + [(nx, ny)]))
                grid[nx][ny] = 1  # Mark as visited
