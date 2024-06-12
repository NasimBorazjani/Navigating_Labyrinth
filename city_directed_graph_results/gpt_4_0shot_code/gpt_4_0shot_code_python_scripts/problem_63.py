
# Define the adjacency matrix
adjacency_matrix = {
    'Z': ['R', 'U', 'L', 'I'],
    'N': ['Z', 'O', 'P', 'L', 'Q', 'G'],
    'R': ['N', 'L', 'I'],
    'F': ['L'],
    'O': ['R', 'F', 'J', 'I', 'Q'],
    'U': ['F', 'L', 'J'],
    'P': ['U', 'I'],
    'L': ['Z', 'O'],
    'J': ['U', 'I'],
    'I': ['U', 'S'],
    'S': ['N', 'O', 'U', 'L', 'J'],
    'Q': ['U', 'P', 'G'],
    'G': ['O', 'L']
}

# Define the start city and the destination cities
start_city = 'F'
destination_cities = ['N', 'J']

# Define a function to find the quickest route
def find_route(city, visited, route):
    # Add the current city to the route
    route.append(city)
    visited.add(city)

    # If we have visited the destination cities twice, return the route
    if route.count(destination_cities[0]) == 2 and route.count(destination_cities[1]) == 2:
        return route

    # Otherwise, visit each city connected to the current city
    for next_city in adjacency_matrix[city]:
        if next_city not in visited or (next_city in destination_cities and route.count(next_city) < 2):
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
