
# Define the adjacency matrix
adjacency_matrix = {
    'O': ['B'],
    'C': ['O', 'F', 'P'],
    'F': ['O', 'U', 'Q', 'G'],
    'W': ['O', 'C', 'U', 'I'],
    'I': ['C', 'U', 'B', 'G', 'S'],
    'P': ['F', 'W', 'B', 'H'],
    'U': ['C', 'I'],
    'B': ['F', 'U'],
    'H': ['C', 'F', 'W', 'I', 'P', 'B'],
    'Q': ['C', 'F', 'I', 'S', 'G'],
    'G': ['P'],
    'S': ['C', 'W', 'H', 'Q']
}

# Define the start city
start_city = 'G'

# Define the destination cities
destination_cities = ['F', 'U']

# Define the visited cities
visited_cities = []

# Define the path
path = []

# Define the DFS function
def dfs(city, visited_cities, path):
    visited_cities.append(city)
    path.append(city)

    if len(path) == 2 * len(destination_cities) + 1:
        if all(city in path for city in destination_cities) and path.count('F') == 2 and path.count('U') == 2:
            print(' -> '.join(path))
        path.pop()
        visited_cities.remove(city)
        return

    for next_city in adjacency_matrix[city]:
        if next_city not in visited_cities or (next_city in destination_cities and path.count(next_city) < 2):
            dfs(next_city, visited_cities, path)

    path.pop()
    visited_cities.remove(city)

# Call the DFS function
dfs(start_city, visited_cities, path)
