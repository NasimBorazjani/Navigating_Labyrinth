
# Define the adjacency matrix
adjacency_matrix = {
    'G': ['R', 'H'],
    'J': ['G', 'Y', 'Q', 'K'],
    'Y': ['G', 'R', 'F', 'N'],
    'Q': ['F', 'H'],
    'C': ['G', 'J', 'K'],
    'D': ['G', 'Y', 'Q', 'F'],
    'R': ['J', 'Y', 'Q', 'D', 'H'],
    'F': ['D', 'R'],
    'K': ['G', 'R', 'F', 'H', 'N'],
    'H': ['J', 'Y', 'Q', 'C'],
    'N': ['J', 'Y', 'C', 'D', 'F']
}

# Define the start city and the destination cities
start_city = 'Q'
destination_cities = ['K', 'Y']

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
        if next_city not in visited or (next_city in destination_cities and path.count(next_city) < 2):
            route = find_route(next_city, visited, path)
            if route:
                return route

    # If no route is found, backtrack
    path.pop()
    visited.remove(city)

# Find the quickest route
route = find_route(start_city, set(), [])

# Print the route
print(route)
