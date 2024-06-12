
import itertools

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],  # L
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],  # T
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],  # W
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # P
    [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],  # Z
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],  # H
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],  # I
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],  # X
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],  # R
    [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],  # C
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]   # K
]

# Dictionary to store shortest distances from city I
distances = {city: matrix[city][0] for city in range(len(matrix))}

# List of cities to visit twice
cities_to_visit_twice = ['L', 'W']

# Start city
start_city = 'I'

# Path
path = [start_city]

# Visit each city twice
for _ in range(2):
    for city in cities_to_visit_twice:
        city_index = ord(city) - ord('A')
        distances[city_index] = matrix[city_index][0]

    # Find city with shortest total distance to visit twice
    city_to_visit = min(distances, key=distances.get)
    path.append(chr(city_to_visit + ord('A')))
    distances[city_to_visit] = float('inf')  # Ensure city is not visited again in this iteration

# Find remaining cities
for city in range(len(matrix)):
    if city not in [ord(city) - ord('A') for city in path]:
        path.append(chr(city + ord('A')))

print(path)
