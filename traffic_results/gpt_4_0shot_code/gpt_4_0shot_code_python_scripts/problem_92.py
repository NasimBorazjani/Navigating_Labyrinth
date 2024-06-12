
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
    [15, 1, 'x', 3, 'x', 9, 15, 8, 17, 'x', 'x', 6, 'x', 12, 3],
    ['x', 'x', 'x', 14, 'x', 7, 18, 6, 14, 2, 19, 15, 'x', 'x', 'x'],
    [4, 3, 'x', 10, 8, 4, 16, 13, 6, 'x', 18, 10, 14, 'x', 'x'],
    ['x', 'x', 'x', 10, 'x', 14, 10, 7, 'x', 'x', 'x', 4, 2, 19, 3],
    [5, 'x', 10, 'x', 18, 12, 20, 15, 'x', 'x', 11, 11, 1, 10, 19],
    [8, 'x', 13, 'x', 'x', 'x', 16, 7, 3, 'x', 'x', 2, 18, 11, 'x'],
    [12, 'x', 15, 'x', 'x', 6, 'x', 'x', 'x', 'x', 18, 3, 14, 3, 6],
    ['x', 6, 13, 19, 19, 'x', 7, 12, 18, 5, 'x', 1, 4, 18, 11],
    [5, 'x', 18, 'x', 12, 4, 3, 7, 'x', 16, 1, 'x', 16, 2, 'x'],
    ['x', 'x', 'x', 'x', 18, 'x', 'x', 14, 15, 1, 'x', 'x', 9, 'x', 'x'],
    ['x', 13, 'x', 7, 7, 'x', 'x', 16, 10, 'x', 'x', 'x', 'x', 8, 'x'],
    ['x', 'x', 19, 18, 8, 18, 'x', 'x', 12, 'x', 13, 'x', 17, 12, 7],
    ['x', 'x', 'x', 'x', 7, 7, 13, 17, 'x', 'x', 'x', 'x', 'x', 9, 5],
    [9, 'x', 14, 'x', 9, 'x', 8, 'x', 'x', 'x', 17, 4, 12, 12, 12],
    [8, 1, 11, 'x', 'x', 'x', 'x', 'x', 15, 'x', 'x', 2, 16, 'x', 15]
]

start = (7, 14)
end = (2, 4)
print(bfs(matrix, start, end))
