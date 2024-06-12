
from collections import deque

# Define the map of the trampoline park
park = [
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1]
]

# Define the starting and ending positions
start = (0, 9)
end = (9, 2)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Initialize the queue for the BFS
queue = deque([(start, 0, [start])])

while queue:
    # Get the current position, number of jumps, and path
    pos, jumps, path = queue.popleft()

    # If we have reached the end, print the path and break
    if pos == end and jumps == 3:
        print(path)
        break

    # If we have made too many jumps, continue
    if jumps > 3:
        continue

    # Try all possible moves
    for move in moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])

        # If the new position is valid, add it to the queue
        if 0 <= new_pos[0] < 11 and 0 <= new_pos[1] < 11 and park[new_pos[0]][new_pos[1]] == 0:
            queue.append((new_pos, jumps + 1, path + [new_pos]))
