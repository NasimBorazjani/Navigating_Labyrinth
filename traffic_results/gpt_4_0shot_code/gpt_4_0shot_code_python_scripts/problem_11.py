
from collections import deque

def bfs(matrix, start, end):
    queue = deque([([start], 0)])
    seen = set([start])
    while queue:
        (path, length) = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for (x2, y2) in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < len(matrix) and 0 <= y2 < len(matrix[0]) and matrix[x2][y2] != 'x' and (x2, y2) not in seen:
                queue.append((path + [(x2, y2)], length + matrix[x2][y2]))
                seen.add((x2, y2))
    return None

matrix = [
    ['x', 15, 'x', 18, 8, 6, 11, 'x', 7],
    [9, 10, 18, 9, 2, 16, 9, 8, 'x'],
    [14, 'x', 'x', 10, 18, 'x', 13, 12, 14],
    [11, 18, 4, 11, 14, 2, 20, 'x', 15],
    [12, 'x', 'x', 8, 10, 'x', 'x', 10, 11],
    [5, 19, 20, 15, 11, 'x', 14, 'x', 18],
    ['x', 5, 'x', 'x', 'x', 'x', 'x', 9, 'x'],
    ['x', 'x', 18, 'x', 'x', 4, 'x', 17, 13],
    ['x', 7, 17, 'x', 'x', 'x', 'x', 7, 19]
]

start = (3, 0)
end = (4, 8)

print(bfs(matrix, start, end))
