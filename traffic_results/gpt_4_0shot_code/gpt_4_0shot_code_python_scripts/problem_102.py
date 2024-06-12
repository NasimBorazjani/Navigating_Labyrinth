
from collections import deque

def bfs(matrix, start, end):
    queue = deque([([start], 0)])
    seen = set([start])
    while queue:
        (path, length) = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and
                matrix[nx][ny] != 'x' and (nx, ny) not in seen):
                queue.append((path + [(nx, ny)], length + matrix[nx][ny]))
                seen.add((nx, ny))

matrix = [
    ['x', 13, 'x', 'x', 'x', 'x', 3, 4, 'x', 'x', 9, 'x', 18, 7, 2],
    [1, 10, 17, 'x', 'x', 'x', 11, 13, 'x', 10, 'x', 9, 13, 'x', 'x'],
    ['x', 'x', 7, 18, 'x', 'x', 'x', 'x', 7, 'x', 'x', 'x', 1, 'x', 16],
    [10, 'x', 'x', 'x', 13, 'x', 2, 9, 'x', 'x', 8, 'x', 'x', 5, 'x'],
    ['x', 7, 12, 'x', 1, 18, 14, 'x', 7, 'x', 'x', 16, 'x', 'x', 19],
    [5, 1, 13, 17, 11, 14, 16, 'x', 14, 'x', 18, 5, 'x', 18, 'x'],
    ['x', 15, 19, 4, 'x', 13, 'x', 5, 'x', 'x', 18, 'x', 17, 'x', 'x'],
    [3, 7, 'x', 'x', 'x', 12, 'x', 'x', 17, 4, 'x', 13, 19, 3, 10],
    [11, 'x', 'x', 'x', 'x', 2, 2, 19, 13, 4, 7, 17, 16, 'x', 17],
    [12, 5, 4, 'x', 'x', 'x', 'x', 12, 8, 11, 'x', 17, 14, 19, 2],
    [4, 10, 'x', 'x', 6, 11, 16, 17, 'x', 'x', 18, 'x', 17, 'x', 'x'],
    ['x', 'x', 'x', 'x', 11, 9, 18, 17, 12, 'x', 'x', 'x', 'x', 'x', 1],
    [18, 13, 7, 'x', 'x', 5, 4, 13, 'x', 'x', 19, 12, 1, 18, 'x'],
    [15, 'x', 17, 'x', 'x', 'x', 17, 'x', 'x', 'x', 10, 'x', 15, 16, 'x'],
    ['x', 'x', 11, 15, 'x', 'x', 12, 16, 12, 13, 18, 'x', 17, 8, 15]
]

start = (5, 0)
end = (7, 13)
print(bfs(matrix, start, end))
