
from collections import deque

# Define the city map
city_map = [
    [7, 'x', 19, 11, 6, 'x', 4, 15, 9, 3],
    ['x', 'x', 13, 'x', 8, 17, 'x', 'x', 12, 16],
    ['x', 'x', 2, 'x', 15, 8, 'x', 13, 4, 'x'],
    [13, 11, 3, 3, 3, 'x', 'x', 'x', 'x', 'x'],
    [1, 16, 14, 6, 14, 17, 4, 9, 1, 'x'],
    ['x', 4, 9, 'x', 17, 17, 'x', 13, 2, 9],
    ['x', 'x', 'x', 'x', 5, 14, 17, 12, 7, 14],
    ['x', 15, 1, 6, 'x', 'x', 5, 'x', 'x', 1],
    ['x', 'x', 19, 'x', 'x', 'x', 'x', 'x', 13, 8],
    ['x', 6, 9, 12, 8, 8, 'x', 18, 'x', 'x']
]

# Define the start and end points
start = (5, 9)
end = (3, 1)

# Define the districts
districts = [(0, 3), (4, 4), (5, 9)]

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

# Run the BFS function
path = bfs(start, end, city_map, districts)

# Print the path
print(path)
