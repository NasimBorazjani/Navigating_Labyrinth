
from collections import deque

# Grid map
grid = [[1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 0, 1, 0]]

# Function to check if a position is valid
def is_valid(pos, visited):
    x, y = pos
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 1 or visited[x][y]:
        return False
    return True

# Function to generate next positions
def next_positions(pos):
    x, y = pos
    directions = [(x-2, y-1), (x-2, y+1), (x-1, y-2), (x-1, y+2), (x+1, y-2), (x+1, y+2), (x+2, y-1), (x+2, y+1)]
    return [d for d in directions if is_valid(d, visited)]

# BFS algorithm
def shortest_path(start, end):
    queue = deque([(start, [start])])
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    visited[start[0]][start[1]] = True

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        for next_pos in next_positions(current):
            queue.append((next_pos, path + [next_pos]))

start, end = (1, 9), (8, 3)
print(shortest_path(start, end))
