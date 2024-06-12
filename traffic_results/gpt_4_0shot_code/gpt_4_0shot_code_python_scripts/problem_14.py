
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
    ['x', 3, 13, 18, 'x', 'x', 3, 'x', 'x'],
    ['x', 3, 'x', 'x', 18, 1, 13, 'x', 'x'],
    ['x', 'x', 'x', 6, 'x', 13, 'x', 11, 1],
    [4, 3, 'x', 'x', 'x', 'x', 6, 6, 11],
    [14, 16, 'x', 'x', 'x', 'x', 'x', 18, 11],
    [14, 'x', 11, 'x', 'x', 4, 'x', 1, 'x'],
    [18, 7, 1, 'x', 8, 'x', 'x', 'x', 'x'],
    [4, 9, 6, 12, 13, 19, 'x', 14, 4],
    ['x', 'x', 17, 12, 7, 7, 9, 3, 1]
]

start = (3, 1)
end = (7, 8)
print(bfs(matrix, start, end))
