
# Define the adjacency matrix
adjacency_matrix = {
    'L': ['H', 'O', 'J', 'Y'],
    'H': ['A', 'I', 'W', 'Y'],
    'D': ['H'],
    'O': ['H', 'A', 'B'],
    'A': ['D', 'B'],
    'M': ['L', 'H'],
    'I': ['J', 'Y'],
    'J': ['L', 'O', 'W'],
    'W': ['L', 'M', 'I', 'B'],
    'Y': ['H', 'D'],
    'B': ['I', 'W']
}

# Define the start city and the destination cities
start_city = 'D'
destination_cities = ['B', 'L']

# Define a function to find the quickest route
def find_route(city, visited, route):
    # Add the current city to the route
    route.append(city)
    # If the current city is a destination city and we have visited all destination cities twice, return the route
    if city in destination_cities:
        visited[city] += 1
        if all(value == 2 for value in visited.values()):
            return route
    # If not, continue to the next city
    for next_city in adjacency_matrix[city]:
        if next_city not in route or (next_city in destination_cities and visited[next_city] < 2):
            result = find_route(next_city, visited.copy(), route.copy())
            if result:
                return result

# Initialize the visited dictionary
visited = {city: 0 for city in destination_cities}

# Find the quickest route
route = find_route(start_city, visited, [])

# Print the route
print(route)
