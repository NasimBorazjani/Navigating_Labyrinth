
from collections import deque

def bfs(matrix, start, end):
    queue = deque([([start], 0)])
    seen = {start}
    while queue:
        (path, length), *queue = queue
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and
                matrix[nx][ny] != 'x' and (nx, ny) not in seen):
                queue.append((path + [(nx, ny)], length + matrix[nx][ny]))
                seen.add((nx, ny))

matrix = [
    [13, 'x', 'x', 'x', 'x', 'x', 8, 'x', 'x', 6],
    ['x', 'x', 'x', 8, 10, 'x', 17, 'x', 15, 14],
    ['x', 6, 'x', 'x', 'x', 16, 12, 7, 8, 11],
    ['x', 15, 'x', 1, 11, 19, 9, 17, 'x', 'x'],
    [18, 20, 16, 19, 12, 1, 'x', 'x', 'x', 5],
    [11, 'x', 18, 14, 'x', 2, 'x', 9, 8, 1],
    ['x', 2, 5, 16, 3, 9, 2, 18, 'x', 'x'],
    ['x', 8, 15, 17, 16, 6, 'x', 3, 'x', 10],
    [3, 'x', 'x', 'x', 8, 9, 10, 'x', 6, 'x'],
    [6, 'x', 9, 16, 1, 3, 16, 18, 'x', 'x']
]

start = (1, 8)
end = (4, 1)
print(bfs(matrix, start, end))
