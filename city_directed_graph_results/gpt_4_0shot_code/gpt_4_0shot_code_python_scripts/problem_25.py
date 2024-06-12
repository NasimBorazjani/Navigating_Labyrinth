
# Define the adjacency matrix
adjacency_matrix = {
    'O': ['Z', 'L', 'R'],
    'M': ['V'],
    'Y': ['O', 'M', 'V', 'R'],
    'J': ['Z', 'F', 'X', 'L'],
    'Z': ['K'],
    'V': ['F'],
    'K': ['M', 'Y', 'Z', 'V'],
    'F': ['O', 'Y'],
    'X': ['J', 'Z', 'V', 'K'],
    'L': ['O', 'M', 'X', 'K'],
    'R': ['J', 'V', 'F']
}

# Define the start city and the destination cities
start_city = 'M'
destination_cities = ['X', 'Y']

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
paths = []
for city in destination_cities:
    paths.extend(find_all_paths(start_city, city))

# Filter the paths to only include those that visit both destination cities twice
valid_paths = [path for path in paths if path.count('X') == 2 and path.count('Y') == 2]

# Print the shortest valid path
print(min(valid_paths, key=len))
