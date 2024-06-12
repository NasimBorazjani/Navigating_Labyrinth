
# Define the adjacency matrix
adjacency_matrix = {
    'R': ['F', 'M', 'X', 'L'],
    'Q': ['X', 'H'],
    'Y': ['R', 'Q', 'L'],
    'U': ['Y', 'T'],
    'F': ['Q', 'M', 'X', 'L'],
    'K': ['R', 'U', 'F', 'M', 'X'],
    'M': ['K', 'T'],
    'T': ['Q', 'Y', 'X'],
    'X': ['Q', 'U', 'L'],
    'W': ['R', 'U', 'F', 'T'],
    'H': ['Q', 'F', 'W'],
    'L': ['W']
}

# Define the start city and the destination cities
start_city = 'L'
destination_cities = ['M', 'Q']

# Define a function to find the quickest route
def find_route(city, visited, path):
    # Mark the current city as visited and add it to the path
    visited[city] = True
    path.append(city)

    # If the path includes the destination cities twice, print the path
    if path.count(destination_cities[0]) == 2 and path.count(destination_cities[1]) == 2:
        print(path)

    # If not, visit the adjacent cities
    else:
        for adjacent_city in adjacency_matrix[city]:
            if not visited[adjacent_city] or (adjacent_city in destination_cities and path.count(adjacent_city) < 2):
                find_route(adjacent_city, visited.copy(), path.copy())

# Initialize the visited dictionary and the path list
visited = {city: False for city in adjacency_matrix.keys()}
path = []

# Find the quickest route
find_route(start_city, visited, path)
