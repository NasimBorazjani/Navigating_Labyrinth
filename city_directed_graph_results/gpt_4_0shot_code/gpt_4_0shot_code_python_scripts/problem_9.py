
# Define the adjacency matrix
adjacency_matrix = {
    'R': ['T', 'C', 'Y', 'E', 'W'],
    'T': ['C', 'F', 'W'],
    'C': ['Y'],
    'F': ['R', 'T', 'X', 'E', 'A'],
    'S': ['R', 'F', 'E'],
    'X': ['R', 'C', 'F', 'S'],
    'Y': ['R', 'T', 'F'],
    'E': ['C', 'S'],
    'A': ['R', 'S', 'X', 'Y', 'E'],
    'W': ['R', 'F', 'S', 'X', 'E', 'A']
}

# Define the start city
start_city = 'C'

# Define the destination cities
destination_cities = ['F', 'W']

# Define a function to find the quickest route
def find_route(city, visited, path):
    # Add the current city to the path
    path.append(city)
    
    # If the path contains the destination cities twice, print the path
    if path.count('F') == 2 and path.count('W') == 2:
        print(path)
        return
    
    # For each city connected to the current city
    for next_city in adjacency_matrix[city]:
        # If the city has not been visited or it is a destination city
        if next_city not in visited or next_city in destination_cities:
            # Add the city to the visited cities
            visited.add(next_city)
            # Find the route from the next city
            find_route(next_city, visited, path)
            # Remove the city from the visited cities and the path
            visited.remove(next_city)
            path.pop()

# Find the quickest route from the start city
find_route(start_city, set(), [])
