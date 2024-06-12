
from collections import deque

# Map of the trampoline park
map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]
]

# Function to check if a position is valid
def is_valid(x, y, visited):
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
        return False
    if visited[x][y] or map[x][y] == 1:
        return False
    return True

# Function to find the shortest path
def shortest_path(start, end):
    visited = [[False]*len(map[0]) for _ in range(len(map))]
    visited[start[0]][start[1]] = True
    queue = deque([(start, [start])])
    while queue:
        point, path = queue.popleft()
        if point == end:
            return path
        for i, j in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-2, 0), (2, 0), (0, -2), (0, 2)]:
            next_point = (point[0]+i, point[1]+j)
            if is_valid(next_point[0], next_point[1], visited):
                visited[next_point[0]][next_point[1]] = True
                queue.append((next_point, path+[next_point]))
    return []

# Find the shortest path
start = (1, 11)
end = (9, 0)
path = shortest_path(start, end)

# Convert the path to the required format
path = [(i, j) for i, j in path]
print(path)
