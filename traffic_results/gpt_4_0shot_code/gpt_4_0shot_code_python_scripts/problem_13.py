
from collections import deque

def bfs(matrix, start, end):
    queue = deque([([start], 0)])
    visited = set([start])
    while queue:
        (path, length) = queue.popleft()
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
    ['x', 'x', 'x', 'x', 9, 'x', 20, 3, 9],
    [17, 11, 17, 'x', 9, 2, 7, 'x', 15],
    ['x', 4, 2, 19, 12, 6, 'x', 4, 17],
    [15, 'x', 'x', 15, 11, 19, 'x', 9, 5],
    [3, 9, 19, 15, 2, 'x', 'x', 18, 'x'],
    [19, 5, 9, 11, 9, 'x', 'x', 3, 'x'],
    ['x', 'x', 2, 8, 8, 'x', 'x', 'x', 19],
    ['x', 'x', 14, 'x', 'x', 'x', 18, 'x', 18],
    ['x', 14, 18, 7, 8, 'x', 10, 15, 'x']
]

start = (3, 7)
end = (5, 0)
print(bfs(matrix, start, end))
