
from collections import deque

def is_valid(grid, visited, pos, dest, diag_jumps):
    x, y = pos
    dx, dy = dest

    # Check if within grid, not broken, and exactly 3 diagonal jumps
    if x<0 or y<0 or x>=10 or y>=10 or grid[x][y]==1 or visited[x][y] or (abs(x-dx) + abs(y-dy) - 3*diag_jumps != 0):
        return False
    return True

def bfs(grid, start, dest):
    visited = [[0]*10 for _ in range(10)]
    queue = deque([(start, [], 0)])
    while queue:
        pos, path, diag_jumps = queue.popleft()
        if pos == dest:
            return path + [pos]
        for dx, dy in [(-1,1), (1,1), (-1,-1), (1,-1), (1,0), (-1,0), (0,1), (0,-1)]:
            x, y = pos[0]+dx, pos[1]+dy
            if is_valid(grid, visited, (x, y), dest, diag_jumps+(abs(dx)!=abs(dy))):
                visited[x][y] = 1
                queue.append(((x, y), path + [pos], diag_jumps+(abs(dx)!=abs(dy))))

grid = [[0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 0]]

start = (0, 4)
dest = (9, 8)

print(bfs(grid, start, dest))
