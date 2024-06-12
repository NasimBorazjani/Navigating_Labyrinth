
from collections import deque

def bfs(matrix, start, end):
    queue = deque([([start], 0)])
    visited = set([start])
    while queue:
        path, length = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and
                matrix[nx][ny] != 'x' and (nx, ny) not in visited):
                queue.append((path + [(nx, ny)], length + matrix[nx][ny]))
                visited.add((nx, ny))

matrix = [
    [10, 'x', 'x', 1, 1, 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    [11, 9, 17, 'x', 14, 3, 'x', 13, 'x', 'x', 6, 'x'],
    ['x', 5, 'x', 'x', 10, 13, 13, 19, 10, 'x', 1, 12],
    [6, 'x', 'x', 17, 5, 6, 17, 4, 5, 'x', 1, 'x'],
    [4, 11, 1, 'x', 'x', 'x', 14, 7, 19, 4, 'x', 6],
    ['x', 'x', 6, 18, 'x', 'x', 'x', 5, 8, 2, 1, 'x'],
    [19, 19, 10, 9, 19, 19, 'x', 6, 'x', 1, 14, 11],
    ['x', 'x', 'x', 18, 11, 'x', 7, 5, 15, 13, 1, 11],
    ['x', 4, 'x', 8, 'x', 11, 'x', 'x', 9, 'x', 'x', 15],
    [10, 8, 10, 2, 'x', 'x', 'x', 'x', 'x', 12, 'x', 17],
    [19, 'x', 3, 11, 'x', 'x', 9, 3, 15, 'x', 5, 17],
    [18, 'x', 'x', 'x', 11, 14, 'x', 14, 13, 'x', 'x', 8]
]

start = (3, 3)
end = (8, 11)
print(bfs(matrix, start, end))
