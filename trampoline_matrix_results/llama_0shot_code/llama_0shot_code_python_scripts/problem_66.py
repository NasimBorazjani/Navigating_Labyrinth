
from collections import deque

map = [
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1]
]

def is_valid(x, y, visited, diagonal_jumps):
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
        return False
    if map[x][y] == 1:
        return False
    if visited[x][y] == 1:
        return False
    if (x != 12 or y != 9) and (x, y) not in [(3, 1), (12, 9)]:
        if abs(x - 12) + abs(y - 9) != abs(3 - 1) + abs(1 - 9) - 2 * diagonal_jumps:
            return False
    return True

def bfs(start, end, diagonal_jumps):
    visited = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]
    queue = deque([(start, [start])])
    visited[start[0]][start[1]] = 1

    while queue:
        x, y = queue.popleft()[0]
        if (x, y) == end:
            return queue.popleft()[1]

        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited, diagonal_jumps):
                visited[nx][ny] = 1
                queue.append(((nx, ny), queue[-1][1] + [(nx, ny)]))

    return None

start = (12, 9)
end = (3, 1)
diagonal_jumps = 2
path = bfs(start, end, diagonal_jumps)
print(path)
