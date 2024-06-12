
# Define the adjacency matrix
adjacency_matrix = {
    'Z': ['N', 'F'],
    'G': ['E', 'R', 'W'],
    'K': ['N', 'S', 'V', 'W'],
    'N': ['S', 'X'],
    'S': ['X', 'E'],
    'X': ['G', 'I', 'F', 'C', 'W'],
    'I': ['V'],
    'F': ['N', 'S', 'C', 'W'],
    'E': ['Z', 'K', 'X', 'I', 'C', 'R'],
    'C': ['G', 'N', 'W'],
    'R': ['K', 'C'],
    'V': ['G', 'K', 'S', 'I', 'E', 'C'],
    'L': ['G', 'I', 'F'],
    'W': ['Z', 'X', 'C', 'V', 'L']
}

# Define the start city and the destination cities
start_city = 'I'
destination_cities = ['S', 'W']

# Define a function to find the quickest route
def find_route(city, visited, route):
    # Add the current city to the route
    route.append(city)
    visited.add(city)

    # If we have visited all the destination cities twice, return the route
    if route.count(destination_cities[0]) == 2 and route.count(destination_cities[1]) == 2:
        return route

    # Otherwise, for each city connected to the current city
    for next_city in adjacency_matrix[city]:
        # If we have not visited the city or it is a destination city
        if next_city not in visited or next_city in destination_cities:
            # Recursively find the route from the next city
            result = find_route(next_city, visited, route)
            # If a route is found, return it
            if result:
                return result

    # If no route is found, backtrack by removing the current city from the route and the visited set
    route.pop()
    visited.remove(city)

    return None

# Find the quickest route
route = find_route(start_city, set(), [])

# Print the route
print(route)
