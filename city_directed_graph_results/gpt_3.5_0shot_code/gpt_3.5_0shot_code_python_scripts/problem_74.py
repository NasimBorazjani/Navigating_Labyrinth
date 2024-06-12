
import numpy as np

# Create adjacency matrix
adj_matrix = np.array([[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
                        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                        [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                        [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                        [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]])

# Define the starting city
start_city = 'M'

# Find the indices of cities L and Z
city_indices = {'O': 0, 'M': 1, 'U': 2, 'L': 3, 'Q': 4, 'P': 5, 'D': 6, 'A': 7, 'S': 8, 'B': 9, 'K': 10, 'V': 11, 'E': 12, 'Z': 13}
city_L_index = city_indices['L']
city_Z_index = city_indices['Z']

# Initialize the path with the starting city
path = [start_city]

# Visit city L and Z for the first time
if adj_matrix[city_indices[start_city], city_L_index] == 1:
    path.append('L')
else:
    path.append('Z')

# Visit the rest of the cities in the order of their indices
for i in range(len(adj_matrix)):
    if i != city_indices[start_city] and i != city_L_index and i != city_Z_index:
        if adj_matrix[city_indices[start_city], i] == 1:
            path.append(list(city_indices.keys())[list(city_indices.values()).index(i)])

# Visit city Z and L for the second time
if adj_matrix[city_indices[path[-1]], city_Z_index] == 1:
    path.append('Z')
else:
    path.append('L')

print(path)
