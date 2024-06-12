
from collections import deque

# Define the map of the trampoline park
park = [
    [1, 0, 1, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1]
]

# Define the starting and ending positions
start = (0, 6)
end = (8, 2)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue with the starting position and 0 diagonal jumps
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next position from the queue
    (x, y), jumps, path = queue.popleft()

    # If we have reached the end and made exactly 3 diagonal jumps, print the path and exit
    if (x, y) == end and jumps == 3:
        print(path)
        break

    # Otherwise, for each possible move
    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        # If the new position is within the park, is not broken, and we have not made more than 3 diagonal jumps
        if 0 <= nx < 9 and 0 <= ny < 9 and park[nx][ny] == 0 and jumps < 3:
            # Add the new position to the queue with one more diagonal jump
            queue.append(((nx, ny), jumps + 1, path + [(nx, ny)]))
