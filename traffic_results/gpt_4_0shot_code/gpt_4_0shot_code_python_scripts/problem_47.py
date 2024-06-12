
from collections import deque

# Define the city map
city_map = [
    [5, 'x', 'x', 4, 'x', 12, 7, 11, 8, 3, 19, 'x'],
    ['x', 'x', 6, 15, 16, 'x', 'x', 4, 'x', 7, 8, 19],
    [18, 'x', 'x', 15, 'x', 'x', 'x', 8, 4, 16, 7, 9],
    ['x', 19, 'x', 'x', 'x', 16, 'x', 'x', 17, 15, 'x', 9],
    [15, 8, 19, 'x', 4, 4, 'x', 'x', 'x', 3, 3, 10],
    [18, 6, 14, 5, 'x', 18, 19, 15, 18, 19, 12, 5],
    [12, 'x', 2, 2, 6, 3, 3, 8, 3, 1, 'x', 15],
    [10, 4, 'x', 9, 15, 3, 'x', 7, 'x', 17, 'x', 'x'],
    [5, 18, 'x', 17, 'x', 17, 'x', 'x', 15, 'x', 18, 'x'],
    [4, 'x', 16, 11, 10, 3, 12, 'x', 11, 14, 3, 'x'],
    ['x', 9, 9, 14, 19, 15, 'x', 1, 10, 19, 6, 'x'],
    ['x', 'x', 17, 4, 'x', 2, 'x', 7, 'x', 4, 4, 18]
]

# Define the start and end points
start = (4, 11)
end = (6, 0)

# Define the directions
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Define the BFS function
def bfs(start, end, city_map):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        (x, y), path = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and
                city_map[nx][ny] != 'x' and (nx, ny) not in visited):
                if (nx, ny) == end:
                    return path + [(nx, ny)]
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    return None

# Call the BFS function
path = bfs(start, end, city_map)

# Print the path
print(path)
