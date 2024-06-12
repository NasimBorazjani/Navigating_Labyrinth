
# Define the adjacency matrix
adjacency_matrix = {
    'G': ['T', 'K', 'Y', 'P'],
    'T': ['A', 'E'],
    'M': ['G', 'T'],
    'U': ['G', 'M'],
    'K': ['T', 'U', 'D', 'P', 'I'],
    'Y': ['M', 'U', 'K', 'D'],
    'D': ['M', 'S', 'I'],
    'A': ['G', 'U', 'Y', 'D'],
    'P': ['M', 'A', 'I'],
    'R': ['U', 'E'],
    'E': ['K', 'R'],
    'S': ['T', 'K', 'P'],
    'I': ['U', 'Y', 'E']
}

# Define the start city
start_city = 'R'

# Define the destination cities
destination_cities = ['A', 'Y']

# Define the visited cities
visited_cities = []

# Define the path
path = []

# Define the DFS function
def dfs(city, visited_cities, path):
    # Add the city to the visited cities
    visited_cities.append(city)
    
    # Add the city to the path
    path.append(city)
    
    # If the path contains the destination cities twice, print the path
    if path.count(destination_cities[0]) == 2 and path.count(destination_cities[1]) == 2:
        print(path)
        return
    
    # For each neighbor of the city
    for neighbor in adjacency_matrix[city]:
        # If the neighbor has not been visited or it is a destination city
        if neighbor not in visited_cities or neighbor in destination_cities:
            # Call the DFS function
            dfs(neighbor, visited_cities.copy(), path.copy())

# Call the DFS function
dfs(start_city, visited_cities, path)
