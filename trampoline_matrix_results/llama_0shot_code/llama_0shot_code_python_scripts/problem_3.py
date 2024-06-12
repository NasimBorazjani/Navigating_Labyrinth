
from collections import deque

def is_valid(i, j, n, m, visited):
    if i < 0 or j < 0 or i >= n or j >= m or visited[i][j] == 1 or grid[i][j] == 1:
        return False
    return True

def bfs(grid, src, dest):
    n, m = len(grid), len(grid[0])
    visited = [[0]*m for _ in range(n)]
    visited[src[0]][src[1]] = 1
    q = deque([(src, 0, [])])
    while q:
        curr_pos, diag_jumps, path = q.popleft()
        i, j = curr_pos
        if curr_pos == dest:
            return path + [curr_pos]
        for x, y in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            dx, dy = curr_pos[0] + x, curr_pos[1] + y
            if is_valid(dx, dy, n, m, visited):
                visited[dx][dy] = 1
                q.append(((dx, dy), diag_jumps+1, path + [curr_pos]))
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dx, dy = curr_pos[0] + x, curr_pos[1] + y
            if is_valid(dx, dy, n, m, visited):
                visited[dx][dy] = 1
                q.append(((dx, dy), diag_jumps, path + [curr_pos]))
    return None

grid = [
    [0, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0]
]

src = (8, 6)
dest = (0, 0)

path = bfs(grid, src, dest)
print(path)
