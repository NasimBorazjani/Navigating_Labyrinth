
from collections import deque

# Define the city map
city_map = [
    ['x', 9, 4, 8, 'x', 'x', 4, 'x', 8, 12, 'x', 'x', 14],
    [17, 'x', 3, 'x', 6, 'x', 12, 2, 'x', 'x', 'x', 5, 19],
    ['x', 8, 8, 'x', 5, 'x', 15, 14, 14, 3, 10, 12, 3],
    [4, 'x', 16, 'x', 'x', 11, 12, 'x', 'x', 6, 5, 18, 19],
    ['x', 4, 9, 17, 'x', 'x', 'x', 13, 4, 7, 'x', 2, 16],
    [3, 6, 'x', 'x', 'x', 10, 5, 'x', 18, 10, 9, 20, 4],
    ['x', 'x', 'x', 14, 18, 'x', 'x', 'x', 'x', 16, 'x', 'x', 4],
    [14, 12, 'x', 4, 12, 11, 19, 'x', 3, 2, 'x', 13, 'x'],
    [19, 6, 2, 18, 'x', 'x', 8, 7, 1, 12, 19, 'x', 'x'],
    ['x', 9, 16, 17, 5, 12, 19, 8, 'x', 3, 10, 'x', 'x'],
    ['x', 10, 3, 'x', 14, 16, 2, 16, 4, 10, 18, 15, 'x'],
    [15, 5, 5, 'x', 13, 'x', 3, 7, 'x', 4, 1, 17, 15],
    [5, 2, 6, 'x', 'x', 'x', 'x', 8, 16, 'x', 'x', 'x', 'x']
]

# Define the start and end points
start = (7, 1)
end = (2, 10)

# Define the districts
districts = [(0, 2), (3, 7), (8, 12)]

# Define the BFS function
def bfs(start, end, city_map, districts):
    queue = deque([(start, [start], set([get_district(start, districts)]))])
    while queue:
        (x, y), path, visited_districts = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and
                city_map[nx][ny] != 'x' and (nx, ny) not in path):
                new_path = path + [(nx, ny)]
                new_visited_districts = visited_districts | set([get_district((nx, ny), districts)])
                if (nx, ny) == end and len(new_visited_districts) == len(districts):
                    return new_path
                queue.append(((nx, ny), new_path, new_visited_districts))

# Define the function to get the district of a point
def get_district(point, districts):
    x, y = point
    for i, (start, end) in enumerate(districts):
        if start <= x <= end:
            return i

# Print the quickest route
print(bfs(start, end, city_map, districts))
