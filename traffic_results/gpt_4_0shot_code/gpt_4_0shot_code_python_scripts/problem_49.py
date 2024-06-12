
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
    ['x', 'x', 13, 9, 'x', 15, 'x', 'x', 2, 13, 9, 11],
    [8, 'x', 4, 5, 13, 'x', 'x', 7, 16, 'x', 15, 13],
    ['x', 'x', 'x', 'x', 3, 'x', 4, 3, 18, 'x', 11, 18],
    [6, 'x', 14, 5, 16, 'x', 11, 'x', 3, 16, 3, 3],
    [15, 12, 'x', 'x', 10, 3, 2, 14, 'x', 18, 'x', 'x'],
    [11, 1, 2, 1, 17, 15, 'x', 2, 'x', 12, 'x', 'x'],
    ['x', 'x', 3, 15, 16, 1, 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 10, 'x', 'x', 'x', 6, 1, 8, 19, 13, 7, 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 3],
    [3, 7, 12, 'x', 15, 'x', 19, 13, 17, 14, 'x', 'x'],
    ['x', 'x', 'x', 'x', 4, 4, 18, 'x', 5, 'x', 'x', 10],
    ['x', 'x', 15, 9, 13, 10, 8, 4, 8, 6, 7, 7]
]

start = (3, 11)
end = (4, 0)
print(bfs(matrix, start, end))
