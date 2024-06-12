
from collections import deque

# Define the trampoline park
park = [
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1]
]

# Define the starting and ending positions
start = (12, 9)
end = (3, 1)

# Define the possible moves (including diagonal ones)
moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

# Initialize the queue with the starting position and 0 diagonal jumps
queue = deque([(start, 0, [start])])

# While there are positions to check
while queue:
    # Get the current position and number of diagonal jumps
    (x, y), jumps, path = queue.popleft()

    # If we have reached the end and made exactly 4 diagonal jumps
    if (x, y) == end and jumps == 4:
        # Print the path and stop the search
        print(path)
        break

    # For each possible move
    for dx, dy in moves:
        # Calculate the new position
        nx, ny = x + dx, y + dy

        # If the new position is inside the park and the trampoline is not broken
        if 0 <= nx < 13 and 0 <= ny < 13 and park[nx][ny] == 0:
            # Calculate the new number of diagonal jumps
            new_jumps = jumps + 1 if dx != 0 and dy != 0 else jumps

            # If we have not made more than 4 diagonal jumps
            if new_jumps <= 4:
                # Add the new position to the queue
                queue.append(((nx, ny), new_jumps, path + [(nx, ny)]))

                # Mark the trampoline as broken so we don't visit it again
                park[nx][ny] = 1
