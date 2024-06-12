
from collections import deque

# Define the trampoline park
park = [
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1]
]

# Define the starting and ending positions
start = (0, 11)
end = (12, 2)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the queue for the BFS
queue = deque([(start, [start], 0)])

while queue:
    # Pop the next position from the queue
    pos, path, diagonals = queue.popleft()

    # If we've reached the end, print the path and exit
    if pos == end and diagonals == 4:
        print(path)
        break

    # Otherwise, add all possible next positions to the queue
    for move in moves:
        next_pos = (pos[0] + move[0], pos[1] + move[1])
        if (0 <= next_pos[0] < 14 and 0 <= next_pos[1] < 14 and
            park[next_pos[0]][next_pos[1]] == 0 and
            next_pos not in path):
            next_diagonals = diagonals + 1 if move in moves[:4] else diagonals
            if next_diagonals <= 4:
                queue.append((next_pos, path + [next_pos], next_diagonals))
