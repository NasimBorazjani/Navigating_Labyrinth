
from collections import deque

# Define the trampoline park
park = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1]
]

# Define the starting and ending positions
start = (11, 9)
end = (0, 3)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Perform a breadth-first search
queue = deque([(start, 0, [start])])
visited = set()
while queue:
    (x, y), count, path = queue.popleft()
    if (x, y) == end and count == 4:
        print(path)
        break
    if (x, y) not in visited or visited[(x, y)] > count:
        visited[(x, y)] = count
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 12 and 0 <= ny < 12 and park[nx][ny] == 0:
                queue.append(((nx, ny), count + 1, path + [(nx, ny)]))
