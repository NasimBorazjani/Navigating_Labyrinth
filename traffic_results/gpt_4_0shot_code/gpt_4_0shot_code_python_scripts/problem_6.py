
from collections import deque

def bfs(matrix, start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        (x, y), path = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] != 'x' and (nx, ny) not in visited:
                if (nx, ny) == end:
                    return path + [(nx, ny)]
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    return None

matrix = [
    [6, 16, 'x', 'x', 15, 'x', 14, 11, 'x'],
    [5, 2, 1, 'x', 3, 'x', 4, 13, 'x'],
    ['x', 7, 'x', 'x', 13, 'x', 10, 14, 5],
    [6, 16, 'x', 13, 6, 'x', 16, 'x', 'x'],
    ['x', 1, 17, 'x', 6, 3, 'x', 'x', 3],
    [11, 10, 7, 19, 15, 8, 12, 6, 'x'],
    [18, 'x', 'x', 9, 8, 9, 'x', 'x', 13],
    [4, 'x', 'x', 'x', 18, 20, 'x', 'x', 'x'],
    ['x', 'x', 8, 'x', 18, 2, 6, 13, 'x']
]

start = (5, 5)
end = (1, 0)

path = bfs(matrix, start, end)
print(path)
