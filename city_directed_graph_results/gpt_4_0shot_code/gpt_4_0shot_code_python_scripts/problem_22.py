
# Define the adjacency matrix
adjacency_matrix = {
    'X': ['U', 'N', 'Z', 'S'],
    'M': ['U', 'N', 'T', 'S'],
    'U': ['N', 'S'],
    'N': ['X', 'S', 'F'],
    'T': ['X', 'M', 'U', 'N', 'V', 'E'],
    'V': ['X', 'M', 'U', 'N', 'T', 'Z', 'S', 'E', 'J'],
    'Z': ['M', 'V', 'F'],
    'S': ['N', 'F', 'E'],
    'F': ['E'],
    'E': ['U', 'Z', 'S', 'J'],
    'J': ['M', 'U']
}

# Define the start city
start_city = 'X'

# Define the destination cities
destination_cities = ['E', 'T']

# Define a function to find the quickest route
def find_route(city, visited, path):
    # Add the current city to the path
    path.append(city)
    
    # If the path includes each destination city twice, print the path
    if all(path.count(destination) == 2 for destination in destination_cities):
        print(path)
        return
    
    # For each city connected to the current city
    for next_city in adjacency_matrix[city]:
        # If the city has not been visited or it is a destination city
        if next_city not in visited or next_city in destination_cities:
            # Add the city to the visited cities
            visited.add(next_city)
            # Recursively find the route from the next city
            find_route(next_city, visited, path)
            # Remove the city from the visited cities and the path
            visited.remove(next_city)
            path.pop()

# Find the quickest route from the start city
find_route(start_city, set(start_city), [])
