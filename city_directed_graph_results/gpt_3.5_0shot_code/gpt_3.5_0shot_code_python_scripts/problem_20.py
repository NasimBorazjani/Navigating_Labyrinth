
import numpy as np

# Define the adjacency matrix
adj_matrix = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                        [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]])

# Define the cities
cities = ['F', 'I', 'Y', 'R', 'X', 'Q', 'M', 'S', 'C', 'D', 'N']

# Initialize variables
current_city = 'F'
visited = [current_city]
total_cities = len(cities)
count = 0

# Function to find the next city to visit
def find_next_city(current_city):
    for i in range(total_cities):
        if adj_matrix[cities.index(current_city)][i] == 1 and cities[i] not in visited:
            return cities[i]
    return None

# Visit I and N twice
while count < 2:
    next_city = find_next_city(current_city)
    if next_city == 'I' or next_city == 'N':
        visited.append(next_city)
        count += 1
    visited.append(next_city)
    current_city = next_city

print(visited)
