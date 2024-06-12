
from collections import deque

# Define the city map
city_map = [
    [7, 6, 11, 'x', 'x', 'x', 19, 'x', 9, 15, 12, 8, 10, 15, 5],
    [9, 14, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 18, 2, 11, 'x', 10],
    [14, 5, 'x', 'x', 4, 4, 12, 'x', 18, 'x', 17, 11, 3, 18, 19],
    [18, 17, 'x', 8, 'x', 'x', 9, 'x', 'x', 8, 19, 10, 'x', 'x', 'x'],
    [7, 'x', 'x', 11, 4, 'x', 'x', 10, 1, 2, 3, 12, 8, 12, 15],
    ['x', 3, 7, 8, 'x', 'x', 'x', 'x', 4, 16, 13, 19, 14, 10, 13],
    [18, 1, 2, 'x', 16, 20, 5, 'x', 2, 4, 20, 12, 14, 18, 16],
    [1, 'x', 1, 'x', 15, 19, 11, 9, 19, 16, 'x', 'x', 'x', 'x', 19],
    ['x', 8, 'x', 1, 7, 'x', 2, 3, 'x', 'x', 'x', 'x', 1, 3, 'x'],
    [6, 16, 'x', 3, 'x', 18, 'x', 2, 18, 'x', 'x', 16, 'x', 'x', 8],
    ['x', 9, 'x', 5, 2, 'x', 'x', 'x', 'x', 17, 'x', 6, 18, 14, 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 18, 'x', 'x', 3, 'x', 10, 'x', 'x'],
    ['x', 2, 15, 'x', 5, 15, 18, 8, 19, 'x', 'x', 'x', 'x', 'x', 10],
    ['x', 'x', 4, 'x', 7, 2, 2, 'x', 19, 'x', 'x', 'x', 'x', 'x', 'x'],
    [17, 'x', 'x', 'x', 5, 'x', 'x', 'x', 4, 1, 18, 'x', 9, 2, 8]
]

# Define the start and end points
start = (4, 14)
end = (8, 3)

# Define the directions
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Define the BFS function
def bfs(start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        (x, y), path = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(city_map) and 0 <= ny < len(city_map[0]) and
                city_map[nx][ny] != 'x' and (nx, ny) not in visited):
                if (nx, ny) == end:
                    return path + [(nx, ny)]
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    return None

# Print the quickest route
print(bfs(start, end))
