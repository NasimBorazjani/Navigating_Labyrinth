
# Define the adjacency matrix
adjacency_matrix = {
    'E': ['N', 'R', 'M', 'B'],
    'K': ['E', 'O', 'M'],
    'G': ['E', 'A', 'H'],
    'C': ['K', 'U', 'O'],
    'U': ['E', 'G'],
    'A': ['C', 'U', 'O', 'N', 'W'],
    'J': ['A', 'O', 'B', 'Q'],
    'O': ['E', 'H'],
    'N': ['K', 'G', 'U', 'J', 'Q'],
    'R': ['G', 'O', 'M', 'B', 'Q'],
    'W': ['E', 'G', 'C', 'A', 'J', 'M', 'H', 'Q'],
    'M': ['C', 'U', 'A', 'O'],
    'B': ['U', 'J', 'M'],
    'H': ['E', 'K', 'A', 'M', 'B'],
    'Q': ['E', 'G', 'C', 'U', 'M', 'B', 'H']
}

# Define the start city and the destination cities
start_city = 'C'
destination_cities = ['E', 'Q']

# Define a function to find the quickest route
def find_route(city, visited, route):
    # Add the current city to the route
    route.append(city)
    # If the route includes each destination city twice, return the route
    if route.count(destination_cities[0]) == 2 and route.count(destination_cities[1]) == 2:
        return route
    # For each city connected to the current city
    for next_city in adjacency_matrix[city]:
        # If the city has not been visited or it is a destination city
        if next_city not in visited or next_city in destination_cities:
            # Add the city to the visited cities
            visited.add(next_city)
            # Find the route from the next city
            result = find_route(next_city, visited, route)
            # If a route was found, return it
            if result:
                return result
            # Otherwise, remove the city from the visited cities and the route
            visited.remove(next_city)
            route.pop()

# Find the quickest route
route = find_route(start_city, set(), [])

# Print the route
print(route)
