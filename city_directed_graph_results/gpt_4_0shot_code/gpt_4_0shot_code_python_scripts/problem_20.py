
# Define the adjacency matrix
adjacency_matrix = {
    'F': ['D'],
    'I': ['R'],
    'Y': ['N'],
    'R': ['F', 'M', 'D'],
    'X': ['R', 'Q'],
    'Q': ['I', 'M'],
    'M': ['F', 'R', 'X', 'N'],
    'S': ['F', 'I', 'X', 'Q'],
    'C': ['I', 'Y', 'R', 'S'],
    'D': ['Y', 'X', 'M'],
    'N': ['X', 'C']
}

# Define the start city and the destination cities
start_city = 'F'
destination_cities = ['N', 'I']

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
valid_paths = [path for path in paths_to_destinations if path.count('N') == 2 and path.count('I') == 2]

# Print the shortest valid path
print(min(valid_paths, key=len))
