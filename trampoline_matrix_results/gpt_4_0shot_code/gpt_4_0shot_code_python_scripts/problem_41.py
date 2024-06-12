
from collections import deque

# Trampoline park map
park = [
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1]
]

# Starting and destination positions
start = (10, 0)
end = (2, 7)

# BFS
queue = deque([(start, 0, [start])])
visited = set()
while queue:
    (x, y), jumps, path = queue.popleft()
    if (x, y) == end and jumps == 3:
        print(path)
        break
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 11 and 0 <= ny < 11 and park[nx][ny] == 0 and (nx, ny) not in visited:
            visited.add((nx, ny))
            new_jumps = jumps + 1 if dx != 0 and dy != 0 else jumps
            if new_jumps <= 3:
                queue.append(((nx, ny), new_jumps, path + [(nx, ny)]))
