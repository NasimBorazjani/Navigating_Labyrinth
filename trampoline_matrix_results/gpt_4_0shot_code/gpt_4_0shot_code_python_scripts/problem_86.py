
from collections import deque

# Define the map of the trampoline park
park = [
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0],
    [1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
]

# Define the starting and ending positions
start = (0, 4)
end = (13, 12)

# Define the possible moves (up, down, left, right, and the four diagonals)
moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue for the BFS algorithm
queue = deque([(start, [start])])

while queue:
    # Get the current position and path
    (x, y), path = queue.popleft()

    # Check if we have reached the end
    if (x, y) == end:
        print(path)
        break

    # Check all possible moves
    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        # Check if the new position is inside the park and the trampoline is not broken
        if 0 <= nx < 14 and 0 <= ny < 14 and park[nx][ny] == 0 and (nx, ny) not in path:
            # Add the new position to the queue
            queue.append(((nx, ny), path + [(nx, ny)]))
