
from collections import deque

# Define the matrix map of the city
city_map = [
    [13, 'x', 10, 17, 'x', 4, 8, 'x', 7, 'x', 12, 19, 4],
    [17, 'x', 8, 11, 7, 'x', 'x', 19, 'x', 11, 'x', 13, 18],
    [15, 6, 2, 12, 16, 7, 'x', 14, 'x', 2, 'x', 14, 4],
    ['x', 18, 4, 'x', 'x', 'x', 13, 14, 2, 4, 20, 10, 7],
    [7, 2, 19, 16, 'x', 'x', 'x', 18, 'x', 'x', 'x', 2, 2],
    [10, 17, 14, 7, 17, 3, 3, 19, 'x', 19, 'x', 'x', 9],
    [9, 'x', 'x', 'x', 5, 18, 13, 6, 'x', 'x', 'x', 19, 10],
    ['x', 'x', 'x', 'x', 'x', 2, 7, 4, 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 6, 3, 'x', 1, 'x', 'x', 14, 'x', 18, 'x', 1],
    [14, 'x', 4, 18, 14, 12, 'x', 'x', 'x', 'x', 2, 'x', 13],
    [12, 'x', 3, 1, 12, 9, 'x', 6, 'x', 'x', 16, 'x', 18],
    [13, 'x', 11, 5, 3, 4, 'x', 'x', 'x', 'x', 'x', 'x', 18],
    [15, 9, 9, 1, 'x', 6, 'x', 'x', 14, 'x', 'x', 1, 14]
]

# Define the districts
districts = {
    1: [(0, 0), (0, 1)],
    2: [(2, 0), (5, 12)],
    3: [(6, 0), (12, 12)]
}

# Define the start and end workshops
start = (5, 1)
end = (2, 11)

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
    
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = row + dr, col + dc
        
        if 0 <= new_row < len(city_map) and 0 <= new_col < len(city_map[0]) and city_map[new_row][new_col] != 'x':
            neighbors.append((new_row, new_col))
    
    return neighbors

# Find the shortest path while visiting at least one workshop in each district
path = None
for district in districts.values():
    for workshop in district:
        temp_path = bfs(start, workshop)
        
        if temp_path:
            temp_path += bfs(workshop, end)[1:]
            
            if path is None or len(temp_path) < len(path):
                path = temp_path

print(path)
