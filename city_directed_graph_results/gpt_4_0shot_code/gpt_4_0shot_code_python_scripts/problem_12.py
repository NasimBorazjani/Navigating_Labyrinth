
# Define the adjacency matrix
adjacency_matrix = {
    'S': ['T', 'B', 'P'],
    'T': ['V'],
    'R': ['S', 'T', 'P', 'N'],
    'A': ['S', 'R', 'V', 'N'],
    'L': ['A', 'V', 'I', 'N'],
    'B': ['S', 'I'],
    'V': ['S', 'T', 'R', 'A', 'B', 'P', 'N'],
    'I': ['L'],
    'P': ['I'],
    'N': ['L', 'B']
}

# Define the start city and the destination cities
start_city = 'B'
destination_cities = ['V', 'L']

# Define a function to find the quickest route
def find_route(city, visited, path):
    # Add the current city to the path
    path.append(city)
    # Mark the current city as visited
    visited[city] += 1
    # If the destination cities have been visited twice, return the path
    if all(visited[city] == 2 for city in destination_cities):
        return path
    # Visit the next city
    for next_city in adjacency_matrix[city]:
        if visited[next_city] < 2:
            route = find_route(next_city, visited.copy(), path.copy())
            if route:
                return route

# Initialize the visited dictionary
visited = {city: 0 for city in adjacency_matrix.keys()}

# Find the quickest route
route = find_route(start_city, visited, [])

# Print the route
print(route)
