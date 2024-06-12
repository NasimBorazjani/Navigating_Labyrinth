
# Define the adjacency matrix
adjacency_matrix = {
    'G': ['X', 'T'],
    'X': ['L', 'Y', 'B'],
    'R': ['Y', 'E', 'B'],
    'L': ['E'],
    'Y': ['X'],
    'E': ['Y', 'T', 'B'],
    'V': ['R', 'Y', 'E', 'B', 'H'],
    'T': ['G', 'X', 'R', 'L', 'E'],
    'B': ['Y', 'T', 'H'],
    'H': ['Y', 'V']
}

# Define the start city and the destination cities
start_city = 'H'
destination_cities = ['E', 'X']

# Define a function to find the quickest route
def find_route(city, visited, route):
    # Add the current city to the route
    route.append(city)
    # If the current city is a destination city and it has not been visited twice
    if city in destination_cities and visited.count(city) < 2:
        # Add the current city to the visited cities
        visited.append(city)
    # If all destination cities have been visited twice
    if visited.count(destination_cities[0]) == 2 and visited.count(destination_cities[1]) == 2:
        # Return the route
        return route
    # For each city connected to the current city
    for next_city in adjacency_matrix[city]:
        # If the next city has not been visited or it is a destination city and it has not been visited twice
        if next_city not in route or (next_city in destination_cities and visited.count(next_city) < 2):
            # Find the route from the next city
            next_route = find_route(next_city, visited, route)
            # If a route was found
            if next_route:
                # Return the route
                return next_route
    # If no route was found, remove the current city from the route and the visited cities
    route.pop()
    if city in visited:
        visited.remove(city)

# Find the quickest route
route = find_route(start_city, [], [])

# Print the route
print(route)
