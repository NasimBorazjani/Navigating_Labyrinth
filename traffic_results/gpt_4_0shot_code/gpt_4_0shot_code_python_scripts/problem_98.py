
from collections import deque

# Define the city map
city_map = [
    ['x', 19, 4, 'x', 17, 11, 'x', 'x', 18, 7, 'x', 8, 20, 'x', 1],
    ['x', 16, 'x', 1, 9, 1, 'x', 8, 16, 'x', 15, 7, 1, 'x', 'x'],
    [7, 'x', 9, 9, 9, 'x', 18, 'x', 15, 13, 10, 'x', 19, 16, 9],
    ['x', 'x', 'x', 6, 'x', 'x', 7, 10, 18, 17, 'x', 8, 9, 6, 5],
    [4, 17, 'x', 'x', 19, 5, 20, 1, 15, 18, 'x', 'x', 5, 8, 2],
    ['x', 'x', 'x', 3, 10, 19, 17, 20, 'x', 'x', 'x', 3, 'x', 5, 'x'],
    ['x', 'x', 'x', 3, 8, 2, 'x', 'x', 7, 19, 'x', 'x', 1, 19, 9],
    ['x', 19, 16, 6, 5, 19, 'x', 'x', 'x', 12, 'x', 3, 8, 10, 'x'],
    [13, 2, 'x', 18, 'x', 'x', 5, 'x', 'x', 'x', 13, 1, 'x', 'x', 6],
    [19, 8, 8, 10, 'x', 'x', 'x', 12, 14, 5, 14, 2, 6, 'x', 'x'],
    ['x', 'x', 'x', 12, 18, 'x', 'x', 'x', 'x', 'x', 'x', 16, 'x', 19, 'x'],
    [11, 'x', 12, 'x', 'x', 5, 'x', 15, 8, 'x', 9, 'x', 'x', 'x', 'x'],
    [9, 'x', 4, 'x', 'x', 'x', 'x', 2, 18, 'x', 11, 'x', 11, 'x', 19],
    [13, 'x', 17, 1, 'x', 14, 'x', 'x', 'x', 'x', 16, 'x', 2, 'x', 'x'],
    [3, 16, 'x', 'x', 3, 11, 'x', 15, 'x', 'x', 'x', 'x', 'x', 16, 'x']
]

# Define the start and end points
start = (9, 3)
end = (4, 14)

# Define the directions
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Define the BFS function
def bfs(start, end):
    queue = deque([([start], 0, {1, 2, 3})])
    while queue:
        path, time, districts = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 15 and 0 <= ny < 15 and city_map[nx][ny] != 'x':
                new_time = time + city_map[nx][ny]
                new_districts = districts - {get_district(nx)}
                if not new_districts:
                    queue.append((path + [(nx, ny)], new_time, new_districts))

# Define the function to get the district
def get_district(row):
    if row < 4:
        return 1
    elif row < 9:
        return 2
    else:
        return 3

# Print the quickest route
print(bfs(start, end))
