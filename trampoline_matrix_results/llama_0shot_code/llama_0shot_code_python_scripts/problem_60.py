
from collections import deque

# Grid map of the trampoline park
grid = [
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
]

def is_valid(x, y, visited):
    # Check if the trampoline is within the grid, not broken, and not visited
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and not visited[x][y]

def bfs(start, end):
    # Initialize the visited matrix and the queue
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    queue = deque([(start, [start])])

    while queue:
        x, y, path = queue.popleft()
        if (x, y) == end:
            return path

        # Check the eight adjacent trampolines
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited):
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None

# Find the shortest sequence of trampolines
start, end = (1, 0), (11, 7)
path = bfs(start, end)
print(path)
