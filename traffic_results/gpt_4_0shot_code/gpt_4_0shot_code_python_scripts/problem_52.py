
from collections import deque

# Define the matrix map
matrix_map = [
    ['x', 3, 11, 7, 'x', 'x', 1, 3, 'x', 'x', 'x', 3],
    ['x', 10, 'x', 'x', 3, 9, 7, 8, 'x', 2, 'x', 17],
    [6, 16, 'x', 18, 10, 5, 'x', 6, 'x', 'x', 7, 'x'],
    ['x', 10, 'x', 8, 13, 10, 'x', 'x', 'x', 'x', 6, 13],
    [6, 11, 3, 16, 8, 15, 'x', 'x', 'x', 13, 12, 20],
    [15, 'x', 16, 'x', 17, 13, 'x', 'x', 8, 6, 19, 9],
    [14, 10, 16, 14, 'x', 'x', 10, 11, 19, 15, 17, 'x'],
    ['x', 'x', 'x', 'x', 18, 13, 14, 19, 12, 1, 3, 'x'],
    [15, 1, 3, 17, 4, 18, 'x', 18, 2, 7, 12, 'x'],
    [19, 'x', 13, 17, 2, 14, 8, 'x', 'x', 8, 16, 'x'],
    ['x', 19, 'x', 15, 'x', 18, 'x', 13, 'x', 13, 'x', 'x'],
    [7, 14, 2, 'x', 10, 3, 'x', 'x', 2, 5, 10, 'x']
]

# Define the start and end workshops
start = (8, 1)
end = (5, 11)

# Define the districts
districts = [(0, 4), (5, 8), (9, 11)]

# Define the directions
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Define the BFS algorithm
def bfs(matrix_map, start, end, districts, directions):
    queue = deque([(start, [start], [0, 0, 0])])
    visited = set([start])
    while queue:
        (x, y), path, district_visited = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix_map) and 0 <= ny < len(matrix_map[0]) and matrix_map[nx][ny] != 'x' and (nx, ny) not in visited:
                new_path = path + [(nx, ny)]
                new_district_visited = district_visited[:]
                for i, (start, end) in enumerate(districts):
                    if start <= nx <= end:
                        new_district_visited[i] = 1
                if (nx, ny) == end and all(new_district_visited):
                    return new_path
                queue.append(((nx, ny), new_path, new_district_visited))
                visited.add((nx, ny))
    return None

# Find the shortest path
shortest_path = bfs(matrix_map, start, end, districts, directions)
print(shortest_path)
