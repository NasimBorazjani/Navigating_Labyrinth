
from collections import deque

# Define the matrix map of the city
city_map = [
    [8, 15, 3, 10, 6, 15, 'x', 4, 'x', 'x', 'x', 'x', 'x', 4],
    [3, 'x', 14, 8, 16, 19, 'x', 18, 4, 'x', 2, 'x', 6, 'x'],
    [18, 18, 'x', 4, 'x', 17, 11, 10, 17, 9, 'x', 4, 1, 5],
    ['x', 2, 'x', 12, 1, 'x', 13, 17, 14, 15, 17, 'x', 15, 'x'],
    ['x', 'x', 'x', 15, 'x', 2, 2, 11, 7, 'x', 5, 7, 4, 18],
    [16, 'x', 5, 'x', 19, 12, 5, 9, 13, 16, 9, 'x', 3, 'x'],
    ['x', 'x', 'x', 'x', 14, 18, 'x', 16, 13, 'x', 1, 5, 10, 'x'],
    [3, 11, 'x', 1, 8, 'x', 'x', 'x', 18, 8, 11, 'x', 'x', 6],
    [19, 2, 'x', 19, 5, 'x', 'x', 'x', 9, 'x', 6, 'x', 'x', 4],
    ['x', 2, 'x', 10, 9, 15, 'x', 'x', 'x', 16, 'x', 8, 'x', 'x'],
    [18, 8, 10, 'x', 3, 'x', 11, 'x', 17, 'x', 17, 'x', 'x', 'x'],
    [14, 12, 'x', 2, 'x', 19, 2, 19, 14, 'x', 'x', 'x', 3, 'x'],
    [7, 'x', 'x', 'x', 'x', 'x', 'x', 9, 8, 7, 'x', 15, 2, 'x'],
    ['x', 'x', 15, 'x', 'x', 15, 16, 'x', 'x', 'x', 19, 'x', 13, 1]
]

# Define the districts
districts = {
    1: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
    2: [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
    3: [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2), (10, 0), (10, 1), (10, 2), (11, 0), (11, 1), (11, 2), (12, 0), (12, 1), (12, 2), (13, 0), (13, 1), (13, 2)]
}

# Define the start and end workshops
start_workshop = (2, 0)
end_workshop = (6, 11)

# Perform breadth-first search to find the shortest path
def bfs(start, end):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        current, path = queue.popleft()
        
        if current == end:
            return path
        
        visited.add(current)
        
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return None

# Get valid neighbors of a workshop
def get_neighbors(workshop):
    row, col = workshop
    neighbors = []
    
    if row > 0 and city_map[row - 1][col] != 'x':
        neighbors.append((row - 1, col))
    if row < len(city_map) - 1 and city_map[row + 1][col] != 'x':
        neighbors.append((row + 1, col))
    if col > 0 and city_map[row][col - 1] != 'x':
        neighbors.append((row, col - 1))
    if col < len(city_map[0]) - 1 and city_map[row][col + 1] != 'x':
        neighbors.append((row, col + 1))
    
    return neighbors

# Find the shortest path that satisfies the district requirements
path = None
for district in districts.values():
    for workshop in district:
        if path is None:
            path = bfs(start_workshop, workshop)
        else:
            new_path = bfs(start_workshop, workshop)
            if new_path and len(new_path) < len(path):
                path = new_path

if path:
    path += bfs(path[-1], end_workshop)[1:]
    print(path)
else:
    print("No valid path found")
