
from collections import deque

# Define the city map
city_map = [
    ['x', 5, 9, 6, 13, 13, 8, 6, 13, 'x', 13, 'x', 'x', 'x'],
    [3, 10, 16, 'x', 'x', 3, 13, 1, 11, 9, 7, 6, 'x', 18],
    [9, 11, 3, 'x', 'x', 6, 13, 'x', 14, 'x', 12, 1, 2, 4],
    ['x', 17, 13, 'x', 14, 4, 6, 8, 'x', 'x', 1, 'x', 6, 2],
    [7, 'x', 11, 'x', 14, 'x', 11, 7, 'x', 5, 'x', 1, 12, 'x'],
    ['x', 20, 20, 19, 'x', 18, 2, 19, 1, 6, 12, 'x', 'x', 16],
    [8, 5, 7, 11, 'x', 1, 'x', 'x', 'x', 11, 4, 'x', 'x', 3],
    ['x', 11, 'x', 11, 11, 'x', 'x', 18, 'x', 'x', 'x', 7, 6, 'x'],
    [2, 2, 14, 5, 5, 'x', 'x', 11, 19, 16, 'x', 14, 7, 19],
    ['x', 5, 'x', 'x', 7, 'x', 10, 'x', 'x', 'x', 3, 15, 'x', 'x'],
    [19, 'x', 'x', 'x', 'x', 8, 3, 19, 'x', 18, 'x', 'x', 'x', 9],
    [17, 'x', 19, 'x', 'x', 'x', 5, 3, 'x', 'x', 7, 4, 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 12, 11, 'x', 'x', 'x', 'x', 'x', 6, 6],
    ['x', 'x', 'x', 'x', 'x', 'x', 4, 'x', 'x', 'x', 7, 'x', 6, 3]
]

# Define the start and end points
start = (6, 1)
end = (3, 13)

# Define the districts
districts = [(0, 1), (2, 5), (6, 13)]

# Define the BFS function
def bfs(start, end, city_map, districts):
    queue = deque([(start, [start], set([1]))])
    while queue:
        (x, y), path, visited_districts = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and
                city_map[nx][ny] != 'x' and (nx, ny) not in path):
                new_path = path + [(nx, ny)]
                new_visited_districts = visited_districts.copy()
                for i, (d_start, d_end) in enumerate(districts, start=1):
                    if d_start <= nx <= d_end:
                        new_visited_districts.add(i)
                if (nx, ny) == end and len(new_visited_districts) == len(districts):
                    return new_path
                queue.append(((nx, ny), new_path, new_visited_districts))

# Print the quickest route
print(bfs(start, end, city_map, districts))
