
from collections import deque

# Define the map of the trampoline park
park = [
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0]
]

# Define the starting and ending positions
start = (7, 9)
end = (3, 0)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the queue for the BFS
queue = deque([(start, 0, [start])])

while queue:
    # Get the current position, number of diagonal jumps, and path
    (x, y), jumps, path = queue.popleft()

    # If we have reached the end, print the path and stop
    if (x, y) == end and jumps == 3:
        print(path)
        break

    # Try all possible moves
    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        # Check if the new position is valid
        if 0 <= nx < 10 and 0 <= ny < 10 and park[nx][ny] == 0:
            # Check if the move is diagonal
            if dx != 0 and dy != 0:
                # If we have already made 3 diagonal jumps, skip this move
                if jumps == 3:
                    continue
                else:
                    queue.append(((nx, ny), jumps + 1, path + [(nx, ny)]))
            else:
                queue.append(((nx, ny), jumps, path + [(nx, ny)]))
