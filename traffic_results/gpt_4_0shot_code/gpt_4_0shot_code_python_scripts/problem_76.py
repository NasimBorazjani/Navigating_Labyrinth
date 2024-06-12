
from collections import deque

def bfs(matrix, start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        (x, y), path = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] != 'x' and (nx, ny) not in visited:
                if (nx, ny) == end:
                    return path + [(nx, ny)]
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    return None

matrix = [
    ['x', 12, 8, 4, 4, 16, 8, 'x', 'x', 17, 18, 9, 'x', 16],
    [2, 9, 'x', 1, 4, 13, 20, 11, 2, 'x', 11, 7, 14, 12],
    ['x', 'x', 'x', 'x', 17, 15, 8, 12, 'x', 'x', 7, 'x', 'x', 'x'],
    [2, 2, 'x', 5, 14, 'x', 1, 5, 4, 14, 7, 'x', 'x', 'x'],
    [19, 'x', 11, 1, 19, 19, 12, 'x', 12, 13, 5, 3, 17, 17],
    ['x', 'x', 'x', 'x', 'x', 1, 'x', 'x', 4, 'x', 'x', 'x', 8, 19],
    [6, 'x', 10, 'x', 7, 1, 11, 'x', 'x', 3, 'x', 3, 2, 'x'],
    [19, 'x', 3, 11, 'x', 6, 11, 'x', 12, 14, 10, 'x', 11, 18],
    [13, 'x', 'x', 'x', 'x', 'x', 4, 'x', 'x', 'x', 'x', 'x', 10, 5],
    [19, 'x', 'x', 16, 'x', 'x', 18, 'x', 8, 'x', 2, 11, 'x', 12],
    ['x', 14, 'x', 6, 'x', 18, 'x', 11, 'x', 'x', 14, 11, 2, 'x'],
    ['x', 'x', 6, 8, 10, 8, 14, 'x', 'x', 13, 'x', 10, 'x', 19],
    ['x', 19, 'x', 7, 12, 17, 'x', 15, 'x', 16, 19, 'x', 5, 'x'],
    [8, 'x', 17, 'x', 'x', 5, 15, 'x', 'x', 16, 1, 'x', 'x', 17]
]

start = (4, 3)
end = (8, 13)
print(bfs(matrix, start, end))
