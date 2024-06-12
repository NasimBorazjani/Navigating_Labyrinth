
from collections import deque

# Define the city map
city_map = [
    [13, 'x', 'x', 3, 10, 20, 3, 'x', 5],
    ['x', 'x', 'x', 'x', 20, 16, 'x', 'x', 17],
    [3, 14, 18, 8, 1, 20, 14, 'x', 7],
    [13, 3, 6, 10, 7, 4, 6, 6, 1],
    [10, 12, 2, 'x', 11, 'x', 10, 8, 11],
    ['x', 'x', 'x', 11, 6, 18, 13, 20, 17],
    ['x', 'x', 16, 'x', 4, 17, 7, 10, 15],
    ['x', 7, 16, 6, 19, 4, 7, 'x', 'x'],
    ['x', 11, 18, 'x', 'x', 'x', 3, 8, 'x']
]

# Define the start and end points
start = (5, 7)
end = (2, 1)

# Define the directions
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Define the BFS function
def bfs(start, end):
    queue = deque([([start], 0, {1: False, 2: False, 3: False})])
    while queue:
        path, time, districts = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and city_map[nx][ny] != 'x':
                new_districts = districts.copy()
                if 0 <= nx <= 2:
                    new_districts[1] = True
                elif 3 <= nx <= 4:
                    new_districts[2] = True
                elif 5 <= nx <= 8:
                    new_districts[3] = True
                if all(new_districts.values()):
                    if (nx, ny) == end:
                        return path + [(nx, ny)]
                else:
                    queue.append((path + [(nx, ny)], time + city_map[nx][ny], new_districts))

# Print the quickest route
print(bfs(start, end))
