
from collections import deque

# Define the city map
city_map = [
    [5, 15, 15, 5, 6, 19, 'x', 9, 2, 'x', 16, 'x', 15],
    [16, 'x', 'x', 7, 5, 'x', 'x', 'x', 5, 2, 19, 'x', 3],
    ['x', 11, 2, 19, 17, 5, 11, 6, 3, 18, 15, 16, 'x'],
    [2, 'x', 12, 'x', 20, 11, 7, 19, 2, 'x', 4, 14, 'x'],
    [3, 'x', 19, 'x', 11, 19, 'x', 14, 'x', 12, 'x', 18, 7],
    [6, 'x', 5, 8, 3, 12, 12, 11, 5, 14, 'x', 6, 'x'],
    ['x', 'x', 13, 2, 'x', 20, 'x', 'x', 'x', 18, 18, 'x', 3],
    ['x', 'x', 13, 1, 10, 18, 'x', 'x', 'x', 'x', 10, 'x', 15],
    [10, 'x', 9, 2, 17, 19, 16, 8, 'x', 18, 10, 'x', 13],
    ['x', 'x', 2, 8, 2, 7, 'x', 17, 'x', 1, 'x', 9, 'x'],
    ['x', 13, 'x', 19, 15, 3, 15, 13, 1, 12, 4, 7, 'x'],
    [14, 'x', 'x', 'x', 'x', 'x', 'x', 16, 'x', 15, 'x', 'x', 'x'],
    [3, 15, 'x', 6, 'x', 9, 'x', 'x', 9, 1, 6, 'x', 5]
]

# Define the start and end workshops
start = (8, 2)
end = (2, 9)

# Define the districts
districts = [range(0, 3), range(3, 8), range(8, 13)]

# Define the BFS function
def bfs(city_map, start, end, districts):
    queue = deque([(start, [start], set())])
    while queue:
        (x, y), path, visited_districts = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and
                city_map[nx][ny] != 'x' and (nx, ny) not in path):
                new_path = path + [(nx, ny)]
                new_visited_districts = visited_districts.copy()
                for i, district in enumerate(districts):
                    if nx in district:
                        new_visited_districts.add(i)
                if (nx, ny) == end and len(new_visited_districts) == len(districts):
                    return new_path
                queue.append(((nx, ny), new_path, new_visited_districts))

# Print the shortest path
print(bfs(city_map, start, end, districts))
