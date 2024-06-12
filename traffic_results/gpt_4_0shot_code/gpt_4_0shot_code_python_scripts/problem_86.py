
from collections import deque

# Define the city map
city_map = [
    ['x', 'x', 11, 16, 'x', 'x', 'x', 'x', 4, 'x', 14, 5, 'x', 'x'],
    [3, 1, 13, 'x', 'x', 14, 11, 'x', 'x', 15, 12, 15, 'x', 'x'],
    [17, 15, 17, 10, 11, 'x', 7, 1, 1, 14, 'x', 9, 'x', 'x'],
    [8, 'x', 'x', 13, 2, 12, 'x', 8, 'x', 'x', 9, 13, 19, 5],
    [4, 'x', 2, 3, 8, 'x', 'x', 17, 'x', 'x', 16, 10, 'x', 'x'],
    ['x', 'x', 'x', 'x', 3, 13, 14, 16, 18, 11, 4, 19, 20, 'x'],
    ['x', 11, 'x', 'x', 3, 10, 8, 9, 18, 7, 1, 14, 'x', 6],
    [11, 'x', 12, 11, 'x', 11, 10, 3, 10, 12, 15, 'x', 11, 'x'],
    ['x', 'x', 4, 18, 'x', 'x', 13, 'x', 14, 10, 'x', 8, 'x', 17],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 7, 7, 'x', 'x', 18, 19, 18],
    [19, 4, 'x', 2, 14, 2, 'x', 9, 'x', 10, 7, 17, 4, 12],
    [13, 2, 'x', 'x', 18, 5, 'x', 11, 'x', 'x', 'x', 18, 'x', 'x'],
    ['x', 'x', 13, 1, 13, 'x', 2, 'x', 'x', 'x', 'x', 'x', 'x', 14],
    ['x', 12, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 19, 'x', 'x', 9, 1]
]

# Define the start and end points
start = (3, 0)
end = (5, 12)

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
