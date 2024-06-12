
from collections import deque

map = [
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0]
]

def is_valid(x, y, visited, diagonal_jumps):
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
        return False
    if map[x][y] == 1:
        return False
    if (x != 1 or y != 7) and (x, y) in visited:
        return False
    if (x, y) == (1, 7):
        return True
    if (x, y) == (10, 0):
        return diagonal_jumps == 4
    return True

def bfs(start, end, diagonal_jumps):
    queue = deque([(start, [start], 0)])
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return [tuple(i) for i in queue.popleft()[1]]
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, queue[0][1], diagonal_jumps):
                queue.append(((nx, ny), queue[0][1] + [(nx, ny)], diagonal_jumps + 1))
    return []

print(bfs((1, 7), (10, 0), 0))
