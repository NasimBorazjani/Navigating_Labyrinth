
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
    [18, 19, 9, 'x', 'x', 'x', 3, 'x', 8, 'x'],
    [13, 2, 3, 15, 3, 'x', 8, 9, 'x', 'x'],
    ['x', 6, 18, 1, 20, 7, 16, 8, 1, 19],
    ['x', 'x', 'x', 20, 14, 'x', 19, 11, 9, 6],
    [2, 'x', 'x', 6, 5, 6, 7, 1, 'x', 8],
    [17, 9, 5, 3, 3, 'x', 16, 18, 'x', 8],
    [10, 'x', 14, 16, 'x', 8, 'x', 9, 6, 'x'],
    ['x', 17, 8, 11, 12, 'x', 4, 8, 'x', 13],
    ['x', 'x', 6, 'x', 'x', 'x', 'x', 13, 'x', 7],
    [9, 'x', 'x', 'x', 3, 10, 'x', 3, 10, 1]
]

start = (5, 1)
end = (3, 9)
print(bfs(matrix, start, end))
