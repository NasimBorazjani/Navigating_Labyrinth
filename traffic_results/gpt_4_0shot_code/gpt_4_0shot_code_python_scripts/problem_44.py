
from collections import deque

# Define the city map
city_map = [
    ['x', 16, 5, 13, 'x', 'x', 2, 'x', 6, 'x', 'x'],
    ['x', 'x', 17, 'x', 15, 'x', 10, 'x', 5, 17, 'x'],
    ['x', 'x', 'x', 'x', 15, 3, 10, 2, 4, 13, 14],
    ['x', 'x', 'x', 'x', 17, 2, 4, 'x', 1, 4, 5],
    [2, 'x', 'x', 2, 6, 17, 'x', 'x', 'x', 4, 19],
    [19, 5, 'x', 'x', 'x', 'x', 10, 12, 1, 18, 10],
    ['x', 3, 'x', 12, 'x', 10, 15, 11, 'x', 4, 15],
    [2, 'x', 11, 9, 'x', 12, 11, 'x', 15, 10, 6],
    [19, 'x', 16, 5, 'x', 'x', 'x', 11, 'x', 11, 8],
    [12, 2, 'x', 3, 'x', 4, 'x', 'x', 15, 'x', 'x'],
    ['x', 'x', 18, 16, 'x', 'x', 4, 'x', 12, 13, 'x']
]

# Define the start and end points
start = (8, 10)
end = (3, 4)

# Define the districts
districts = [(0, 2), (3, 7), (8, 10)]

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
