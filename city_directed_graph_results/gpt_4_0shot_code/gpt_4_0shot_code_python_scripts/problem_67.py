
# Define the adjacency matrix
adjacency_matrix = {
    'A': ['Q', 'N'],
    'K': ['D', 'X'],
    'G': ['K', 'Z'],
    'U': ['R'],
    'Q': ['Y', 'R'],
    'D': ['A', 'K', 'Q', 'V', 'Y'],
    'N': ['G', 'Q', 'Y'],
    'X': ['A', 'U', 'N'],
    'S': ['A', 'K', 'Q', 'X', 'R'],
    'V': ['G', 'N', 'X', 'S'],
    'Y': ['A', 'Q'],
    'R': ['K', 'X', 'N', 'Y'],
    'Z': ['A', 'K', 'U', 'X', 'S', 'V', 'Y', 'R']
}

# Define the start city
start_city = 'S'

# Define the destination cities
destination_cities = ['N', 'R']

# Define the visited cities
visited_cities = []

# Define the path
path = []

# Define the DFS function
def dfs(city, visited_cities, path):
    visited_cities.append(city)
    path.append(city)

    if set(destination_cities).issubset(set(path)) and len(path) == len(set(path)):
        print(' -> '.join(path))
        return

    for next_city in adjacency_matrix[city]:
        if next_city not in visited_cities or next_city in destination_cities:
            dfs(next_city, visited_cities, path)
            path.pop()
            visited_cities.pop()

# Call the DFS function
dfs(start_city, visited_cities, path)
