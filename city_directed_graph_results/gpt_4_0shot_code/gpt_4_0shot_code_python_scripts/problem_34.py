
# Define the adjacency matrix
adjacency_matrix = {
    'J': ['N'],
    'S': ['W', 'Z'],
    'T': ['B'],
    'W': ['J', 'S', 'G', 'P', 'U'],
    'G': ['S', 'W', 'Z', 'U'],
    'N': ['T', 'W', 'G', 'P', 'U'],
    'M': ['W'],
    'Z': ['N', 'B', 'U'],
    'B': ['J', 'G', 'M'],
    'P': ['T', 'N', 'M'],
    'U': ['J', 'G', 'N', 'P']
}

# Define the start city and the destination cities
start_city = 'T'
destination_cities = ['N', 'W']

# Define a function to find the quickest route
def find_route(start_city, destination_cities, adjacency_matrix):
    visited_cities = [start_city]
    stack = [(start_city, visited_cities)]
    while stack:
        (city, path) = stack.pop()
        for next_city in adjacency_matrix[city]:
            if next_city in destination_cities and path.count(next_city) < 2:
                new_path = path + [next_city]
                stack.append((next_city, new_path))
                if len(new_path) >= 6 and new_path.count('N') == 2 and new_path.count('W') == 2:
                    return new_path
            elif next_city not in path:
                new_path = path + [next_city]
                stack.append((next_city, new_path))

# Print the quickest route
print(find_route(start_city, destination_cities, adjacency_matrix))
