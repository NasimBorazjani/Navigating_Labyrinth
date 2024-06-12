
from collections import deque

# Define the city map
city_map = [
    ['x', 12, 'x', 'x', 'x', 5, 9, 14, 6, 'x', 3, 14, 'x'],
    ['x', 'x', 3, 'x', 11, 'x', 13, 'x', 'x', 'x', 'x', 9, 8],
    ['x', 18, 'x', 'x', 'x', 13, 4, 5, 'x', 'x', 'x', 13, 'x'],
    [10, 4, 'x', 'x', 'x', 'x', 'x', 18, 'x', 15, 'x', 'x', 'x'],
    ['x', 1, 7, 'x', 7, 6, 'x', 3, 'x', 2, 'x', 'x', 5],
    ['x', 15, 5, 'x', 'x', 10, 'x', 19, 'x', 'x', 'x', 10, 6],
    ['x', 18, 1, 2, 'x', 7, 16, 19, 'x', 'x', 10, 8, 8],
    [8, 'x', 'x', 6, 2, 'x', 'x', 'x', 7, 11, 5, 11, 2],
    ['x', 4, 1, 1, 5, 12, 3, 6, 2, 1, 'x', 3, 8],
    ['x', 'x', 5, 5, 14, 15, 7, 'x', 'x', 11, 'x', 7, 9],
    ['x', 6, 12, 16, 17, 'x', 'x', 4, 'x', 19, 9, 5, 'x'],
    [12, 'x', 4, 'x', 8, 4, 'x', 5, 'x', 'x', 'x', 5, 'x'],
    ['x', 5, 'x', 'x', 'x', 'x', 'x', 7, 'x', 'x', 11, 'x', 'x']
]

# Define the start and end points
start = (6, 12)
end = (4, 1)

# Define the districts
districts = [(0, 4), (5, 5), (6, 12)]

# Define the BFS function
def bfs(start, end, city_map, districts):
    queue = deque([(start, [start], {get_district(start, districts)})])
    while queue:
        (x, y), path, visited_districts = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and
                city_map[nx][ny] != 'x' and (nx, ny) not in path):
                if (nx, ny) == end and len(visited_districts | {get_district((nx, ny), districts)}) == len(districts):
                    return path + [(nx, ny)]
                queue.append(((nx, ny), path + [(nx, ny)], visited_districts | {get_district((nx, ny), districts)}))

# Define the function to get the district of a point
def get_district(point, districts):
    x, y = point
    for i, (start, end) in enumerate(districts):
        if start <= x <= end:
            return i

# Print the quickest route
print(bfs(start, end, city_map, districts))
