
# Define the adjacency matrix
adjacency_matrix = {
    'Y': ['O', 'R', 'A', 'U', 'M', 'L'],
    'O': ['A'],
    'Q': ['Y', 'X', 'R', 'M'],
    'X': ['Y', 'Q', 'R', 'M', 'L'],
    'K': ['O', 'X', 'A'],
    'R': ['K'],
    'A': ['X', 'R', 'M', 'L'],
    'U': ['L'],
    'M': ['Q'],
    'L': ['O']
}

# Define the start city and the destination cities
start_city = 'U'
destination_cities = ['A', 'X']

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
valid_paths = [path for path in paths if path.count('A') == 2 and path.count('X') == 2]

# Print the shortest valid path
print(min(valid_paths, key=len))
