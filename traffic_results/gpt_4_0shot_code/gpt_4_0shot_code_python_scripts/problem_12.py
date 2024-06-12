
from collections import deque

# Define the city map
city_map = [
    [19, 'x', 17, 14, 3, 'x', 10, 5, 2],
    ['x', 'x', 1, 'x', 'x', 'x', 19, 7, 1],
    [16, 12, 'x', 3, 19, 2, 14, 1, 14],
    ['x', 1, 16, 'x', 12, 3, 13, 'x', 3],
    ['x', 'x', 7, 19, 10, 'x', 5, 'x', 19],
    [5, 'x', 'x', 6, 14, 'x', 'x', 10, 12],
    ['x', 'x', 'x', 'x', 18, 'x', 'x', 15, 12],
    ['x', 'x', 16, 8, 'x', 3, 4, 'x', 'x'],
    ['x', 'x', 'x', 16, 'x', 'x', 8, 14, 7]
]

# Define the start and end points
start = (3, 1)
end = (5, 8)

# Define the districts
districts = [(0, 3), (4, 4), (5, 8)]

# Define the BFS function
def bfs(start, end, city_map, districts):
    queue = deque([(start, [start], {start[0]})])
    while queue:
        (x, y), path, visited_districts = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and
                city_map[nx][ny] != 'x' and (nx, ny) not in path):
                new_path = path + [(nx, ny)]
                new_visited_districts = visited_districts | {nx}
                if (nx, ny) == end and all(district in new_visited_districts for district, _ in districts):
                    return new_path
                queue.append(((nx, ny), new_path, new_visited_districts))

# Call the BFS function
path = bfs(start, end, city_map, districts)
print(path)
