
# Define the adjacency matrix
adjacency_matrix = {
    'R': ['E', 'G', 'Z'],
    'L': ['G', 'A'],
    'F': ['Q'],
    'E': ['Q', 'U'],
    'D': ['R', 'E', 'H', 'A'],
    'Q': ['R', 'L', 'U', 'H'],
    'G': ['L', 'F', 'E', 'D', 'U', 'H'],
    'U': ['D', 'H', 'Z', 'A'],
    'H': ['R', 'F', 'Z'],
    'T': ['L', 'D', 'H', 'Z'],
    'Z': ['R', 'F', 'D', 'Q', 'H'],
    'A': ['D', 'Q', 'T']
}

# Define the start city
start_city = 'F'

# Define the destination cities
destination_cities = ['R', 'A']

# Define the visited cities
visited_cities = []

# Define the path
path = []

# Define the function to find the quickest route
def find_route(city, visited, path):
    visited.append(city)
    path.append(city)

    if len(path) == len(visited_cities) + 2:
        if path.count('R') == 2 and path.count('A') == 2:
            print(' -> '.join(path))
        path.pop()
        visited.remove(city)
        return

    for neighbour in adjacency_matrix[city]:
        if neighbour not in visited or (neighbour in destination_cities and path.count(neighbour) < 2):
            find_route(neighbour, visited, path)

    path.pop()
    visited.remove(city)

# Find the quickest route
find_route(start_city, visited_cities, path)
