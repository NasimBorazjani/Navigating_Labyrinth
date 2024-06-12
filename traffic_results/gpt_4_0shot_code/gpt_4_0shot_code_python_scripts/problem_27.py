
from collections import deque

def bfs(matrix, start, end):
    queue = deque([([start], 0)])
    seen = {start}
    while queue:
        (path, length), queue = queue.popleft(), deque(list(queue)[1:])
        x, y = path[-1]
        if (x, y) == end:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < len(matrix) and 0 <= y2 < len(matrix[0]) and matrix[x2][y2] != 'x' and (x2, y2) not in seen:
                queue.append((path + [(x2, y2)], length + matrix[x2][y2]))
                seen.add((x2, y2))

matrix = [
    [19, 'x', 3, 'x', 'x', 'x', 13, 'x', 12, 'x'],
    ['x', 'x', 8, 'x', 15, 18, 11, 12, 'x', 7],
    ['x', 8, 'x', 'x', 15, 20, 17, 12, 2, 8],
    ['x', 'x', 4, 13, 2, 14, 19, 13, 15, 19],
    [13, 2, 'x', 8, 'x', 17, 13, 'x', 'x', 12],
    [2, 20, 20, 14, 'x', 'x', 15, 'x', 2, 19],
    [15, 16, 18, 'x', 2, 'x', 'x', 'x', 'x', 'x'],
    [2, 'x', 17, 'x', 'x', 12, 'x', 'x', 3, 'x'],
    [2, 'x', 10, 'x', 6, 'x', 'x', 9, 8, 19],
    [17, 'x', 6, 13, 'x', 18, 'x', 3, 'x', 18]
]

start = (3, 8)
end = (6, 0)

print(bfs(matrix, start, end))
