
from collections import deque

# Define the city map
city_map = [
    ['x', 7, 'x', 13, 8, 2, 15, 2, 5, 15, 6, 4, 7, 'x'],
    ['x', 6, 19, 17, 5, 13, 15, 2, 11, 5, 'x', 'x', 9, 8],
    [16, 12, 10, 7, 8, 19, 19, 9, 5, 10, 2, 'x', 'x', 12],
    ['x', 1, 19, 20, 'x', 3, 4, 18, 'x', 'x', 10, 1, 12, 2],
    ['x', 1, 4, 1, 1, 10, 4, 'x', 12, 'x', 5, 10, 3, 8],
    ['x', 'x', 'x', 7, 'x', 'x', 16, 12, 'x', 'x', 'x', 13, 6, 10],
    ['x', 'x', 11, 12, 13, 15, 8, 'x', 12, 1, 16, 14, 8, 15],
    ['x', 11, 'x', 15, 'x', 'x', 'x', 'x', 'x', 'x', 5, 'x', 'x', 14],
    [1, 'x', 'x', 8, 'x', 13, 17, 'x', 3, 12, 'x', 'x', 'x', 'x'],
    [14, 3, 'x', 4, 'x', 'x', 'x', 12, 'x', 7, 'x', 'x', 'x', 'x'],
    ['x', 5, 15, 'x', 10, 17, 'x', 'x', 6, 9, 2, 'x', 'x', 'x'],
    [1, 7, 17, 1, 'x', 'x', 'x', 'x', 11, 'x', 'x', 'x', 'x', 12],
    ['x', 'x', 14, 18, 8, 19, 19, 16, 'x', 6, 5, 16, 17, 7],
    ['x', 'x', 'x', 'x', 'x', 'x', 19, 17, 'x', 'x', 2, 12, 'x', 'x']
]

# Define the start and end points
start = (3, 1)
end = (5, 13)

# Define the districts
districts = [(0, 3), (4, 5), (6, 13)]

# Define the BFS function
def bfs(start, end, city_map, districts):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        (x, y), path = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and
                city_map[nx][ny] != 'x' and (nx, ny) not in visited):
                if (nx, ny) == end:
                    return path + [(nx, ny)]
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    return None

# Find the path
path = bfs(start, end, city_map, districts)
print(path)
