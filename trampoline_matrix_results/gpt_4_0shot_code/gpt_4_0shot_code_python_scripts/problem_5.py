
from collections import deque

# Define the map of the trampoline park
park = [
    [0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1]
]

# Define the starting and ending positions
start = (0, 0)
end = (5, 7)

# Define the possible moves
moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

# Initialize the queue for the BFS
queue = deque([(start, 0, [start])])

while queue:
    # Get the current position, number of diagonal jumps, and path
    pos, jumps, path = queue.popleft()

    # If we have reached the destination with exactly 3 diagonal jumps, print the path and exit
    if pos == end and jumps == 3:
        print(path)
        break

    # Try all possible moves
    for move in moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])
        new_jumps = jumps + (move[0] != 0 and move[1] != 0)

        # If the new position is valid and we have not made more than 3 diagonal jumps, add it to the queue
        if (0 <= new_pos[0] < 9 and 0 <= new_pos[1] < 9 and park[new_pos[0]][new_pos[1]] == 0 and new_jumps <= 3):
            queue.append((new_pos, new_jumps, path + [new_pos]))
