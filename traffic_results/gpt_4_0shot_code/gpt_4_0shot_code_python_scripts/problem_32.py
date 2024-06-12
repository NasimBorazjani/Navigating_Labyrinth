
from collections import deque

# Define the city map
city_map = [
    ['x', 'x', 13, 'x', 'x', 7, 'x', 13, 3, 'x', 13],
    [10, 4, 'x', 4, 12, 2, 'x', 3, 4, 'x', 15],
    ['x', 3, 'x', 'x', 15, 9, 'x', 'x', 18, 17, 14],
    [5, 'x', 'x', 'x', 3, 'x', 11, 'x', 17, 9, 17],
    [8, 3, 13, 'x', 5, 7, 8, 17, 7, 'x', 'x'],
    ['x', 'x', 13, 2, 2, 11, 6, 8, 'x', 'x', 'x'],
    ['x', 1, 9, 6, 5, 13, 16, 1, 7, 5, 'x'],
    [4, 'x', 13, 'x', 10, 18, 3, 'x', 'x', 19, 19],
    ['x', 'x', 'x', 2, 5, 9, 13, 'x', 7, 1, 'x'],
    ['x', 'x', 7, 'x', 'x', 5, 19, 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 6, 'x', 19, 'x', 'x', 'x', 'x', 1]
]

# Define the start and end points
start = (5, 2)
end = (2, 10)

# Define the districts
districts = [(0, 2), (3, 4), (5, 10)]

# Define the BFS function
def bfs(start, end, city_map, districts):
    queue = deque([(start, [start], set([1 if start[0] <= districts[1][1] else 2 if start[0] <= districts[2][1] else 3]))])
    while queue:
        (x, y), path, visited_districts = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and city_map[nx][ny] != 'x'):
                if (nx, ny) == end and len(visited_districts.union(set([1 if nx <= districts[1][1] else 2 if nx <= districts[2][1] else 3]))) == 3:
                    return path + [(nx, ny)]
                else:
                    queue.append(((nx, ny), path + [(nx, ny)], visited_districts.union(set([1 if nx <= districts[1][1] else 2 if nx <= districts[2][1] else 3]))))

# Call the BFS function
print(bfs(start, end, city_map, districts))
