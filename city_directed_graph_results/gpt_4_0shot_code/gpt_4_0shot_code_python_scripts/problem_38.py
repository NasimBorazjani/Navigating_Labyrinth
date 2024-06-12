
# Define the adjacency matrix
adj_matrix = {
    'S': ['X', 'V', 'F', 'C'],
    'X': ['O', 'D'],
    'Y': ['S', 'X', 'R', 'F'],
    'Q': ['X', 'D'],
    'O': ['R', 'V', 'H'],
    'R': ['X', 'V', 'C'],
    'D': ['S', 'Y', 'H'],
    'V': ['Y', 'R', 'D', 'C'],
    'H': ['S', 'Y', 'Q', 'V', 'C'],
    'J': ['X', 'Y', 'R', 'H'],
    'F': ['Y', 'D', 'V', 'J'],
    'C': ['S', 'V', 'J', 'F']
}

# Define the start city and the destination cities
start_city = 'Q'
dest_cities = ['V', 'F']

# Define a function to find the quickest route
def find_route(city, visited, route):
    # Add the current city to the route
    route.append(city)
    # If the route includes each destination city twice, return the route
    if route.count(dest_cities[0]) == 2 and route.count(dest_cities[1]) == 2:
        return route
    # For each city connected to the current city
    for next_city in adj_matrix[city]:
        # If the city has not been visited or it is a destination city
        if next_city not in visited or next_city in dest_cities:
            # Add the city to the visited list
            visited.append(next_city)
            # Recursively find the route from the next city
            result = find_route(next_city, visited, route)
            # If a route is found, return it
            if result:
                return result
            # If no route is found, remove the city from the visited list and the route
            visited.remove(next_city)
            route.remove(next_city)
    # If no route is found, return None
    return None

# Find the quickest route
route = find_route(start_city, [], [])

# Print the route
print(route)
