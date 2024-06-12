
from collections import deque

# Define the city map
city_map = [
    [11, 'x', 'x', 'x', 15, 5, 18, 4, 1, 17, 14, 'x', 9],
    ['x', 10, 10, 7, 12, 12, 6, 'x', 'x', 8, 4, 19, 11],
    [17, 'x', 'x', 12, 8, 'x', 'x', 'x', 14, 19, 'x', 18, 16],
    [17, 'x', 16, 'x', 'x', 17, 4, 'x', 15, 'x', 'x', 'x', 17],
    [17, 'x', 'x', 6, 'x', 'x', 12, 6, 10, 3, 11, 'x', 19],
    [10, 'x', 9, 15, 17, 4, 'x', 'x', 'x', 'x', 14, 17, 18],
    [4, 'x', 'x', 'x', 'x', 13, 18, 13, 'x', 17, 12, 'x', 19],
    ['x', 2, 11, 7, 6, 14, 9, 'x', 12, 17, 9, 13, 14],
    ['x', 18, 16, 'x', 'x', 'x', 11, 6, 12, 'x', 'x', 10, 'x'],
    [5, 3, 'x', 'x', 'x', 5, 'x', 14, 'x', 'x', 'x', 'x', 'x'],
    [18, 'x', 'x', 'x', 'x', 14, 'x', 'x', 13, 1, 3, 'x', 'x'],
    [1, 16, 10, 'x', 'x', 14, 13, 'x', 10, 'x', 1, 'x', 18],
    [8, 'x', 'x', 10, 2, 10, 'x', 'x', 'x', 'x', 'x', 13, 5]
]

# Define the start and end points
start = (8, 11)
end = (2, 3)

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
