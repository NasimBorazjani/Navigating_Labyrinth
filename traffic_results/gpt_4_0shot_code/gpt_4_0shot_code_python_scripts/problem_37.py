
from collections import deque

def bfs(matrix, start, end):
    queue = deque([([start], 0)])
    seen = set([start])
    while queue:
        (path, length) = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and
                matrix[nx][ny] != 'x' and (nx, ny) not in seen):
                queue.append((path + [(nx, ny)], length + matrix[nx][ny]))
                seen.add((nx, ny))

matrix = [
    [15, 'x', 12, 'x', 9, 19, 'x', 'x', 13, 'x', 16],
    [14, 6, 3, 18, 'x', 8, 18, 'x', 'x', 'x', 'x'],
    [16, 10, 9, 4, 9, 5, 15, 4, 'x', 'x', 2],
    [5, 9, 'x', 8, 1, 15, 7, 15, 'x', 'x', 'x'],
    [6, 'x', 3, 'x', 4, 6, 6, 19, 'x', 16, 13],
    [17, 'x', 11, 5, 18, 11, 18, 'x', 'x', 10, 19],
    [6, 3, 'x', 'x', 10, 18, 2, 'x', 'x', 'x', 'x'],
    ['x', 'x', 4, 2, 'x', 13, 7, 'x', 3, 19, 16],
    ['x', 1, 10, 'x', 15, 'x', 2, 'x', 1, 7, 10],
    ['x', 'x', 'x', 4, 7, 'x', 7, 'x', 'x', 6, 'x'],
    [16, 'x', 15, 3, 'x', 8, 'x', 'x', 13, 'x', 14]
]

start = (7, 5)
end = (1, 0)
print(bfs(matrix, start, end))
