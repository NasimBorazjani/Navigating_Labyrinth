
from collections import deque

# Map of the trampoline park
park = [
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
]

# Function to check if a position is valid
def is_valid(x, y, visited):
    if x < 0 or y < 0 or x >= len(park) or y >= len(park[0]) or park[x][y] == 1 or visited[x][y]:
        return False
    return True

# Function to find the shortest path
def shortest_path(start, end, park):
    visited = [[False for _ in range(len(park[0]))] for _ in range(len(park))]
    visited[start[0]][start[1]] = True
    queue = deque([(start, [start])])
    while queue:
        current_position, path = queue.popleft()
        if current_position == end:
            return path
        for x, y in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-2, 0), (2, 0), (0, -2), (0, 2)]:
            next_position = (current_position[0] + x, current_position[1] + y)
            if is_valid(next_position[0], next_position[1], visited):
                visited[next_position[0]][next_position[1]] = True
                queue.append((next_position, path + [next_position]))

# Start position and end position
start = (2, 1)
end = (10, 9)

# Find the shortest path
path = shortest_path(start, end, park)

# Print the result
print(path)
