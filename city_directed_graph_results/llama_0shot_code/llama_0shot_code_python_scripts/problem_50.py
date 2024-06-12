
import itertools

# The adjacency matrix
adjacency_matrix = [
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
]

# Convert the adjacency matrix into a dictionary
map = {city: {} for city in 'ABCDEFGHIJKLNO'}
for i, row in enumerate(adjacency_matrix):
    for j, col in enumerate(row):
        if col == 1:
            map[chr(i + 65)][chr(j + 65)] = 1

# Function to get the quickest route from the current city to the destination cities
def get_path(current, destinations, map, path=[]):
    path = path + [current]
    if current in destinations and len(path) == len(destinations) * 2 + 1:
        return path
    best_path = None
    for city in map[current]:
        if city not in path:
            new_path = get_path(city, destinations, map, path)
            if new_path and (not best_path or len(new_path) < len(best_path)):
                best_path = new_path
    return best_path

# Get the quickest route to visit cities 'N' and 'O' exactly twice, starting from 'E'
destinations = 'NO'
start = 'E'
path = get_path(start, destinations, map)

# Print the solution
print(path)
