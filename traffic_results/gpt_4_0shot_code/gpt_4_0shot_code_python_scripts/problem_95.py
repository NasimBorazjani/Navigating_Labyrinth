
from collections import deque

def bfs(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False]*cols for _ in range(rows)]
    queue = deque([(start, [start], {get_district(start)} )])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        (x, y), path, districts = queue.popleft()
        if (x, y) == end and len(districts) == 3:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and matrix[nx][ny] != 'x':
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(nx, ny)], districts | {get_district((nx, ny))}))

def get_district(pos):
    x, y = pos
    if 0 <= x <= 4:
        return 1
    elif 5 <= x <= 9:
        return 2
    else:
        return 3

matrix = [
    ['x', 'x', 'x', 'x', 9, 'x', 14, 17, 'x', 13, 3, 'x', 13, 10, 18],
    [1, 'x', 11, 12, 14, 13, 8, 'x', 5, 7, 'x', 'x', 'x', 'x', 'x'],
    [3, 'x', 'x', 18, 11, 16, 'x', 'x', 'x', 'x', 1, 'x', 15, 12, 10],
    ['x', 10, 'x', 3, 2, 15, 14, 'x', 'x', 'x', 17, 'x', 6, 1, 'x'],
    [8, 10, 'x', 'x', 'x', 'x', 1, 19, 6, 'x', 17, 2, 'x', 'x', 'x'],
    ['x', 6, 15, 2, 17, 2, 11, 5, 9, 'x', 12, 15, 'x', 'x', 16],
    ['x', 'x', 8, 'x', 14, 'x', 13, 20, 17, 12, 19, 9, 'x', 'x', 'x'],
    [13, 10, 1, 4, 11, 3, 15, 'x', 'x', 3, 14, 20, 'x', 6, 'x'],
    ['x', 11, 16, 9, 19, 18, 12, 2, 'x', 'x', 1, 10, 'x', 'x', 'x'],
    ['x', 13, 18, 18, 7, 'x', 'x', 'x', 'x', 18, 5, 6, 'x', 7, 3],
    ['x', 'x', 'x', 18, 6, 16, 10, 18, 9, 19, 'x', 3, 5, 3, 4],
    [14, 18, 4, 1, 17, 'x', 7, 'x', 3, 16, 11, 'x', 17, 11, 1],
    ['x', 'x', 12, 16, 'x', 14, 9, 'x', 'x', 'x', 13, 1, 'x', 'x', 19],
    [19, 'x', 3, 'x', 8, 'x', 'x', 'x', 3, 'x', 'x', 'x', 17, 9, 8],
    [15, 'x', 2, 8, 9, 13, 'x', 14, 'x', 6, 'x', 19, 'x', 'x', 5]
]

start = (5, 2)
end = (9, 13)
print(bfs(matrix, start, end))
