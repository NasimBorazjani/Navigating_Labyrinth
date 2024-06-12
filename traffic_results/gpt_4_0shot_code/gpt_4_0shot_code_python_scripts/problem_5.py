
from collections import deque

# Define the city map
city_map = [
    [8, 'x', 4, 7, 10, 'x', 12, 5, 'x'],
    ['x', 'x', 4, 11, 16, 4, 12, 15, 'x'],
    [3, 'x', 16, 16, 4, 'x', 'x', 'x', 'x'],
    [11, 6, 3, 12, 8, 2, 19, 14, 'x'],
    [20, 18, 19, 'x', 4, 18, 'x', 15, 13],
    [8, 15, 'x', 16, 11, 'x', 10, 14, 1],
    ['x', 'x', 'x', 19, 'x', 'x', 'x', 'x', 'x'],
    [7, 'x', 'x', 'x', 'x', 'x', 1, 7, 8],
    [15, 3, 'x', 'x', 'x', 'x', 'x', 'x', 'x']
]

# Define the start and end points
start = (5, 0)
end = (3, 7)

# Define the directions
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Define the BFS function
def bfs(start, end):
    queue = deque([([start], 0)])
    visited = {start}
    while queue:
        path, dist = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and
                (nx, ny) not in visited and city_map[nx][ny] != 'x'):
                queue.append((path + [(nx, ny)], dist + city_map[nx][ny]))
                visited.add((nx, ny))

# Print the quickest route
print(bfs(start, end))
