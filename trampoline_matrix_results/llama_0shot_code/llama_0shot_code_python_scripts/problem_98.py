
from collections import deque

# Map of the trampoline park
map = [
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0]
]

# Function to check if a position is valid
def is_valid(x, y, visited):
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
        return False
    if map[x][y] == 1 or visited[x][y]:
        return False
    return True

# Function to find the shortest path
def find_shortest_path(start, end):
    queue = deque([(start, [start])])
    visited = [[False]*len(map[0]) for _ in range(len(map))]
    visited[start[0]][start[1]] = True

    while queue:
        x, y = pos := queue.popleft()
        if pos == end:
            return path
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited):
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None

# Function to find the shortest sequence of trampolines
def shortest_sequence(start, end):
    path = find_shortest_path(start, end)
    return path[1:] if path else None  # Exclude the starting trampoline

# Test the function
start = (1, 2)
end = (12, 11)
print(shortest_sequence(start, end))
