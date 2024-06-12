
import numpy as np

# Define the matrix map of the city
city_map = np.array([[12, 17, 10, -1, -1, -1, -1, 9, 15, 5, -1, -1],
                      [-1, -1, -1, -1, -1, 12, 20, 9, 19, 8, 12, 11],
                      [9, -1, -1, 2, -1, 2, 1, 9, 8, 14, 16, -1],
                      [19, -1, 1, 20, 7, 9, 18, -1, 18, 7, -1, -1],
                      [5, 2, 11, 9, -1, 5, 4, 16, -1, 1, -1, 10],
                      [10, 8, 8, 4, 11, 11, -1, -1, 5, -1, -1, -1],
                      [15, 15, -1, -1, 13, 5, 19, -1, -1, 15, -1, -1],
                      [15, 16, 9, 18, -1, -1, 16, -1, -1, -1, 5, 12],
                      [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                      [-1, -1, 14, 14, -1, -1, 15, 6, 6, -1, -1, -1],
                      [-1, -1, -1, -1, -1, 8, 14, -1, 5, -1, -1, 15],
                      [x, 6, 15, -1, -1, -1, -1, -1, -1, 8, -1, -1]])

# Define the districts
districts = {1: range(0, 4), 2: range(4, 7), 3: range(7, 12)}

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
            if 0 <= new_position[0] < len(city_map) and 0 <= new_position[1] < len(city_map[0]) and city_map[new_position[0], new_position[1]] != -1 and new_position not in visited:
                new_path = path + [new_position]
                queue.append((new_position, new_path))
    
    return None

# Find the shortest path that satisfies the conditions
start_workshop = (3, 9)
end_workshop = (7, 1)
shortest_path = None

for district1 in districts[1]:
    for district2 in districts[2]:
        for district3 in districts[3]:
            path1 = shortest_path(start_workshop, (district1, 0))
            path2 = shortest_path((district1, 0), (district2, 0))
            path3 = shortest_path((district2, 0), (district3, 0))
            path4 = shortest_path((district3, 0), end_workshop)
            
            if path1 and path2 and path3 and path4:
                shortest_path = path1 + path2[1:] + path3[1:] + path4[1:]
                break

if shortest_path:
    print(shortest_path)
else:
    print("No valid path found")
