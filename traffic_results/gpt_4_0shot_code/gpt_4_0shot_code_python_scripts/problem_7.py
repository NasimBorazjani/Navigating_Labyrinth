
from collections import deque

# Define the city map
city_map = [
    ['x', 7, 7, 12, 7, 'x', 13, 1, 18],
    [9, 18, 'x', 4, 19, 8, 'x', 15, 10],
    [9, 'x', 10, 5, 5, 9, 8, 'x', 'x'],
    [14, 4, 19, 9, 14, 'x', 'x', 7, 9],
    [9, 4, 11, 15, 7, 'x', 17, 3, 'x'],
    [11, 'x', 2, 18, 15, 15, 'x', 'x', 'x'],
    ['x', 5, 10, 'x', 'x', 13, 'x', 9, 'x'],
    [3, 'x', 2, 'x', 12, 'x', 'x', 'x', 4],
    ['x', 'x', 7, 'x', 19, 'x', 'x', 'x', 9]
]

# Define the start and end points
start = (6, 1)
end = (2, 6)

# Define the directions
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

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
print(path)
