
from collections import deque

# Define the grid
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

# Define the start and end points
start = (0, 10)
end = (9, 2)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Define the BFS function
def bfs(start, end):
    queue = deque([(start, [start])])
    seen = set([start])
    while queue:
        (x, y), path = queue.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if (0 <= nx < 11 and 0 <= ny < 11 and grid[nx][ny] == 0 and
                (nx, ny) not in seen):
                if len(path) < 4:
                    queue.append(((nx, ny), path + [(nx, ny)]))
                    seen.add((nx, ny))
                elif (nx, ny) == end:
                    return path + [(nx, ny)]
    return None

# Print the shortest sequence of trampolines
print(bfs(start, end))
