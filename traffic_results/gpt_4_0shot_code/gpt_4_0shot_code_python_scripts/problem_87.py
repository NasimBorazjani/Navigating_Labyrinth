
from collections import deque

# Define the city map
city_map = [
    ['x', 6, 19, 13, 'x', 16, 11, 6, 14, 15, 7, 'x', 'x', 'x'],
    ['x', 6, 16, 15, 'x', 19, 16, 18, 'x', 8, 10, 'x', 'x', 'x'],
    ['x', 5, 10, 14, 2, 'x', 'x', 'x', 11, 'x', 11, 'x', 'x', 'x'],
    [6, 13, 15, 10, 'x', 'x', 'x', 'x', 19, 'x', 'x', 'x', 2, 'x'],
    ['x', 15, 10, 6, 6, 8, 10, 9, 11, 'x', 'x', 'x', 16, 'x'],
    ['x', 'x', 'x', 8, 15, 12, 10, 19, 1, 18, 19, 4, 'x', 10],
    [1, 17, 'x', 'x', 6, 8, 4, 'x', 15, 8, 10, 6, 4, 'x'],
    ['x', 'x', 'x', 'x', 13, 'x', 5, 'x', 9, 10, 'x', 'x', 'x', 'x'],
    [12, 'x', 11, 'x', 13, 'x', 11, 7, 5, 13, 'x', 'x', 6, 15],
    ['x', 18, 19, 'x', 'x', 'x', 3, 'x', 16, 11, 'x', 15, 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 2, 15, 'x', 'x', 8, 'x', 'x', 'x'],
    [11, 'x', 6, 13, 12, 'x', 12, 'x', 'x', 9, 'x', 17, 'x', 'x'],
    ['x', 1, 'x', 18, 18, 3, 'x', 11, 13, 1, 13, 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 6, 'x', 'x', 8, 'x', 'x', 'x', 4, 11]
]

# Define the start and end points
start = (3, 0)
end = (6, 12)

# Define the BFS function
def bfs(city_map, start, end):
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
path = bfs(city_map, start, end)

# Print the path
print(path)
