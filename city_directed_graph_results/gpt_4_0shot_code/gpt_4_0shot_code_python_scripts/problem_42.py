
# Define the adjacency matrix
adjacency_matrix = {
    'J': ['Y', 'M'],
    'U': ['T', 'Y', 'C', 'P'],
    'T': ['J', 'N', 'H'],
    'S': ['J', 'U', 'Y', 'P'],
    'N': ['J', 'S', 'A', 'M'],
    'F': ['A'],
    'Y': ['H'],
    'C': ['T', 'F'],
    'H': ['J', 'U', 'S', 'C'],
    'A': ['J', 'F', 'H', 'M'],
    'M': ['T', 'H', 'P'],
    'P': ['N', 'C', 'H', 'M']
}

# Define the start city and the destination cities
start_city = 'F'
destination_cities = ['H', 'N']

# Define a function to find the quickest route
def find_route(city, visited, path):
    # Add the current city to the path
    path.append(city)
    visited[city] += 1

    # If the path includes each destination city twice, print the path
    if all(visited[city] == 2 for city in destination_cities):
        print(path)

    # Otherwise, continue to the next city
    else:
        for next_city in adjacency_matrix[city]:
            if visited[next_city] < 2:
                find_route(next_city, visited.copy(), path.copy())

# Initialize the visited dictionary and the path list
visited = {city: 0 for city in adjacency_matrix}
path = []

# Find the quickest route
find_route(start_city, visited, path)
