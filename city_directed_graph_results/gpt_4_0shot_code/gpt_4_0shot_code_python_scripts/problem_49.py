
# Define the adjacency matrix
adjacency_matrix = {
    'W': ['Y', 'K', 'Q'],
    'D': ['A', 'E'],
    'R': ['W', 'C'],
    'A': ['D', 'R', 'Y', 'S', 'N'],
    'Y': ['Q'],
    'F': ['W', 'R', 'S'],
    'C': ['D', 'Y', 'F', 'S', 'N', 'E', 'Q'],
    'S': ['W', 'D', 'Y', 'N'],
    'N': ['D', 'R', 'A', 'F'],
    'E': ['K'],
    'K': ['A', 'F', 'N'],
    'Q': ['D', 'A', 'S', 'N', 'E']
}

# Define the start city
start_city = 'E'

# Define the destination cities
destination_cities = ['D', 'R']

# Define a function to find the quickest route
def find_route(city, visited, path):
    # Add the current city to the path
    path.append(city)
    
    # If the path contains the destination cities twice, print the path
    if path.count('D') == 2 and path.count('R') == 2:
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
find_route(start_city, set(), [])
