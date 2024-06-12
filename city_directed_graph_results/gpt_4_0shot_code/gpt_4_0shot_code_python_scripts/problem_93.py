
# Define the adjacency matrix
adjacency_matrix = {
    'C': ['Q', 'R'],
    'Q': ['C', 'K', 'B', 'R', 'D', 'Y', 'V', 'N'],
    'T': ['C', 'R', 'N'],
    'K': ['B', 'P'],
    'M': ['T', 'B', 'A', 'N'],
    'B': ['D', 'A', 'V'],
    'R': ['J', 'V', 'O'],
    'D': ['K', 'B', 'J', 'A', 'N'],
    'J': ['T', 'B', 'O'],
    'A': ['C', 'T', 'D', 'J', 'Y', 'V'],
    'Y': ['C', 'T', 'B', 'R', 'J', 'O'],
    'V': ['K', 'J', 'N', 'P'],
    'O': ['C', 'K', 'A'],
    'N': ['C', 'T', 'B', 'P'],
    'P': ['C', 'M', 'V', 'A', 'Y', 'O', 'N']
}

# Define the start city and the destination cities
start_city = 'M'
destination_cities = ['K', 'Y']

# Define a function to find the quickest route
def find_route(city, visited, route):
    # Add the current city to the route
    route.append(city)
    visited.add(city)

    # If we have visited the destination cities twice, return the route
    if route.count(destination_cities[0]) == 2 and route.count(destination_cities[1]) == 2:
        return route

    # Otherwise, continue to the next city
    for next_city in adjacency_matrix[city]:
        if next_city not in visited or next_city in destination_cities:
            result = find_route(next_city, visited, route)
            if result:
                return result

    # If no route is found, backtrack
    route.pop()
    visited.remove(city)

# Find the quickest route
route = find_route(start_city, set(), [])

# Print the route
print(route)
