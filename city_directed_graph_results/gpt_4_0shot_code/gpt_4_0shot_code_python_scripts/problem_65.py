
# Define the adjacency matrix
adjacency_matrix = {
    'F': ['Z', 'I', 'P'],
    'D': ['F', 'E', 'I'],
    'E': ['G', 'S', 'C'],
    'Z': ['E', 'Y', 'X', 'S', 'C'],
    'G': ['F', 'I', 'P'],
    'Y': ['G', 'I'],
    'N': ['Y'],
    'I': ['E', 'Z', 'X'],
    'X': ['E', 'G', 'P', 'S'],
    'P': ['D', 'Z', 'Q'],
    'S': ['F', 'X', 'N', 'C'],
    'Q': ['D', 'X'],
    'C': ['G', 'N', 'I', 'X']
}

# Define the start city and the destination cities
start_city = 'Q'
destination_cities = ['F', 'N']

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
            if visited[next_city] < 2 and (all(visited[city] >= 1 for city in destination_cities) or next_city in destination_cities):
                find_route(next_city, visited.copy(), path.copy())

# Initialize the visited dictionary
visited = {city: 0 for city in adjacency_matrix.keys()}

# Find the quickest route
find_route(start_city, visited, [])
