
import numpy as np

# Define the matrix map of the city
city_map = np.array([[0, 0, 0, 0, 9, 1, 14, 0, 0, 0, 11, 15, 12],
                     [2, 0, 18, 0, 14, 0, 11, 3, 0, 0, 0, 0, 0],
                     [10, 0, 3, 0, 0, 0, 8, 6, 0, 10, 9, 7, 0],
                     [1, 18, 2, 6, 0, 0, 1, 5, 0, 0, 6, 0, 0],
                     [4, 14, 12, 3, 2, 2, 15, 8, 19, 3, 18, 0, 0],
                     [5, 6, 2, 2, 13, 0, 7, 3, 12, 0, 16, 10, 5],
                     [0, 2, 13, 0, 0, 9, 5, 0, 0, 0, 7, 10, 11],
                     [17, 10, 3, 11, 4, 0, 0, 19, 0, 5, 0, 0, 9],
                     [13, 0, 0, 0, 0, 9, 13, 4, 7, 0, 13, 10, 0],
                     [0, 0, 0, 9, 0, 8, 8, 14, 0, 0, 19, 0, 0],
                     [6, 0, 0, 0, 0, 0, 1, 11, 0, 4, 13, 0, 0],
                     [0, 0, 0, 11, 11, 0, 9, 16, 12, 0, 6, 0, 5],
                     [16, 19, 14, 0, 5, 13, 0, 0, 0, 0, 13, 0, 0]])

# Define the districts
districts = {1: range(0, 4), 2: range(4, 6), 3: range(6, 13)}

# Define the directions Ben can move
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Function to find the shortest path using breadth-first search
def shortest_path(start, end):
    queue = [(start, [start])]
    visited = set()
    
    while queue:
        current, path = queue.pop(0)
        visited.add(current)
        
        if current == end:
            return path
        
        for direction in directions:
            new_position = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= new_position[0] < city_map.shape[0] and 0 <= new_position[1] < city_map.shape[1] and city_map[new_position[0], new_position[1]] != 0 and new_position not in visited:
                new_path = path + [new_position]
                queue.append((new_position, new_path))
    
    return None

# Find the shortest path that satisfies the conditions
start_workshop = (6, 12)
end_workshop = (5, 0)
shortest_path = None

for district in districts.values():
    for workshop in district:
        path_to_district = shortest_path(start_workshop, (workshop, 0))
        if path_to_district:
            remaining_districts = set(districts.keys()) - {key for key, value in districts.items() if workshop in value}
            for next_district in remaining_districts:
                for next_workshop in districts[next_district]:
                    path_to_destination = shortest_path((workshop, 0), (next_workshop, 0))
                    if path_to_destination:
                        final_path = path_to_district + path_to_destination[1:]
                        if shortest_path is None or len(final_path) < len(shortest_path):
                            shortest_path = final_path

print(shortest_path)
