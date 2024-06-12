
from collections import deque

# Map of the trampoline park
map = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0]
]

# Function to check if a position is valid
def is_valid(x, y, visited):
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
        return False
    if map[x][y] == 1 or visited[x][y]:
        return False
    return True

# Function to find the shortest path
def shortest_path(start, end, max_diagonal_jumps):
    queue = deque([(start, 0, [start])])
    visited = [[False]*len(map[0]) for _ in range(len(map))]
    visited[start[0]][start[1]] = True

    while queue:
        (x, y), diagonal_jumps, path = queue.popleft()

        if (x, y) == end:
            return path

        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited):
                visited[nx][ny] = True
                queue.append(((nx, ny), diagonal_jumps + 1 if dx * dy == 1 else diagonal_jumps, path + [(nx, ny)]))

    return None

# Function to convert list of tuples to string
def list_to_str(lst):
    return '[' + ', '.join(str(pos) for pos in lst) + ']'

# Start position and end position
start = (2, 13)
end = (8, 0)

# Find the shortest path
path = shortest_path(start, end, 4)

# Print the result
print("The shortest sequence of trampolines:", list_to_str(path))
