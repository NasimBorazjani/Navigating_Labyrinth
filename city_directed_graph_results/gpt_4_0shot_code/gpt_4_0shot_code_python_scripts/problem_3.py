
# Define the adjacency matrix
adjacency_matrix = {
    'O': ['A'],
    'T': ['O', 'I'],
    'I': ['A', 'M', 'R', 'G'],
    'F': ['I', 'G'],
    'A': ['O', 'T', 'X'],
    'M': ['F', 'G'],
    'X': ['I', 'F', 'A', 'Y'],
    'Y': ['O', 'T', 'X', 'R', 'G'],
    'R': ['O', 'T', 'F', 'Y'],
    'G': ['F', 'A', 'R']
}

# Define the start city
start_city = 'M'

# Define the destination cities
destination_cities = ['A', 'R']

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
    
    # If the path contains the destination cities twice
    if path.count(destination_cities[0]) == 2 and path.count(destination_cities[1]) == 2:
        return path
    
    # For each neighbor of the city
    for neighbor in adjacency_matrix[city]:
        # If the neighbor is not visited or the neighbor is a destination city
        if neighbor not in visited_cities or neighbor in destination_cities:
            # Call the DFS function
            result = dfs(neighbor, visited_cities, path)
            
            # If the result is not None
            if result is not None:
                return result
    
    # Remove the city from the path
    path.pop()
    
    # Remove the city from the visited cities
    visited_cities.remove(city)

# Call the DFS function
result = dfs(start_city, visited_cities, path)

# Print the result
print(result)
