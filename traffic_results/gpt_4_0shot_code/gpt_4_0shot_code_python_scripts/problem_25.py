
from collections import deque

# Define the city map
city_map = [
    ['x', 'x', 6, 'x', 'x', 'x', 'x', 15, 'x', 'x'],
    ['x', 17, 13, 13, 'x', 12, 'x', 3, 10, 2],
    ['x', 5, 13, 15, 4, 'x', 'x', 20, 6, 2],
    ['x', 9, 'x', 6, 2, 16, 18, 9, 13, 'x'],
    ['x', 'x', 15, 17, 'x', 10, 11, 'x', 'x', 'x'],
    [3, 'x', 3, 17, 8, 'x', 1, 'x', 16, 'x'],
    ['x', 'x', 13, 15, 'x', 'x', 11, 'x', 'x', 4],
    ['x', 'x', 12, 1, 'x', 'x', 'x', 14, 11, 'x'],
    ['x', 14, 'x', 'x', 19, 13, 4, 'x', 'x', 'x'],
    [1, 'x', 'x', 14, 11, 19, 2, 17, 2, 5]
]

# Define the start and end points
start = (2, 9)
end = (5, 2)

# Define the directions
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Define the BFS function
def bfs(start, end):
    queue = deque([([start], 0, {1, 2, 3})])
    visited = set([start])
    while queue:
        path, time, districts = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) not in visited and city_map[nx][ny] != 'x':
                new_districts = districts - {get_district(nx)}
                if not new_districts or (nx, ny) == end:
                    queue.append((path + [(nx, ny)], time + city_map[nx][ny], new_districts))
                    visited.add((nx, ny))

# Define the function to get the district
def get_district(x):
    if x < 3:
        return 1
    elif x < 5:
        return 2
    else:
        return 3

# Print the path
print(bfs(start, end))
