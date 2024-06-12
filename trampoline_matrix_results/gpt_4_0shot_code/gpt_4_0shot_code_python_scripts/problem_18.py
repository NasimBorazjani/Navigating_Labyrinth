
from collections import deque

# Define the map of the trampoline park
park = [
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
]

# Define the starting and ending positions
start = (8, 2)
end = (1, 8)

# Define the possible moves (diagonal only)
moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# Initialize the queue for the BFS
queue = deque([(start, [start])])

while queue:
    # Get the current position and path
    (x, y), path = queue.popleft()

    # Check if we have reached the end
    if (x, y) == end and len(path) == 4:
        print(path)
        break

    # Check all possible moves
    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        # Check if the new position is valid
        if 0 <= nx < 10 and 0 <= ny < 10 and park[nx][ny] == 0 and (nx, ny) not in path:
            queue.append(((nx, ny), path + [(nx, ny)]))
