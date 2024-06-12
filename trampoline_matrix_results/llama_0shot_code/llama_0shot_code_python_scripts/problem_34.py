
from collections import deque

def get_neighbors(pos, grid):
    x, y = pos
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
    valid_neighbors = [n for n in neighbors if 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0]) and grid[n[0]][n[1]] == 0]
    return valid_neighbors

def bfs(start, end, grid):
    queue = deque([start])
    path_dict = {start: None}
    while queue:
        pos = queue.popleft()
        if pos == end:
            path = []
            while pos is not None:
                path.append(pos)
                pos = path_dict[pos]
            return path[::-1]
        for neighbor in get_neighbors(pos, grid):
            if neighbor not in path_dict:
                queue.append(neighbor)
                path_dict[neighbor] = pos
    return None

grid = [
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

start = (10, 10)
end = (5, 0)

path = bfs(start, end, grid)

print(path)
