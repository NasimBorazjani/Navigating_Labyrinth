
from collections import deque

# Define the map of the trampoline park
park = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
]

# Define the starting and ending positions
start = (0, 9)
end = (7, 3)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the queue for the BFS
queue = deque([(start, 0, [start])])

while queue:
    # Get the current position, number of diagonal jumps, and path
    (x, y), jumps, path = queue.popleft()

    # If we have reached the destination with exactly 3 diagonal jumps, print the path and exit
    if (x, y) == end and jumps == 3:
        print(path)
        break

    # Try all possible moves
    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        # Check if the new position is valid
        if 0 <= nx < 10 and 0 <= ny < 10 and park[nx][ny] == 0:
            # Count the diagonal jumps
            new_jumps = jumps + 1 if dx != 0 and dy != 0 else jumps

            # If we have not made more than 3 diagonal jumps, add the new position to the queue
            if new_jumps <= 3:
                queue.append(((nx, ny), new_jumps, path + [(nx, ny)]))
