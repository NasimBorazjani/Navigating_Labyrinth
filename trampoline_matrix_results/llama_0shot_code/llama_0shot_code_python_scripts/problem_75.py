
from collections import deque

map = [
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1]
]

def is_valid(x, y, dx, dy, visited, n):
    return (0 <= x < len(map) and 0 <= y < len(map[0]) and 
            map[x][y] == 0 and not visited[x][y] and 
            (dx == 0 or dy == 0 or abs(dx) == abs(dy)) and 
            abs(dx) + abs(dy) == n)

def bfs(start, end, n):
    queue = deque([(start, [])])
    visited = [[False]*len(map[0]) for _ in range(len(map))]
    visited[start[0]][start[1]] = True

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return [(x, y) for x, y in path] + [(x, y)]

        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, dx, dy, visited, n):
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(x, y)]))

print(bfs((0, 7), (12, 0), 4))
