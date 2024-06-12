
from collections import deque

def bfs(matrix, start, end):
    queue = deque([([start], 0)])
    visited = set([start])
    while queue:
        path, dist = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and
                matrix[nx][ny] != 'x' and (nx, ny) not in visited):
                queue.append((path + [(nx, ny)], dist + matrix[nx][ny]))
                visited.add((nx, ny))

matrix = [
    ['x', 'x', 12, 'x', 18, 3, 2, 15, 6, 11, 13, 'x', 7, 17, 'x'],
    [13, 'x', 20, 13, 5, 2, 'x', 'x', 10, 12, 19, 19, 16, 'x', 17],
    [12, 12, 7, 'x', 'x', 'x', 9, 'x', 'x', 10, 10, 18, 4, 'x', 'x'],
    ['x', 14, 3, 13, 9, 2, 19, 19, 'x', 'x', 'x', 4, 'x', 2, 15],
    ['x', 14, 2, 'x', 3, 'x', 10, 11, 'x', 4, 'x', 12, 4, 'x', 'x'],
    ['x', 9, 7, 16, 'x', 'x', 19, 17, 17, 14, 14, 12, 14, 19, 12],
    [2, 'x', 'x', 7, 15, 'x', 'x', 13, 'x', 8, 1, 1, 'x', 14, 19],
    [16, 'x', 14, 'x', 'x', 6, 'x', 'x', 16, 'x', 'x', 9, 10, 18, 4],
    [3, 'x', 'x', 3, 'x', 'x', 'x', 'x', 9, 8, 'x', 9, 14, 'x', 14],
    ['x', 'x', 'x', 4, 19, 'x', 4, 15, 'x', 'x', 'x', 17, 'x', 'x', 'x'],
    [16, 17, 'x', 'x', 13, 'x', 18, 5, 'x', 14, 'x', 'x', 'x', 'x', 'x'],
    [2, 'x', 17, 'x', 'x', 'x', 'x', 'x', 'x', 12, 3, 8, 'x', 2, 9],
    ['x', 'x', 14, 7, 11, 'x', 'x', 10, 9, 3, 7, 16, 'x', 7, 1],
    ['x', 12, 14, 1, 'x', 'x', 3, 12, 'x', 7, 'x', 'x', 8, 'x', 'x'],
    ['x', 2, 'x', 15, 2, 'x', 14, 16, 13, 19, 16, 1, 11, 'x', 'x']
]

start = (5, 2)
end = (8, 14)
print(bfs(matrix, start, end))
