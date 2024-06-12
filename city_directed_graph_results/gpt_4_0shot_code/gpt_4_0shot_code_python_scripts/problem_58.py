
# Define the adjacency matrix
adjacency_matrix = {
    'B': ['K', 'P', 'M', 'R', 'J'],
    'K': ['X', 'P'],
    'S': ['K', 'P'],
    'X': ['K', 'V', 'E'],
    'T': ['K', 'S', 'Q', 'V', 'E'],
    'P': ['T', 'G'],
    'Q': ['B', 'P', 'G', 'V'],
    'M': ['K', 'S', 'T'],
    'R': ['B', 'K', 'X', 'Q', 'G'],
    'G': ['S', 'Q', 'V'],
    'J': ['K', 'T', 'M'],
    'V': ['B', 'R', 'E'],
    'E': ['B', 'K', 'T', 'P', 'Q', 'G']
}

# Define the start city and the destination cities
start_city = 'S'
destination_cities = ['B', 'V']

# Define a function to find the quickest route
def find_route(city, visited, path):
    # Add the current city to the path
    path.append(city)
    visited[city] += 1

    # If the path includes each destination city twice, return the path
    if all(visited[city] >= 2 for city in destination_cities):
        return path

    # Otherwise, continue to the next city
    for next_city in adjacency_matrix[city]:
        if visited[next_city] < 2:
            route = find_route(next_city, visited.copy(), path.copy())
            if route:
                return route

# Find the quickest route
route = find_route(start_city, {city: 0 for city in adjacency_matrix}, [])

# Print the route
print(route)
