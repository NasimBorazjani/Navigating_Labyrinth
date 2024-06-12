
import numpy as np

# Define the adjacency matrix
adj_matrix = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                        [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                        [0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                        [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]])

# Define the cities
cities = ['J', 'U', 'X', 'R', 'L', 'Z', 'O', 'F', 'Q', 'C', 'N', 'V', 'M']

# Initialize variables
current_city = 'J'
path = [current_city]
visited = [current_city]

# Function to find the next city to visit
def find_next_city(current_city, visited):
    for i, city in enumerate(cities):
        if adj_matrix[cities.index(current_city)][i] == 1 and city not in visited:
            return city
    return None

# Visit Z and M for the first time
next_city = find_next_city(current_city, visited)
while next_city != 'Z' and next_city != 'M':
    path.append(next_city)
    visited.append(next_city)
    current_city = next_city
    next_city = find_next_city(current_city, visited)

# Visit Z and M for the second time
visited = []
next_city = find_next_city(current_city, visited)
while next_city != 'Z' and next_city != 'M':
    path.append(next_city)
    visited.append(next_city)
    current_city = next_city
    next_city = find_next_city(current_city, visited)

# Visit the remaining cities to complete the path
visited = []
next_city = find_next_city(current_city, visited)
while next_city is not None:
    path.append(next_city)
    visited.append(next_city)
    current_city = next_city
    next_city = find_next_city(current_city, visited)

print(path)
