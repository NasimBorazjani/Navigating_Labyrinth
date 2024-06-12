
from collections import deque

# Define the matrix map of the city
city_map = [
    ['x', 6, 19, 13, 'x', 16, 11, 6, 14, 15, 7, 'x', 'x', 'x'],
    ['x', 6, 16, 15, 'x', 19, 16, 18, 'x', 8, 10, 'x', 'x', 'x'],
    ['x', 5, 10, 14, 2, 'x', 'x', 'x', 11, 'x', 11, 'x', 'x', 'x'],
    [6, 13, 15, 10, 'x', 'x', 'x', 'x', 19, 'x', 'x', 'x', 2, 'x'],
    ['x', 15, 10, 6, 6, 8, 10, 9, 11, 'x', 'x', 'x', 16, 'x'],
    ['x', 'x', 'x', 8, 15, 12, 10, 19, 1, 18, 19, 4, 'x', 10],
    [1, 17, 'x', 'x', 6, 8, 4, 'x', 15, 8, 10, 6, 4, 'x'],
    ['x', 'x', 'x', 'x', 13, 'x', 5, 'x', 9, 10, 'x', 'x', 'x', 'x'],
    [12, 'x', 11, 'x', 13, 'x', 11, 7, 5, 13, 'x', 'x', 6, 15],
    ['x', 18, 19, 'x', 'x', 'x', 3, 'x', 16, 11, 'x', 15, 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 2, 15, 'x', 'x', 8, 'x', 'x', 'x'],
    [11, 'x', 6, 13, 12, 'x', 12, 'x', 'x', 9, 'x', 17, 'x', 'x'],
    ['x', 1, 'x', 18, 18, 3, 'x', 11, 13, 1, 13, 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 6, 'x', 'x', 8, 'x', 'x', 'x', 4, 11]
]

# Define the districts
districts = {
    1: (0, 2),
    2: (3, 5),
    3: (6, 13)
}

# Define the start and end workshops
start_workshop = (3, 0)
end_workshop = (6, 12)

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
    for row in range(district[0], district[1] + 1):
        for col in range(len(city_map[0]):
            if city_map[row][col] != 'x':
                path = bfs(start_workshop, (row, col))
                if path and (shortest_path is None or len(path) < len(shortest_path)):
                    shortest_path = path

print(shortest_path)
