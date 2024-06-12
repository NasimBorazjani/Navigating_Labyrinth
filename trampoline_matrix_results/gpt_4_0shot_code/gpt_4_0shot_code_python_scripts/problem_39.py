
from collections import deque

# Define the trampoline park
park = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1]
]

# Define the starting and ending positions
start = (9, 9)
end = (0, 3)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Perform a breadth-first search
queue = deque([(start, 0, [start])])
visited = set()
while queue:
    (x, y), jumps, path = queue.popleft()
    if (x, y) == end and jumps == 3:
        print(path)
        break
    if (x, y) in visited or jumps > 3:
        continue
    visited.add((x, y))
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 11 and 0 <= ny < 11 and park[nx][ny] == 0:
            queue.append(((nx, ny), jumps + 1, path + [(nx, ny)]))
