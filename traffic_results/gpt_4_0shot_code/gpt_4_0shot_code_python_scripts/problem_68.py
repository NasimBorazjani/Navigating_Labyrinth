
from collections import deque

# Define the city map
city_map = [
    [18, 'x', 'x', 'x', 19, 'x', 'x', 8, 6, 3, 'x', 'x', 'x'],
    ['x', 'x', 8, 1, 11, 'x', 'x', 'x', 'x', 'x', 4, 6, 4],
    [1, 4, 15, 13, 17, 11, 'x', 15, 'x', 13, 1, 'x', 'x'],
    [3, 'x', 6, 1, 15, 2, 'x', 13, 13, 'x', 10, 'x', 'x'],
    [17, 12, 13, 11, 6, 1, 3, 'x', 'x', 19, 6, 6, 'x'],
    ['x', 17, 7, 12, 1, 15, 17, 20, 3, 'x', 'x', 18, 10],
    [16, 14, 15, 'x', 'x', 11, 'x', 17, 20, 15, 7, 10, 'x'],
    [5, 11, 'x', 7, 19, 'x', 6, 18, 15, 'x', 8, 'x', 1],
    [10, 'x', 1, 'x', 'x', 6, 'x', 11, 'x', 13, 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 4, 'x', 8, 'x', 12, 'x', 12, 13, 'x'],
    ['x', 'x', 18, 14, 'x', 'x', 5, 'x', 'x', 13, 1, 'x', 'x'],
    ['x', 'x', 1, 17, 8, 18, 'x', 7, 'x', 'x', 16, 8, 'x'],
    ['x', 'x', 'x', 16, 1, 'x', 19, 'x', 'x', 'x', 'x', 14, 'x']
]

# Define the start and end points
start = (5, 12)
end = (1, 2)

# Define the BFS function
def bfs(start, end, city_map):
    queue = deque([([start], 0, {1, 2, 3})])
    while queue:
        path, time, districts = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and city_map[nx][ny] != 'x':
                new_time = time + city_map[nx][ny]
                new_districts = districts - {1 if nx < 2 else 2 if nx < 6 else 3}
                if not new_districts or (nx, ny) == end:
                    queue.append((path + [(nx, ny)], new_time, new_districts))

# Print the quickest route
print(bfs(start, end, city_map))
