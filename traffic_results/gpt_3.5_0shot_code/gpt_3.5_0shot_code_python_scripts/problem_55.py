
from collections import deque

# Define the matrix map of the city
city_map = [
    [9, 4, 16, 7, 'x', 2, 'x', 'x', 14, 'x', 'x', 'x'],
    ['x', 15, 10, 5, 12, 16, 'x', 'x', 'x', 3, 12, 18],
    [12, 'x', 'x', 'x', 9, 16, 3, 9, 'x', 'x', 'x', 7],
    [10, 6, 3, 10, 'x', 'x', 1, 17, 'x', 12, 12, 'x'],
    [11, 8, 15, 'x', 8, 16, 'x', 'x', 5, 15, 12, 7],
    ['x', 'x', 'x', 'x', 6, 'x', 11, 19, 17, 17, 10, 20],
    ['x', 3, 17, 17, 'x', 'x', 18, 4, 'x', 'x', 9, 4],
    ['x', 1, 5, 17, 8, 15, 4, 17, 5, 6, 9, 11],
    ['x', 'x', 4, 5, 17, 18, 3, 'x', 9, 1, 11, 2],
    ['x', 'x', 5, 3, 4, 14, 14, 1, 17, 3, 12, 12],
    ['x', 15, 9, 7, 3, 'x', 'x', 'x', 'x', 'x', 17, 'x'],
    ['x', 'x', 13, 16, 6, 'x', 6, 'x', 'x', 'x', 'x', 'x']
]

# Define the districts
districts = {
    1: (0, 3),
    2: (4, 8),
    3: (9, 11)
}

# Define the start and end workshops
start_workshop = (3, 9)
end_workshop = (7, 1)

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

# Find the shortest path that satisfies the conditions
shortest_path = None
for district in districts.values():
    for i in range(district[0], district[1] + 1):
        path1 = bfs(start_workshop, (i, 0))
        path2 = bfs((i, 0), end_workshop)
        
        if path1 and path2:
            path = path1 + path2[1:]
            if shortest_path is None or len(path) < len(shortest_path):
                shortest_path = path

# Print the shortest path
print(shortest_path)
