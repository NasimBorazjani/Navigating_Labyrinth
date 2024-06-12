
# Define the adjacency matrix
adjacency_matrix = {
    'R': ['E', 'D', 'J'],
    'S': ['W', 'G', 'N', 'J'],
    'W': ['R'],
    'B': ['P', 'J'],
    'P': ['S', 'D'],
    'G': ['B'],
    'Q': ['W', 'B', 'P', 'N', 'D'],
    'E': ['R', 'S', 'P', 'G', 'Q'],
    'N': ['P', 'G', 'D'],
    'D': ['W', 'E'],
    'J': ['S', 'P', 'Q']
}

# Define the start city and the destination cities
start_city = 'G'
destination_cities = ['S', 'E']

# Define a function to find the quickest route
def find_route(city, visited, route):
    # Add the current city to the route
    route.append(city)
    # If the current city is a destination city and we have visited all destination cities twice, return the route
    if city in destination_cities:
        visited[city] += 1
        if all(value == 2 for value in visited.values()):
            return route
    # If the current city is not a destination city or we have not visited it twice yet, continue with the next city
    for next_city in adjacency_matrix[city]:
        if next_city not in route or (next_city in destination_cities and visited[next_city] < 2):
            result = find_route(next_city, visited, route)
            if result:
                return result
    # If no route is found, backtrack by removing the current city from the route and decreasing its visited count
    route.pop()
    if city in visited:
        visited[city] -= 1
    return None

# Initialize the visited dictionary
visited = {city: 0 for city in destination_cities}

# Find the quickest route
route = find_route(start_city, visited, [])

# Print the route
print(route)
