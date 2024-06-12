
from collections import deque

grid = [
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0]
]

def is_valid(x, y, visited):
    return (0 <= x < len(grid) and 
            0 <= y < len(grid[0]) and 
            grid[x][y] != 1 and 
            (x, y) not in visited)

def get_moves(pos):
    x, y = pos
    moves = [(x-2, y-1), (x-2, y+1), (x-1, y-2), (x-1, y+2), 
             (x+1, y-2), (x+1, y+2), (x+2, y-1), (x+2, y+1)]
    return [move for move in moves if is_valid(*move, visited)]

def bfs(start, end):
    queue = deque([[start]])
    visited = set([start])
    while queue:
        path = queue.popleft()
        pos = path[-1]
        if pos == end:
            return path
        for move in get_moves(pos):
            if len(path) == 3 or move not in visited:
                new_path = list(path)
                new_path.append(move)
                visited.add(move)
                queue.append(new_path)

start, end = (0, 10), (9, 2)
path = bfs(start, end)
print(path)
