
from collections import deque

# Matrix map of the city
city_map = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 15, 'x', 'x', 19, 1],
    ['x', 12, 'x', 19, 'x', 'x', 13, 'x', 14, 13, 8, 'x', 1, 6],
    ['x', 17, 'x', 19, 5, 4, 'x', 'x', 12, 'x', 'x', 10, 14, 'x'],
    ['x', 18, 'x', 1, 'x', 14, 'x', 'x', 12, 'x', 11, 4, 4, 7],
    [2, 15, 'x', 'x', 'x', 14, 'x', 16, 5, 2, 4, 'x', 10, 2],
    [8, 2, 15, 18, 19, 6, 13, 7, 6, 'x', 'x', 'x', 1, 'x'],
    [5, 'x', 11, 2, 8, 8, 'x', 1, 10, 8, 13, 7, 12, 18],
    ['x', 18, 8, 19, 'x', 'x', 16, 11, 2, 'x', 9, 'x', 9, 8],
    [4, 10, 'x', 12, 12, 13, 13, 2, 13, 'x', 'x', 'x', 8, 18],
    [1, 'x', 'x', 'x', 5, 12, 18, 16, 5, 17, 'x', 16, 11, 18],
    [19, 'x', 'x', 'x', 'x', 1, 'x', 'x', 'x', 'x', 10, 19, 'x', 'x'],
    ['x', 14, 'x', 'x', 'x', 15, 16, 9, 'x', 'x', 'x', 'x', 'x', 'x'],
    [6, 'x', 16, 18, 6, 'x', 18, 'x', 5, 'x', 'x', 'x', 6, 1],
    ['x', 'x', 'x', 17, 4, 'x', 6, 'x', 'x', 19, 17, 'x', 19, 15]
]

# Start and destination workshops
start = (6, 0)
destination = (4, 13)

# Districts
districts = [(0, 4), (5, 6), (7, 13)]

# BFS algorithm
def bfs(city_map, start, destination, districts):
    queue = deque([(start, [start], [0, 0, 0])])
    while queue:
        (x, y), path, visited = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and city_map[nx][ny] != 'x':
                new_visited = visited[:]
                for i, (d_start, d_end) in enumerate(districts):
                    if d_start <= nx <= d_end:
                        new_visited[i] = 1
                if (nx, ny) == destination and all(new_visited):
                    return path + [(nx, ny)]
                if city_map[nx][ny] != 'x' and (nx, ny) not in path:
                    queue.append(((nx, ny), path + [(nx, ny)], new_visited))

# Find the shortest path
path = bfs(city_map, start, destination, districts)
print(path)
