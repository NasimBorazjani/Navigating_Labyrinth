
from collections import deque

def is_valid(x, y, map, visited):
    if x<0 or y<0 or x>=len(map) or y>=len(map[0]) or map[x][y]==1 or visited[x][y]:
        return False
    return True

def bfs(start, end, map):
    queue = deque([(start, 0, [])])
    visited = [[False]*len(map[0]) for _ in range(len(map))]
    visited[start[0]][start[1]] = True
    while queue:
        x, y, path = queue.popleft()
        path.append((x, y))
        if (x, y) == end:
            return path[::-1]
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, map, visited):
                visited[nx][ny] = True
                queue.append(((nx, ny), 0, path))
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, map, visited):
                visited[nx][ny] = True
                queue.append(((nx, ny), 1, path))
    return None

map = [[1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
[1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
[1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
[0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0],
[1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0],
[0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0],
[0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
[0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
[1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

start = (7, 13)
end = (13, 0)
print(bfs(start, end, map))
