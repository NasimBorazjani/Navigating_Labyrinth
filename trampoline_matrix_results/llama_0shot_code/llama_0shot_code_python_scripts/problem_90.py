
from collections import deque

def get_neighbors(pos, grid):
    row, col = pos
    neighbors = [(row-1, col-1), (row-1, col), (row-1, col+1),
                 (row, col-1),                 (row, col+1),
                 (row+1, col-1), (row+1, col), (row+1, col+1)]
    valid_neighbors = [n for n in neighbors if 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0]) and grid[n[0]][n[1]] == 0]
    return valid_neighbors

def is_valid(pos, grid, visited, seq):
    diagonal_jumps = sum(abs(pos[i]-seq[0][i]) for i in (0,1))
    return pos not in visited and diagonal_jumps == 4

def bfs(start, dest, grid):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        pos, seq = queue.popleft()
        if pos == dest:
            return seq
        for n in get_neighbors(pos, grid):
            if is_valid(n, grid, visited, seq):
                queue.append((n, seq + [n]))
                visited.add(n)

grid = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
        [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1]]

start = (12, 11)
dest = (0, 4)

seq = bfs(start, dest, grid)
print(seq)
