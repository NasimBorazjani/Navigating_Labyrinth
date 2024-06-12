
from collections import deque

# Define the city map
city_map = [
    ['x', 'x', 14, 'x', 3, 'x', 18, 'x', 4, 4, 'x', 'x', 16, 'x'],
    ['x', 'x', 1, 15, 'x', 18, 'x', 18, 'x', 'x', 'x', 'x', 14, 'x'],
    ['x', 'x', 7, 14, 'x', 'x', 16, 'x', 'x', 'x', 'x', 5, 19, 15],
    ['x', 13, 18, 'x', 17, 'x', 6, 8, 'x', 8, 'x', 'x', 13, 'x'],
    [12, 'x', 15, 'x', 'x', 'x', 'x', 18, 'x', 'x', 'x', 8, 6, 7],
    [5, 11, 14, 14, 11, 5, 13, 7, 'x', 'x', 10, 12, 17, 17],
    [14, 'x', 3, 15, 3, 'x', 'x', 17, 12, 7, 19, 15, 4, 5],
    ['x', 2, 14, 'x', 8, 'x', 9, 19, 16, 14, 17, 12, 'x', 13],
    ['x', 'x', 2, 15, 'x', 'x', 'x', 2, 14, 17, 3, 4, 'x', 12],
    [2, 'x', 11, 'x', 'x', 14, 'x', 'x', 16, 'x', 11, 13, 'x', 'x'],
    [17, 'x', 'x', 2, 9, 14, 8, 'x', 11, 5, 'x', 10, 5, 'x'],
    [4, 'x', 8, 8, 11, 'x', 16, 'x', 'x', 'x', 15, 'x', 2, 16],
    ['x', 16, 'x', 'x', 9, 'x', 'x', 'x', 'x', 19, 6, 9, 'x', 'x'],
    ['x', 14, 9, 'x', 6, 1, 7, 'x', 10, 4, 'x', 'x', 'x', 'x']
]

# Define the start and end points
start = (2, 13)
end = (5, 1)

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
                new_districts = districts - {get_district(nx)}
                if new_districts or (nx, ny) == end:
                    queue.append((path + [(nx, ny)], new_time, new_districts))

# Define the function to get the district of a workshop
def get_district(x):
    if x < 3:
        return 1
    elif x < 6:
        return 2
    else:
        return 3

# Call the BFS function
print(bfs(start, end, city_map))
