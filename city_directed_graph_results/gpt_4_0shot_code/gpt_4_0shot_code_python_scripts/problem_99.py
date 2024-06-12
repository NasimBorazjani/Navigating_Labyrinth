
# Define the adjacency matrix
adjacency_matrix = {
    'R': ['F', 'M', 'C', 'G'],
    'P': ['R', 'T', 'E', 'W', 'M', 'G'],
    'Z': ['H', 'E', 'M', 'D', 'Y'],
    'U': ['P', 'E', 'Y'],
    'H': ['R', 'U', 'E', 'F', 'M', 'L', 'Y', 'C'],
    'T': ['U', 'H', 'D'],
    'E': ['T', 'H', 'W', 'D', 'G'],
    'W': ['R', 'Z', 'H', 'E', 'Y', 'G'],
    'F': ['Z', 'U', 'H', 'W', 'M'],
    'M': ['H', 'W'],
    'D': ['P', 'T', 'E', 'C'],
    'L': ['U', 'M'],
    'Y': ['R', 'Z', 'H', 'W', 'F', 'G'],
    'C': ['U', 'F', 'Y'],
    'G': ['Z', 'W', 'M', 'D', 'Y']
}

# Define the start city and the destination cities
start_city = 'L'
destination_cities = ['W', 'P']

# Define a function to perform a depth-first search
def dfs(city, visited, path):
    # Mark the current city as visited
    visited.add(city)
    path.append(city)

    # If we have visited the destination cities twice, return the path
    if path.count(destination_cities[0]) == 2 and path.count(destination_cities[1]) == 2:
        return path

    # Visit all the cities connected to the current city
    for next_city in adjacency_matrix[city]:
        if next_city not in visited or next_city in destination_cities:
            result = dfs(next_city, visited, path)
            if result:
                return result

    # Backtrack
    path.pop()
    visited.remove(city)

# Perform a depth-first search from the start city
path = dfs(start_city, set(), [])

# Print the quickest route
print(path)
