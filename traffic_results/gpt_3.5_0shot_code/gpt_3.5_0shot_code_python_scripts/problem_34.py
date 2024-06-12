
import numpy as np

# Define the matrix map of the city
city_map = np.array([[12, 11, 14, 10, 2, 11, 13, 16, 3, -1, 12],
                      [10, 9, -1, 8, -1, -1, 1, 16, 11, -1, 15],
                      [1, 18, 1, -1, -1, -1, -1, -1, 12, 9, -1],
                      [1, 14, 15, 10, 7, 15, 17, 10, 15, 15, 6],
                      [18, 11, -1, -1, -1, 15, -1, -1, 1, 1, -1],
                      [14, -1, -1, -1, 18, 14, 16, 7, -1, 1, -1],
                      [11, 15, -1, -1, 15, 3, 11, 13, -1, -1, -1],
                      [5, -1, -1, -1, -1, -1, 15, -1, 6, -1, -1],
                      [12, 11, 7, 2, 11, -1, 10, 2, 17, -1, -1],
                      [7, -1, -1, -1, 4, -1, 4, -1, -1, 5, -1],
                      [-1, 19, 10, 7, -1, 2, 3, 9, 2, 6, -1]])

# Define the districts
districts = {1: [0, 1, 2], 2: [3, 4, 5, 6], 3: [7, 8, 9, 10]}

# Define the destination workshop
destination = (2, 9)

# Function to find the shortest path using breadth-first search
def find_shortest_path(start, end, city_map, districts):
    queue = [(start, [start])]
    visited = set()
    
    while queue:
        current, path = queue.pop(0)
        visited.add(current)
        
        if current == end:
            return path
        
        for neighbor in get_neighbors(current, city_map, districts):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return None

# Function to get valid neighbors of a workshop
def get_neighbors(workshop, city_map, districts):
    neighbors = []
    row, col = workshop
    
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = row + dr, col + dc
        
        if 0 <= new_row < city_map.shape[0] and 0 <= new_col < city_map.shape[1] and city_map[new_row, new_col] != -1:
            district = get_district(new_row, districts)
            if district not in [get_district(workshop, districts), get_district((new_row, new_col), districts)]:
                neighbors.append((new_row, new_col))
    
    return neighbors

# Function to get the district of a workshop
def get_district(workshop, districts):
    for district, workshops in districts.items():
        if workshop in workshops:
            return district

# Find the shortest path from Ben's current workshop to the destination
start = (7, 0)
path = find_shortest_path(start, destination, city_map, districts)

print(path)
