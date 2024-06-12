
from collections import deque

# Define the trampoline park
park = [
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]

# Define the starting and ending positions
start = (7, 13)
end = (13, 0)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the queue with the starting position and 0 diagonal jumps
queue = deque([(start, 0)])

# While there are positions to explore
while queue:
    # Get the current position and number of diagonal jumps
    (x, y), jumps = queue.popleft()

    # If this is the end position and we have made exactly 4 diagonal jumps
    if (x, y) == end and jumps == 4:
        print((x, y))
        break

    # For each possible move
    for dx, dy in moves:
        # Calculate the new position
        nx, ny = x + dx, y + dy

        # If the new position is within the park and the trampoline is not broken
        if 0 <= nx < 14 and 0 <= ny < 14 and park[nx][ny] == 0:
            # Calculate the number of diagonal jumps
            njumps = jumps + 1 if dx != 0 and dy != 0 else jumps

            # If we have not made more than 4 diagonal jumps
            if njumps <= 4:
                # Add the new position to the queue
                queue.append(((nx, ny), njumps))

                # Mark the trampoline as broken so we don't visit it again
                park[nx][ny] = 1

                print((nx, ny))
