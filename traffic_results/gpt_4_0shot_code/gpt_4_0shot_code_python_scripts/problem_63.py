
from collections import deque

# Define the city map
city_map = [
    [16, 9, 19, 14, 16, 19, 6, 'x', 'x', 'x', 16, 18, 'x'],
    [19, 'x', 'x', 9, 9, 'x', 17, 16, 3, 'x', 'x', 14, 'x'],
    ['x', 'x', 11, 'x', 5, 'x', 15, 15, 17, 10, 'x', 13, 5],
    [2, 12, 9, 18, 7, 'x', 'x', 'x', 4, 'x', 10, 'x', 3],
    [8, 9, 19, 1, 'x', 4, 8, 'x', 17, 6, 'x', 18, 'x'],
    ['x', 6, 7, 9, 1, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 5, 4, 12, 13, 13, 'x', 'x', 'x', 11, 'x', 5, 9],
    ['x', 'x', 2, 20, 6, 11, 2, 'x', 'x', 'x', 10, 18, 'x'],
    ['x', 'x', 1, 18, 1, 17, 2, 3, 10, 12, 11, 'x', 19],
    ['x', 16, 3, 'x', 'x', 16, 3, 10, 19, 'x', 'x', 9, 'x'],
    [10, 'x', 'x', 'x', 'x', 1, 10, 13, 'x', 'x', 13, 'x', 'x'],
    ['x', 'x', 'x', 'x', 13, 'x', 1, 14, 'x', 10, 'x', 'x', 8],
    ['x', 'x', 'x', 'x', 'x', 9, 2, 18, 19, 14, 10, 'x', 'x']
]

# Define the start and end points
start = (3, 0)
end = (8, 9)

# Define the districts
districts = [(0, 3), (4, 8), (9, 12)]

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

# Call the BFS function
path = bfs(start, end, city_map, districts)
print(path)
