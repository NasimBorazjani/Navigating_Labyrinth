
from collections import deque

# Define the map of the trampoline park
park = [
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 1]
]

# Define the starting and ending positions
start = (0, 1)
end = (6, 9)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the queue for the BFS
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next position from the queue
    pos, jumps, path = queue.popleft()

    # If we've reached the end, print the path and break
    if pos == end and jumps == 3:
        print(path)
        break

    # Otherwise, add all possible next positions to the queue
    for move in moves:
        next_pos = (pos[0] + move[0], pos[1] + move[1])
        next_jumps = jumps + (move[0] != 0 and move[1] != 0)
        if (0 <= next_pos[0] < 10 and 0 <= next_pos[1] < 10 and
            park[next_pos[0]][next_pos[1]] == 0 and next_jumps <= 3):
            queue.append((next_pos, next_jumps, path + [next_pos]))
