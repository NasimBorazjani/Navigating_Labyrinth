
from collections import deque

def is_valid(pos, grid, visited):
    x, y = pos
    if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]==1 or pos in visited:
        return False
    return True

def bfs(start, end, grid):
    queue = deque([(start, [start])])
    visited = {start: [start]}
    
    while queue:
        pos, path = queue.popleft()
        if pos == end:
            return path
        
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-2, 0), (2, 0), (0, -2), (0, 2)]:
            next_pos = (pos[0]+dx, pos[1]+dy)
            if is_valid(next_pos, grid, visited):
                queue.append((next_pos, path+[next_pos]))
                visited[next_pos] = path+[next_pos]
    
    return "No solution"

grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
        [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1]]

start, end = (2, 12), (10, 1)
print(bfs(start, end, grid))
