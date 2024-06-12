
import numpy as np

# Define the matrix map of the city
city_map = np.array([[8, 0, 4, 7, 10, 0, 12, 5, 0],
                      [0, 0, 4, 11, 16, 4, 12, 15, 0],
                      [3, 0, 16, 16, 4, 0, 0, 0, 0],
                      [11, 6, 3, 12, 8, 2, 19, 14, 0],
                      [20, 18, 19, 0, 4, 18, 0, 15, 13],
                      [8, 15, 0, 16, 11, 0, 10, 14, 1],
                      [0, 0, 0, 19, 0, 0, 0, 0, 0],
                      [7, 0, 0, 0, 0, 0, 1, 7, 8],
                      [15, 3, 0, 0, 0, 0, 0, 0, 0]])

# Define the districts
districts = {1: (0, 3), 2: (4, 4), 3: (5, 8)}

# Define the start and end workshops
start_workshop = (5, 0)
end_workshop = (3, 7)

# Function to find the shortest path using breadth-first search
def shortest_path(city_map, start, end, districts):
    queue = [(start, [start], set())]
    
    while queue:
        current, path, visited = queue.pop(0)
        
        if current == end:
            return path
        
        visited.add(current)
        
        for neighbor in [(current[0]+1, current[1]), (current[0]-1, current[1]), 
                         (current[0], current[1]+1), (current[0], current[1]-1)]:
            if 0 <= neighbor[0] < city_map.shape[0] and 0 <= neighbor[1] < city_map.shape[1] and city_map[neighbor] != 0 and neighbor not in visited:
                district = get_district(neighbor, districts)
                if district not in [get_district(p, districts) for p in path]:
                    queue.append((neighbor, path + [neighbor], visited.copy()))
    
    return None

# Function to get the district of a workshop
def get_district(workshop, districts):
    for district, (start, end) in districts.items():
        if start <= workshop[0] <= end:
            return district

# Find the shortest path
path = shortest_path(city_map, start_workshop, end_workshop, districts)

print(path)
