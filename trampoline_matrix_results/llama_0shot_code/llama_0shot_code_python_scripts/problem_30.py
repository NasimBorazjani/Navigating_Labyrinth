
from collections import deque

# Represent the grid and the possible moves
grid = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
]

moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

# Function to check if a position is valid
def is_valid(pos):
    x, y = pos
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

# BFS function
def bfs(start, end):
    queue = deque([(start, [start])])
    while queue:
        pos, path = queue.popleft()
        if pos == end:
            return path
        for move in moves:
            next_x, next_y = pos[0] + move[0], pos[1] + move[1]
            if is_valid((next_x, next_y)):
                new_pos = (next_x, next_y)
                queue.append((new_pos, path + [new_pos]))

# Call the function and print the result
start, end = (0, 9), (7, 3)
path = bfs(start, end)
print(path)
