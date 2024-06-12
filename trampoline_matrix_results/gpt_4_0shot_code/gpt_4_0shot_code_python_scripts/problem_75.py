
from collections import deque

# Define the grid
grid = [
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1]
]

# Define the start and end points
start = (0, 7)
end = (12, 0)

# Define the possible moves
moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

# Initialize the queue with the start point
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next point from the queue
    (x, y), diagonal_jumps, path = queue.popleft()

    # If this is the end point and we've made exactly 4 diagonal jumps, print the path and exit
    if (x, y) == end and diagonal_jumps == 4:
        print(path)
        break

    # Otherwise, add all possible next moves to the queue
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 13 and 0 <= ny < 13 and grid[nx][ny] == 0:
            new_diagonal_jumps = diagonal_jumps
            if dx != 0 and dy != 0:
                new_diagonal_jumps += 1
            if new_diagonal_jumps <= 4:
                queue.append(((nx, ny), new_diagonal_jumps, path + [(nx, ny)]))
                grid[nx][ny] = 1  # Mark this point as visited
