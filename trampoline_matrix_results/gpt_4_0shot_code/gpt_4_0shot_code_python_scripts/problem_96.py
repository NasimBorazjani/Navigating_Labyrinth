
from collections import deque

# Define the trampoline park
park = [
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
]

# Define the starting and ending points
start = (3, 10)
end = (13, 0)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

# Perform a breadth-first search
queue = deque([(start, [start])])
while queue:
    (x, y), path = queue.popleft()
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 15 and 0 <= ny < 15 and park[nx][ny] == 0 and (nx, ny) not in path:
            if (nx, ny) == end and len(path) == 5:
                print(path + [(nx, ny)])
                break
            queue.append(((nx, ny), path + [(nx, ny)]))
