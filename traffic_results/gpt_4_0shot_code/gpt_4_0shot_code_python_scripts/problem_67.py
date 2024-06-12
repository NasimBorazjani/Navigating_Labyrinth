
from collections import deque

def bfs(matrix, start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        (x, y), path = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and
                matrix[nx][ny] != 'x' and (nx, ny) not in visited):
                if (nx, ny) == end:
                    return path + [(nx, ny)]
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    return None

matrix = [
    ['x', 'x', 10, 'x', 'x', 'x', 3, 'x', 'x', 'x', 'x', 'x', 'x'],
    [6, 19, 'x', 'x', 'x', 12, 'x', 'x', 3, 'x', 'x', 'x', 'x'],
    [5, 3, 7, 7, 'x', 7, 9, 'x', 18, 'x', 'x', 'x', 'x'],
    [1, 4, 19, 19, 16, 6, 'x', 2, 10, 'x', 1, 7, 'x'],
    [14, 10, 'x', 'x', 2, 3, 5, 3, 13, 7, 'x', 8, 'x'],
    ['x', 8, 11, 14, 18, 'x', 'x', 16, 15, 8, 'x', 10, 'x'],
    ['x', 17, 'x', 'x', 15, 'x', 'x', 1, 17, 9, 7, 'x', 10],
    [18, 6, 14, 4, 12, 12, 'x', 12, 5, 'x', 'x', 5, 18],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 7, 17, 4, 16, 'x', 'x'],
    ['x', 6, 17, 'x', 'x', 'x', 'x', 'x', 15, 'x', 'x', 12, 'x'],
    [14, 'x', 'x', 12, 3, 11, 'x', 'x', 'x', 'x', 'x', 'x', 17],
    ['x', 16, 'x', 'x', 'x', 3, 5, 19, 'x', 16, 14, 'x', 19],
    [13, 'x', 11, 'x', 3, 16, 'x', 1, 'x', 'x', 1, 'x', 'x']
]

start = (2, 3)
end = (8, 10)
print(bfs(matrix, start, end))
