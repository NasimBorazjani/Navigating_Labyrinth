
from collections import deque

# Define the city map
city_map = [
    [10, 'x', 'x', 'x', 16, 9, 'x', 13, 12, 8, 'x', 16, 17],
    [9, 2, 'x', 'x', 5, 'x', 'x', 'x', 12, 'x', 3, 'x', 'x'],
    ['x', 'x', 7, 3, 12, 'x', 11, 18, 10, 'x', 'x', 13, 'x'],
    ['x', 6, 'x', 19, 2, 'x', 'x', 11, 13, 13, 1, 'x', 7],
    ['x', 'x', 11, 'x', 16, 16, 4, 12, 5, 20, 2, 4, 15],
    [19, 'x', 18, 5, 11, 'x', 'x', 3, 17, 18, 3, 8, 18],
    [12, 'x', 9, 'x', 'x', 'x', 'x', 9, 4, 15, 16, 'x', 9],
    ['x', 15, 'x', 6, 10, 'x', 1, 1, 'x', 9, 4, 7, 1],
    ['x', 19, 15, 'x', 1, 10, 5, 17, 'x', 8, 'x', 1, 'x'],
    ['x', 'x', 'x', 'x', 5, 'x', 1, 'x', 'x', 7, 4, 'x', 'x'],
    [9, 'x', 4, 'x', 5, 13, 'x', 15, 'x', 'x', 18, 9, 15],
    [17, 2, 'x', 'x', 'x', 18, 8, 'x', 8, 'x', 'x', 8, 7],
    ['x', 'x', 5, 'x', 'x', 8, 'x', 8, 'x', 15, 19, 'x', 'x']
]

# Define the start and end points
start = (3, 12)
end = (7, 3)

# Define the districts
districts = [(0, 3), (4, 6), (7, 12)]

# Define the BFS function
def bfs(start, end, city_map, districts):
    queue = deque([(start, [start], set([1 if start[0] <= districts[0][1] else 2 if start[0] <= districts[1][1] else 3]))])
    while queue:
        (x, y), path, visited_districts = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and city_map[nx][ny] != 'x'):
                if (nx, ny) == end and len(visited_districts | set([1 if nx <= districts[0][1] else 2 if nx <= districts[1][1] else 3])) == 3:
                    return path + [(nx, ny)]
                else:
                    queue.append(((nx, ny), path + [(nx, ny)], visited_districts | set([1 if nx <= districts[0][1] else 2 if nx <= districts[1][1] else 3])))

# Print the quickest route
print(bfs(start, end, city_map, districts))
