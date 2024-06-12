
from collections import deque

map = [
    [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0]
]

def is_valid(x, y, visited, n_diag):
    return (0 <= x < len(map) and 0 <= y < len(map[0]) and 
            map[x][y] == 0 and (x != 11 or y != 12) and 
            (abs(x - 11) + abs(y - 12) + abs(x - 3) + abs(y - 1)) == 4 + 2 * n_diag)

def bfs(start, dest, n_diag):
    visited = [[False]*len(map[0]) for _ in range(len(map))]
    visited[start[0]][start[1]] = True
    queue = deque([(start, [])])
    while queue:
        point, path = queue.popleft()
        if point == dest:
            return path + [point]
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            x, y = point[0] + dx, point[1] + dy
            if is_valid(x, y, visited, n_diag):
                visited[x][y] = True
                queue.append(((x, y), path + [point]))

print(bfs((11, 12), (3, 1), 2))
