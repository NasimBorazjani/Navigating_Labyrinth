
# Define the adjacency matrix
adjacency_matrix = {
    'A': ['M', 'O', 'E', 'G', 'P'],
    'N': ['Q', 'P'],
    'B': ['Z', 'Q', 'G'],
    'M': ['N', 'E'],
    'Z': ['O', 'Q'],
    'O': ['M', 'E', 'Q', 'L'],
    'E': ['A', 'B', 'M', 'Z', 'G', 'P'],
    'Q': ['M'],
    'G': ['N', 'M', 'Q'],
    'L': ['N', 'Q', 'G', 'P'],
    'P': ['E', 'L']
}

# Define the start city and the destination cities
start_city = 'B'
destination_cities = ['E', 'N']

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
valid_paths = [path for path in paths if path.count('E') == 2 and path.count('N') == 2]

# Print the shortest valid path
print(min(valid_paths, key=len))
