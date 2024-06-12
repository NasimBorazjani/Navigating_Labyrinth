
# Define the adjacency matrix
adjacency_matrix = {
    'G': ['X', 'D', 'Y'],
    'P': ['H', 'I', 'J'],
    'H': ['G', 'P', 'X', 'Q'],
    'I': ['G'],
    'J': ['G', 'H', 'I', 'L'],
    'X': ['Q', 'Y'],
    'D': ['P', 'X', 'Y'],
    'V': ['G', 'X', 'D', 'Y'],
    'Q': ['G', 'H', 'J', 'L', 'D'],
    'L': ['H', 'V', 'Y'],
    'Y': ['G', 'I', 'J', 'X', 'L']
}

# Define the start city and the destination cities
start_city = 'D'
destination_cities = ['Q', 'G']

# Define a function to find the quickest route
def find_route(city, visited, route):
    # Add the current city to the route
    route.append(city)
    # If the current city is a destination city and it has been visited twice, return the route
    if city in destination_cities and visited.count(city) == 2:
        return route
    # If the current city is not a destination city and it has been visited, return None
    if city not in destination_cities and visited.count(city) > 0:
        return None
    # Add the current city to the visited cities
    visited.append(city)
    # For each neighboring city, try to find a route
    for next_city in adjacency_matrix[city]:
        next_route = find_route(next_city, visited.copy(), route.copy())
        # If a route is found, return it
        if next_route is not None:
            return next_route
    # If no route is found, return None
    return None

# Find the quickest route
quickest_route = find_route(start_city, [], [])

# Print the quickest route
print(quickest_route)
