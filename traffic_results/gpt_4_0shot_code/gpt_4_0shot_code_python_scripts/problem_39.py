
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
    [15, 8, 18, 3, 19, 'x', 17, 'x', 'x', 'x', 'x'],
    [19, 16, 'x', 18, 20, 2, 5, 7, 11, 12, 3],
    [18, 'x', 18, 1, 2, 'x', 'x', 'x', 12, 16, 4],
    [9, 20, 4, 19, 5, 15, 'x', 'x', 'x', 6, 4],
    ['x', 18, 8, 1, 'x', 7, 1, 7, 10, 1, 4],
    ['x', 18, 'x', 18, 19, 9, 18, 5, 15, 1, 7],
    [3, 'x', 12, 14, 'x', 'x', 'x', 'x', 1, 'x', 'x'],
    ['x', 12, 6, 'x', 6, 'x', 1, 'x', 1, 7, 'x'],
    ['x', 5, 10, 14, 2, 'x', 'x', 7, 11, 3, 'x'],
    [6, 9, 13, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 3],
    [19, 12, 'x', 15, 'x', 14, 'x', 9, 'x', 'x', 19]
]

start = (3, 1)
end = (5, 10)
print(bfs(matrix, start, end))
