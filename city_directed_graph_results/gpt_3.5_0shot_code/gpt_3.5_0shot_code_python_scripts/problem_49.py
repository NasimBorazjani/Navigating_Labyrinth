
import numpy as np

# Define the adjacency matrix
adj_matrix = np.array([[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                        [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                        [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0]])

# Define the cities
cities = ['W', 'D', 'R', 'A', 'Y', 'F', 'C', 'S', 'N', 'E', 'K', 'Q']

# Initialize variables
current_city = 'E'
path = [current_city]

# Find the quickest route to visit D and R twice
while 'D' in path or 'R' in path:
    if 'D' in path and 'R' in path:
        break
    elif 'D' in path:
        next_city = cities[np.argmax(adj_matrix[cities.index(current_city)])
    else:
        next_city = cities[np.argmin(adj_matrix[cities.index(current_city)])]
    path.append(next_city)
    current_city = next_city

print(path)
