
# Define the adjacency matrix
adj_matrix = {
    'D': ['F', 'S', 'I'],
    'Y': ['D', 'M', 'Q', 'B'],
    'F': ['M', 'K', 'I'],
    'M': ['K', 'S', 'I', 'L'],
    'W': ['F', 'H', 'L'],
    'H': ['F', 'W', 'B'],
    'Q': ['D', 'M', 'Y', 'B'],
    'B': ['F', 'W', 'H'],
    'K': ['H', 'B', 'V'],
    'S': ['Y', 'F', 'B'],
    'V': ['B', 'K', 'L'],
    'I': ['Y', 'W', 'Q'],
    'L': ['F', 'S', 'V']
}

# Define the start city and the destination cities
start_city = 'K'
dest_cities = ['D', 'L']

# Define a function to find the quickest route
def find_route(city, visited, route):
    # Add the current city to the route
    route.append(city)
    visited.add(city)

    # If we have visited the destination cities twice, return the route
    if route.count(dest_cities[0]) == 2 and route.count(dest_cities[1]) == 2:
        return route

    # Otherwise, explore the neighboring cities
    for neighbor in adj_matrix[city]:
        if neighbor not in visited or (neighbor in dest_cities and route.count(neighbor) < 2):
            result = find_route(neighbor, visited, route)
            if result:
                return result

    # If no route is found, backtrack
    route.pop()
    visited.remove(city)

# Find the quickest route
route = find_route(start_city, set(), [])
print(route)
