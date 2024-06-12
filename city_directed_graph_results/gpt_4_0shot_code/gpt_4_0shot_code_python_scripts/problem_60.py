
# Define the adjacency matrix
adjacency_matrix = {
    'H': ['Q', 'N', 'E'],
    'T': ['L', 'N'],
    'R': ['H', 'L', 'G', 'X'],
    'F': ['T', 'R', 'Q'],
    'L': ['F', 'Y', 'X'],
    'U': ['G', 'Y', 'X'],
    'Q': ['F', 'E', 'Y'],
    'G': ['H', 'T', 'F', 'L', 'E'],
    'N': ['T', 'L', 'U', 'G'],
    'E': ['R', 'F', 'G'],
    'Y': ['R', 'Q', 'G'],
    'I': ['H'],
    'X': ['L', 'U', 'Q', 'I']
}

# Define the start city and destination cities
start_city = 'I'
destination_cities = ['F', 'U']

# Define a function to find all paths
def find_all_paths(start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in adjacency_matrix:
        return []
    paths = []
    for node in adjacency_matrix[start]:
        if node not in path:
            newpaths = find_all_paths(node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Find all paths from the start city to the destination cities
paths_to_destinations = []
for city in destination_cities:
    paths_to_destinations.extend(find_all_paths(start_city, city))

# Filter the paths to only include those that visit each destination city twice
valid_paths = [path for path in paths_to_destinations if path.count('F') == 2 and path.count('U') == 2]

# Print the shortest valid path
print(min(valid_paths, key=len))
