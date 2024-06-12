
from collections import deque

# Define the city map
city_map = [
    [18, 9, 2, 'x', 9, 14, 'x', 1, 'x'],
    [3, 14, 18, 7, 'x', 3, 'x', 2, 19],
    [6, 18, 20, 3, 13, 'x', 6, 10, 'x'],
    [20, 'x', 12, 4, 14, 6, 'x', 'x', 'x'],
    [7, 18, 8, 5, 19, 3, 'x', 'x', 7],
    [15, 9, 14, 16, 5, 14, 6, 'x', 'x'],
    ['x', 5, 13, 'x', 'x', 19, 'x', 'x', 2],
    ['x', 'x', 8, 'x', 'x', 'x', 'x', 17, 12],
    ['x', 1, 'x', 'x', 3, 19, 'x', 2, 18]
]

# Define the start and end points
start = (2, 0)
end = (5, 6)

# Define the districts
districts = [(0, 2), (3, 4), (5, 8)]

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

# Call the BFS function
path = bfs(start, end, city_map, districts)

# Print the path
print(path)
