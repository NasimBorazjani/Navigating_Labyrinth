
from collections import deque

# Define the city map
city_map = [
    ['x', 9, 'x', 10, 'x', 11, 13, 5, 4, 'x', 'x', 19, 13, 'x', 'x'],
    ['x', 6, 3, 8, 18, 8, 1, 5, 2, 'x', 'x', 17, 'x', 'x', 'x'],
    ['x', 'x', 11, 5, 'x', 11, 13, 20, 7, 'x', 'x', 'x', 'x', 15, 4],
    ['x', 3, 'x', 14, 4, 20, 4, 15, 12, 12, 4, 'x', 8, 4, 'x'],
    [4, 1, 'x', 9, 17, 'x', 17, 'x', 11, 16, 6, 12, 'x', 18, 'x'],
    [8, 5, 17, 'x', 'x', 1, 'x', 'x', 'x', 19, 14, 2, 1, 'x', 'x'],
    [11, 9, 'x', 'x', 14, 'x', 'x', 'x', 'x', 'x', 'x', 2, 12, 4, 16],
    ['x', 'x', 2, 'x', 'x', 6, 6, 8, 'x', 11, 18, 11, 10, 'x', 'x'],
    ['x', 'x', 'x', 16, 'x', 7, 'x', 'x', 'x', 'x', 7, 11, 18, 9, 17],
    [13, 19, 13, 'x', 18, 'x', 14, 'x', 14, 14, 'x', 'x', 20, 15, 15],
    ['x', 'x', 'x', 'x', 17, 'x', 8, 'x', 'x', 'x', 'x', 'x', 6, 11, 'x'],
    [5, 'x', 7, 'x', 15, 'x', 'x', 19, 1, 'x', 'x', 10, 'x', 'x', 18],
    [11, 19, 'x', 18, 'x', 5, 'x', 19, 16, 'x', 'x', 13, 'x', 'x', 5],
    [8, 16, 6, 13, 1, 'x', 14, 4, 'x', 'x', 'x', 1, 'x', 'x', 5],
    ['x', 19, 5, 'x', 'x', 'x', 12, 5, 9, 16, 11, 9, 14, 'x', 'x']
]

# Define the start and end points
start = (8, 13)
end = (3, 3)

# Define the BFS function
def bfs(start, end, city_map):
    queue = deque([([start], 0, {1: False, 2: False, 3: False})])
    while queue:
        path, time, districts = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and city_map[nx][ny] != 'x':
                new_districts = districts.copy()
                new_districts[(nx // 4) + 1] = True
                if all(new_districts.values()):
                    new_path = path + [(nx, ny)]
                    new_time = time + city_map[nx][ny]
                    queue.append((new_path, new_time, new_districts))

# Print the quickest route
print(bfs(start, end, city_map))
