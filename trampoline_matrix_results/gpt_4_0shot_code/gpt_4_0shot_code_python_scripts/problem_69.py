
from collections import deque

# Define the grid
grid = [
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]
]

# Define the start and end points
start = (12, 0)
end = (3, 8)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the queue with the start point
queue = deque([(start, 0, [start])])

while queue:
    (x, y), diagonal_jumps, path = queue.popleft()
    if (x, y) == end and diagonal_jumps == 4:
        print(path)
        break
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 13 and 0 <= ny < 13 and grid[nx][ny] == 0 and (nx, ny) not in path:
            new_diagonal_jumps = diagonal_jumps + 1 if dx != 0 and dy != 0 else diagonal_jumps
            if new_diagonal_jumps <= 4:
                queue.append(((nx, ny), new_diagonal_jumps, path + [(nx, ny)]))