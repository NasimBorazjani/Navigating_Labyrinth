
from collections import deque

# Define the city map
city_map = [
    [15, 'x', 8, 'x', 6, 9, 'x', 'x', 'x', 'x'],
    [14, 'x', 8, 'x', 14, 'x', 5, 11, 'x', 9],
    ['x', 17, 8, 'x', 17, 15, 12, 'x', 'x', 13],
    ['x', 13, 'x', 'x', 2, 'x', 17, 17, 1, 'x'],
    [6, 'x', 1, 5, 17, 'x', 2, 18, 11, 7],
    [12, 8, 17, 10, 'x', 'x', 'x', 15, 'x', 16],
    [12, 12, 'x', 4, 'x', 13, 'x', 10, 'x', 16],
    ['x', 'x', 10, 'x', 6, 'x', 'x', 'x', 8, 5],
    ['x', 2, 11, 18, 15, 'x', 11, 'x', 'x', 12],
    ['x', 'x', 14, 'x', 'x', 7, 14, 15, 18, 9]
]

# Define the start and end points
start = (5, 0)
end = (3, 8)

# Define the districts
districts = [(0, 3), (4, 4), (5, 9)]

# Define the BFS function
def bfs(start, end, city_map, districts):
    queue = deque([(start, [start], [start[0]//4])])
    while queue:
        (x, y), path, visited_districts = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < 10 and 0 <= ny < 10 and city_map[nx][ny] != 'x' and
                (nx, ny) not in path and len(set(visited_districts + [nx//4])) == 3):
                if (nx, ny) == end:
                    return path + [(nx, ny)]
                queue.append(((nx, ny), path + [(nx, ny)], visited_districts + [nx//4]))

# Call the BFS function
print(bfs(start, end, city_map, districts))
