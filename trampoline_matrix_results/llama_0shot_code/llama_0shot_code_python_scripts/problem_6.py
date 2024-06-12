
from collections import deque

def bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]  # 8 adjacent trampolines + 3 diagonals
    queue = deque([(start, [start], 0)])  # (current position, path, number of diagonal jumps)
    visited = set()
    while queue:
        pos, path, diags = queue.popleft()
        if pos == end:
            return path[1:]  # exclude the starting trampoline
        for d in directions:
            next_pos = (pos[0] + d[0], pos[1] + d[1])
            if (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols and 
                grid[next_pos[0]][next_pos[1]] == 0 and 
                next_pos not in visited and 
                (next_pos[0] != pos[0] and next_pos[1] != pos[1]) == (diags < 3)):
                visited.add(next_pos)
                queue.append((next_pos, path + [next_pos], (diags + 1) % 4))

grid = [[1, 0, 1, 0, 0, 1, 0, 1, 0], [1, 1, 1, 0, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 0, 1, 1, 0], [0, 0, 1, 1, 0, 0, 1, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1, 1, 1, 1]]
start, end = (0, 6), (8, 2)
print(bfs(grid, start, end))
