
from collections import deque

def bfs(start, end, park):
    queue = deque([(start, 0, [])])
    visited = set()
    while queue:
        (x, y), jumps, path = queue.popleft()
        if (x, y) == end and jumps == 3:
            return path + [(x, y)]
        if (x, y) in visited or jumps > 3:
            continue
        visited.add((x, y))
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 11 and 0 <= ny < 11 and park[nx][ny] == 0:
                queue.append(((nx, ny), jumps + 1, path + [(x, y)]))
    return None

park = [
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]

start = (10, 9)
end = (3, 1)
print(bfs(start, end, park))
