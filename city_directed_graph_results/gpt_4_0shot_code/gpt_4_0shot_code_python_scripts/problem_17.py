
# Define the adjacency matrix
adj_matrix = {
    'I': ['E', 'Z', 'Q'],
    'V': ['H'],
    'F': ['I', 'E', 'A'],
    'E': ['I', 'Y'],
    'Y': ['I', 'F', 'Z', 'Q'],
    'A': ['I', 'V'],
    'Z': ['I', 'F', 'E', 'Q'],
    'T': ['V', 'F', 'E', 'Y', 'A', 'Z'],
    'H': ['I', 'T'],
    'Q': ['Z', 'T', 'H']
}

# Define the start city and the destination cities
start_city = 'V'
dest_cities = ['I', 'Y']

# Define a function to find the quickest route
def find_route(city, visited, path):
    # Add the current city to the path
    path.append(city)
    visited.add(city)

    # If the path includes each destination city twice, return the path
    if path.count(dest_cities[0]) == 2 and path.count(dest_cities[1]) == 2:
        return path

    # If not, explore each neighboring city
    for neighbor in adj_matrix[city]:
        if neighbor not in visited or neighbor in dest_cities:
            route = find_route(neighbor, visited.copy(), path.copy())
            if route:
                return route

# Find the quickest route
route = find_route(start_city, set(), [])

# Print the route
print(route)
