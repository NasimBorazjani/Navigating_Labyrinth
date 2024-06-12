
from collections import deque

# Define the city map
city_map = [
    ['x', 'x', 'x', 'x', 'x', 8, 'x', 15, 18, 10],
    [4, 5, 10, 6, 20, 2, 12, 'x', 'x', 'x'],
    [19, 6, 19, 7, 6, 2, 'x', 15, 'x', 14],
    [16, 17, 'x', 2, 3, 7, 4, 'x', 18, 6],
    ['x', 2, 1, 19, 7, 10, 18, 5, 3, 19],
    [8, 5, 'x', 1, 'x', 10, 17, 'x', 13, 5],
    [18, 1, 3, 4, 'x', 'x', 8, 'x', 5, 'x'],
    [15, 'x', 'x', 13, 'x', 11, 'x', 2, 'x', 'x'],
    [4, 'x', 'x', 4, 1, 'x', 'x', 'x', 'x', 'x'],
    ['x', 10, 8, 'x', 'x', 7, 19, 'x', 'x', 'x']
]

# Define the start and end points
start = (5, 8)
end = (3, 0)

# Define the districts
districts = [(0, 2), (3, 4), (5, 9)]

# Define the BFS function
def bfs(start, end, city_map, districts):
    queue = deque([(start, [start], [start[0] // 3])])
    while queue:
        (x, y), path, visited_districts = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and
                city_map[nx][ny] != 'x' and (nx, ny) not in path):
                new_path = path + [(nx, ny)]
                new_visited_districts = visited_districts + [nx // 3]
                if (nx, ny) == end and set(new_visited_districts) == set(range(3)):
                    return new_path
                queue.append(((nx, ny), new_path, new_visited_districts))

# Print the quickest route
print(bfs(start, end, city_map, districts))
