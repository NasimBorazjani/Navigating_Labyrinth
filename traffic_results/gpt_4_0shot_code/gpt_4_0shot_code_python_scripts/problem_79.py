
from collections import deque

# Define the city map
city_map = [
    ['x', 'x', 17, 7, 'x', 'x', 11, 4, 5, 15, 17, 6, 6, 2],
    [17, 'x', 'x', 6, 'x', 'x', 'x', 'x', 1, 8, 'x', 'x', 'x', 7],
    ['x', 'x', 'x', 17, 4, 10, 6, 4, 'x', 8, 16, 11, 'x', 'x'],
    ['x', 4, 'x', 'x', 10, 'x', 8, 10, 'x', 11, 'x', 'x', 1, 'x'],
    ['x', 'x', 11, 9, 4, 'x', 8, 8, 'x', 'x', 'x', 16, 13, 8],
    ['x', 12, 3, 15, 13, 13, 'x', 15, 19, 'x', 2, 2, 6, 'x'],
    [15, 1, 'x', 'x', 'x', 'x', 5, 4, 'x', 5, 12, 2, 5, 'x'],
    [20, 13, 7, 18, 8, 18, 5, 2, 17, 7, 11, 'x', 15, 13],
    [4, 11, 'x', 'x', 10, 9, 'x', 18, 14, 'x', 19, 'x', 'x', 'x'],
    [19, 'x', 2, 'x', 18, 17, 10, 'x', 'x', 'x', 13, 15, 'x', 10],
    [16, 5, 2, 3, 13, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 3],
    ['x', 'x', 'x', 'x', 17, 9, 'x', 'x', 'x', 'x', 'x', 6, 'x', 'x'],
    [11, 'x', 'x', 9, 14, 'x', 'x', 16, 'x', 15, 13, 13, 15, 1],
    [9, 'x', 'x', 10, 14, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 1, 19]
]

# Define the start and end points
start = (4, 12)
end = (7, 0)

# Define the districts
districts = [(0, 4), (5, 6), (7, 13)]

# Define the BFS function
def bfs(start, end, city_map, districts):
    queue = deque([(start, [start], set([1 if start[0] <= districts[0][1] else 2 if start[0] <= districts[1][1] else 3]))])
    while queue:
        (x, y), path, visited_districts = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and city_map[nx][ny] != 'x' and (nx, ny) not in path):
                if (nx, ny) == end and len(visited_districts.union(set([1 if nx <= districts[0][1] else 2 if nx <= districts[1][1] else 3]))) == 3:
                    return path + [(nx, ny)]
                queue.append(((nx, ny), path + [(nx, ny)], visited_districts.union(set([1 if nx <= districts[0][1] else 2 if nx <= districts[1][1] else 3]))))

# Print the quickest route
print(bfs(start, end, city_map, districts))
