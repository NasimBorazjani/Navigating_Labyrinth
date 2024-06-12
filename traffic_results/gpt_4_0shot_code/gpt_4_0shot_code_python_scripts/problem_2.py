
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
    ['x', 13, 9, 'x', 'x', 16, 6, 18, 7],
    ['x', 3, 11, 'x', 'x', 5, 7, 'x', 19],
    [8, 'x', 2, 5, 6, 12, 9, 10, 7],
    [12, 1, 6, 20, 19, 18, 12, 'x', 14],
    [16, 5, 10, 3, 'x', 'x', 'x', 1, 9],
    ['x', 3, 'x', 'x', 'x', 'x', 'x', 'x', 4],
    [7, 10, 'x', 1, 'x', 'x', 17, 'x', 8],
    ['x', 5, 'x', 'x', 'x', 17, 'x', 9, 'x'],
    [13, 16, 8, 15, 'x', 2, 'x', 1, 2]
]

start = (2, 2)
end = (5, 8)
print(bfs(matrix, start, end))
