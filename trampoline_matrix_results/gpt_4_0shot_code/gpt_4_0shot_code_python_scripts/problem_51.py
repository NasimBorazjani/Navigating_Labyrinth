
from collections import deque

# Trampoline park map
park = [
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
]

# Starting and destination positions
start = (1, 11)
end = (11, 3)

# Directions for diagonal jumps
directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# BFS
queue = deque([(start, 0, [start])])
visited = set()
while queue:
    (x, y), jumps, path = queue.popleft()
    if (x, y) == end and jumps == 4:
        print(path)
        break
    if (x, y) not in visited or visited[(x, y)] > jumps:
        visited[(x, y)] = jumps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 12 and 0 <= ny < 12 and park[nx][ny] == 0:
                queue.append(((nx, ny), jumps + 1, path + [(nx, ny)]))
