
# Define the adjacency matrix
adjacency_matrix = {
    'P': ['H', 'R'],
    'G': ['V', 'M'],
    'W': ['L', 'B', 'S', 'D'],
    'V': ['L', 'S', 'N'],
    'L': ['G', 'M', 'B', 'S', 'N'],
    'M': ['W', 'V', 'J', 'D'],
    'B': ['P', 'G', 'L', 'H', 'D'],
    'S': ['G', 'L', 'N'],
    'J': ['W', 'V', 'L', 'B'],
    'H': ['P', 'W', 'M', 'B', 'S', 'R'],
    'D': ['G', 'V', 'J', 'N', 'R'],
    'N': ['J', 'H', 'D'],
    'R': ['G', 'V', 'M', 'H', 'N']
}

# Define the DFS function
def dfs(city, visited, path):
    visited[city] += 1
    path.append(city)

    if len(path) > 4 and path[-1] == 'P':
        if visited['G'] == 2 and visited['J'] == 2:
            print(' -> '.join(path))
        path.pop()
        visited[city] -= 1
        return

    for neighbour in adjacency_matrix[city]:
        if visited[neighbour] < 2:
            dfs(neighbour, visited, path)

    path.pop()
    visited[city] -= 1

# Initialize the visited dictionary
visited = {city: 0 for city in adjacency_matrix.keys()}

# Call the DFS function
dfs('P', visited, [])
