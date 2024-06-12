
from collections import deque

# Define the map of the trampoline park
park = [
    [0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 1, 1, 1]
]

# Define the starting and ending positions
start = (0, 0)
end = (7, 6)

# Define the eight possible directions to jump
directions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the queue for the BFS algorithm
queue = deque([(start, 0, [start])])

while queue:
    # Pop the next position from the queue
    (x, y), diagonal_jumps, path = queue.popleft()

    # If this is the end position and we've made exactly 3 diagonal jumps, print the path and exit
    if (x, y) == end and diagonal_jumps == 3:
        print(path)
        break

    # Otherwise, add all valid adjacent positions to the queue
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 10 and 0 <= ny < 10 and park[nx][ny] == 0:
            new_diagonal_jumps = diagonal_jumps + 1 if dx != 0 and dy != 0 else diagonal_jumps
            if new_diagonal_jumps <= 3:
                queue.append(((nx, ny), new_diagonal_jumps, path + [(nx, ny)]))
