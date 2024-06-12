
import numpy as np

# Define the matrix map of the city
city_map = np.array([[8, 0, 12, 0, 16, 0, 0, 0, 7, 0, 0, 0, 0],
                     [0, 0, 0, 0, 16, 0, 7, 8, 0, 17, 0, 19, 0],
                     [7, 0, 13, 0, 19, 0, 6, 0, 14, 0, 18, 0, 19],
                     [9, 20, 2, 0, 10, 6, 0, 18, 0, 0, 0, 18, 0],
                     [0, 0, 8, 12, 7, 14, 13, 9, 8, 6, 14, 11, 7],
                     [0, 14, 0, 0, 0, 19, 13, 15, 3, 12, 16, 16, 3],
                     [0, 0, 0, 13, 0, 9, 13, 10, 0, 14, 0, 4, 18],
                     [6, 12, 10, 0, 0, 18, 7, 20, 18, 0, 13, 1, 0],
                     [0, 5, 0, 18, 12, 0, 0, 3, 12, 14, 19, 16, 0],
                     [10, 0, 19, 0, 0, 0, 0, 11, 14, 16, 12, 0, 8],
                     [8, 0, 0, 0, 0, 0, 0, 9, 16, 15, 0, 0, 8],
                     [0, 0, 2, 0, 1, 0, 0, 16, 0, 0, 3, 0, 0],
                     [9, 0, 5, 0, 0, 15, 0, 0, 0, 7, 15, 9, 0]])

# Define the districts
districts = {1: range(0, 4), 2: range(4, 6), 3: range(6, 13)}

# Define the directions Ben can move
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Function to find the shortest path using Breadth First Search
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
                new_path = list(path)
                new_path.append(new_position)
                queue.append((new_position, new_path))
    
    return None

# Find the shortest path that satisfies the conditions
start_workshop = (3, 0)
end_workshop = (6, 12)
path = None

for district1 in districts[1]:
    for district2 in districts[2]:
        for district3 in districts[3]:
            path1 = shortest_path(start_workshop, (district1, 0))
            path2 = shortest_path((district1, 0), (district2, 0))
            path3 = shortest_path((district2, 0), (district3, 0))
            path4 = shortest_path((district3, 0), end_workshop)
            
            if path1 and path2 and path3 and path4:
                path = path1[:-1] + path2[:-1] + path3[:-1] + path4
                break

if path:
    print(path)
else:
    print("No valid path found.")
