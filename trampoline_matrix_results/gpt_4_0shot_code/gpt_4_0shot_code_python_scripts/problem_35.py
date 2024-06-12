
from collections import deque

# Trampoline park map
park = [
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1]
]

# Starting and destination positions
start = (1, 9)
end = (8, 0)

# BFS
queue = deque([(start, [start], 0)])
visited = set()
while queue:
    (x, y), path, jumps = queue.popleft()
    if (x, y) == end and jumps == 3:
        print(path)
        break
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 11 and 0 <= ny < 11 and park[nx][ny] == 0 and (nx, ny) not in visited:
            new_jumps = jumps
            if dx != 0 and dy != 0:
                new_jumps += 1
            if new_jumps <= 3:
                queue.append(((nx, ny), path + [(nx, ny)], new_jumps))
                visited.add((nx, ny))
