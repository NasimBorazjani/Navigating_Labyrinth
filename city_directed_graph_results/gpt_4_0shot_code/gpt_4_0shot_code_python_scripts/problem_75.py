
# Define the adjacency matrix
adjacency_matrix = {
    'L': ['P', 'N', 'F', 'K', 'B'],
    'S': ['R', 'F', 'E'],
    'P': ['N', 'K'],
    'R': ['P', 'F', 'H'],
    'N': ['R', 'O', 'K', 'T'],
    'F': ['R', 'O', 'E'],
    'O': ['S', 'K', 'T'],
    'K': ['S', 'F', 'B', 'W'],
    'B': ['P', 'N', 'E'],
    'H': ['S', 'F', 'O', 'E'],
    'T': ['L', 'W', 'U', 'E'],
    'W': ['L', 'P', 'F', 'H', 'E'],
    'U': ['L', 'P', 'K', 'B', 'T'],
    'E': ['S', 'R', 'O', 'K', 'W']
}

# Define the start city
start_city = 'B'

# Define the destination cities
destination_cities = ['W', 'F']

# Define a function to find the quickest route
def find_route(city, visited, path):
    # Mark the current city as visited
    visited.append(city)
    path.append(city)

    # If the path includes each destination city twice, print the path
    if all(path.count(city) == 2 for city in destination_cities):
        print(' -> '.join(path))

    # Recur for all the cities adjacent to this city
    else:
        for next_city in adjacency_matrix[city]:
            if next_city not in visited or next_city in destination_cities:
                find_route(next_city, visited.copy(), path.copy())

# Call the function to find the quickest route
find_route(start_city, [], [])
