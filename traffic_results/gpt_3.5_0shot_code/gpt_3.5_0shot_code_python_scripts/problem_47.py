
import numpy as np

# Define the city map as a numpy array
city_map = np.array([[5, 0, 0, 4, 0, 12, 7, 11, 8, 3, 19, 0],
                      [0, 0, 6, 15, 16, 0, 0, 4, 0, 7, 8, 19],
                      [18, 0, 0, 15, 0, 0, 0, 8, 4, 16, 7, 9],
                      [0, 19, 0, 0, 0, 16, 0, 0, 17, 15, 0, 9],
                      [15, 8, 19, 0, 4, 4, 0, 0, 0, 3, 3, 10],
                      [18, 6, 14, 5, 0, 18, 19, 15, 18, 19, 12, 5],
                      [12, 0, 2, 2, 6, 3, 3, 8, 3, 1, 0, 15],
                      [10, 4, 0, 9, 15, 3, 0, 7, 0, 17, 0, 0],
                      [5, 18, 0, 17, 0, 17, 0, 0, 15, 0, 18, 0],
                      [4, 0, 16, 11, 10, 3, 12, 0, 11, 14, 3, 0],
                      [0, 9, 9, 14, 19, 15, 0, 1, 10, 19, 6, 0],
                      [0, 0, 17, 4, 0, 2, 0, 7, 0, 4, 4, 18]])

# Define the closed workshops as a set
closed_workshops = {(0, 1), (0, 2), (0, 5), (0, 11),
                    (1, 0), (1, 1), (1, 5), (1, 6), (1, 8),
                    (2, 1), (2, 2), (2, 4), (2, 5), (2, 6),
                    (3, 0), (3, 2), (3, 5), (3, 6), (3, 11),
                    (4, 3), (4, 4), (4, 6), (4, 7), (4, 8),
                    (5, 4), (5, 10),
                    (6, 1), (6, 10),
                    (7, 2), (7, 6), (7, 9), (7, 11),
                    (8, 1), (8, 4), (8, 6), (8, 8), (8, 10),
                    (9, 1), (9, 3), (9, 7), (9, 11),
                    (10, 0), (10, 1), (10, 4), (10, 6), (10, 11),
                    (11, 0), (11, 1), (11, 4), (11, 6), (11, 11)}

# Define the districts
districts = {1: set(range(5)), 2: set(range(5, 6)), 3: set(range(6, 12)}

# Define a function to find the shortest path using breadth-first search
def shortest_path(city_map, start, end, closed_workshops, districts):
    queue = [(start, [start])]
    visited = set()
    
    while queue:
        current, path = queue.pop(0)
        visited.add(current)
        
        if current == end:
            return path
        
        for neighbor in [(current[0]+1, current[1]), (current[0]-1, current[1]),
                         (current[0], current[1]+1), (current[0], current[1]-1)]:
            if neighbor[0] in range(12) and neighbor[1] in range(12) and neighbor not in visited and neighbor not in closed_workshops:
                if any(neighbor in districts[i] for i in range(1, 4)):
                    queue.append((neighbor, path + [neighbor]))
    
    return None

# Find the shortest path from (4, 11) to (6, 0)
start = (4, 11)
end = (6, 0)
path = shortest_path(city_map, start, end, closed_workshops, districts)

print(path)
