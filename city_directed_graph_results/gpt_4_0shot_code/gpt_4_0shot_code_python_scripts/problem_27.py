
# Define the adjacency matrix
adjacency_matrix = {
    'J': ['X'],
    'H': ['K', 'B', 'U'],
    'K': ['I'],
    'W': ['H', 'K', 'X'],
    'X': ['H', 'I'],
    'I': ['K', 'B', 'U', 'Z'],
    'B': ['W', 'Z', 'G'],
    'U': ['K', 'W', 'X'],
    'D': ['W', 'I', 'U'],
    'Z': ['J', 'K', 'W', 'U'],
    'G': ['J', 'X', 'Z']
}

# Define the start city and the destination cities
start_city = 'D'
destination_cities = ['H', 'Z']

# Define a function to find the quickest route
def find_route(city, visited, path):
    # Add the current city to the path
    path.append(city)
    visited.add(city)

    # If we have visited the destination cities twice, return the path
    if path.count(destination_cities[0]) == 2 and path.count(destination_cities[1]) == 2:
        return path

    # Otherwise, continue to the next city
    for next_city in adjacency_matrix[city]:
        if next_city not in visited or next_city in destination_cities:
            route = find_route(next_city, visited.copy(), path.copy())
            if route:
                return route

# Find the quickest route
route = find_route(start_city, set(), [])

# Print the route
print(route)
