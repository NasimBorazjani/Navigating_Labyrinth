
from collections import deque

# Define the city map
city_map = [
    [15, 4, 9, 10, 19, 'x', 12, 4, 'x', 15],
    [12, 19, 11, 'x', 'x', 'x', 'x', 7, 6, 3],
    [4, 'x', 8, 'x', 'x', 19, 'x', 11, 1, 6],
    ['x', 'x', 5, 'x', 'x', 'x', 12, 6, 6, 'x'],
    ['x', 14, 'x', 'x', 14, 11, 2, 9, 6, 14],
    [8, 8, 5, 17, 7, 'x', 1, 2, 'x', 6],
    [18, 'x', 'x', 15, 'x', 15, 4, 'x', 'x', 7],
    [19, 'x', 10, 18, 14, 'x', 14, 9, 8, 6],
    [19, 'x', 14, 'x', 10, 8, 15, 'x', 15, 'x'],
    [12, 1, 'x', 5, 3, 3, 'x', 'x', 'x', 'x']
]

# Define the start and end points
start = (1, 9)
end = (6, 3)

# Define the districts
districts = [(0, 1), (2, 6), (7, 9)]

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
                if (nx, ny) == end and all(d in new_visited_districts for d in range(*districts[0]) + range(*districts[1]) + range(*districts[2])):
                    return new_path
                queue.append(((nx, ny), new_path, new_visited_districts))

# Print the result
print(bfs(start, end, city_map, districts))
