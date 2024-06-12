
from collections import deque

# Define the city map
city_map = [
    ['x', 'x', 8, 16, 3, 'x', 15, 17, 2, 'x', 'x', 5, 'x', 'x'],
    ['x', 'x', 17, 'x', 13, 'x', 4, 'x', 13, 3, 3, 6, 11, 'x'],
    ['x', 'x', 8, 'x', 14, 1, 15, 11, 'x', 18, 12, 'x', 'x', 'x'],
    ['x', 13, 19, 4, 13, 2, 13, 3, 'x', 1, 20, 18, 'x', 15],
    [13, 'x', 1, 'x', 11, 'x', 8, 14, 4, 11, 3, 'x', 'x', 'x'],
    [12, 11, 16, 1, 1, 'x', 5, 1, 'x', 9, 'x', 'x', 1, 'x'],
    [8, 'x', 6, 15, 'x', 7, 19, 13, 2, 'x', 3, 3, 'x', 2],
    [18, 'x', 19, 15, 2, 'x', 'x', 18, 2, 'x', 10, 'x', 'x', 1],
    [3, 4, 'x', 19, 'x', 6, 'x', 7, 'x', 'x', 'x', 'x', 15, 'x'],
    ['x', 'x', 'x', 16, 7, 17, 11, 'x', 7, 'x', 'x', 'x', 'x', 15],
    ['x', 9, 'x', 'x', 'x', 19, 19, 7, 3, 12, 14, 11, 16, 7],
    [8, 19, 15, 1, 'x', 14, 'x', 1, 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 14, 'x', 'x', 'x', 'x', 'x', 18, 'x', 'x', 2, 11, 7, 'x'],
    ['x', 'x', 'x', 'x', 'x', 3, 11, 12, 'x', 'x', 'x', 2, 6, 'x']
]

# Define the start and end points
start = (1, 10)
end = (7, 2)

# Define the BFS function
def bfs(start, end, city_map):
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
path = bfs(start, end, city_map)
print(path)
