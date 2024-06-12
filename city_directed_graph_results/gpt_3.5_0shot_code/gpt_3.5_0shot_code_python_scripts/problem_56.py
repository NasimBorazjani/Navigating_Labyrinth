
import numpy as np

# Define the adjacency matrix
adj_matrix = np.array([[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
                        [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]])

# Define the cities
cities = ['K', 'M', 'B', 'X', 'N', 'D', 'V', 'C', 'I', 'R', 'F', 'W', 'L']

# Define the starting city
start_city = 'C'

# Find the quickest route to visit B and L twice
def find_quickest_route(adj_matrix, cities, start_city):
    current_city = start_city
    path = [current_city]
    visited = [False] * len(cities)
    visited[cities.index(current_city)] = True
    while 'B' in path or 'L' in path:
        next_city = None
        min_time = float('inf')
        for i, city in enumerate(cities):
            if adj_matrix[cities.index(current_city)][i] == 1 and not visited[i]:
                if city == 'B' or city == 'L':
                    visited[i] = True
                    path.append(city)
                    current_city = city
                    break
                else:
                    time = adj_matrix[cities.index(current_city)][i]
                    if time < min_time:
                        min_time = time
                        next_city = city
        if next_city is not None:
            visited[cities.index(next_city)] = True
            path.append(next_city)
            current_city = next_city
    return path

# Find and print the quickest route
quickest_route = find_quickest_route(adj_matrix, cities, start_city)
print(quickest_route)
