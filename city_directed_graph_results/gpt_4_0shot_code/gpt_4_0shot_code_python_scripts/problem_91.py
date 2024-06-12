
# Define the adjacency matrix
matrix = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
]

# Define the cities
cities = ['O', 'F', 'U', 'W', 'T', 'Y', 'A', 'Z', 'S', 'G', 'X', 'H', 'D', 'M', 'Q']

# Define the start city
start = 'A'

# Define the destination cities
destinations = ['G', 'O']

# Define the visited cities
visited = []

# Define the path
path = []

# Define the DFS function
def dfs(city, visited, path):
    visited.append(city)
    path.append(city)
    if city in destinations:
        destinations.remove(city)
    if len(destinations) == 0:
        return path
    for i in range(len(matrix[cities.index(city)])):
        if matrix[cities.index(city)][i] == 1 and cities[i] not in visited:
            return dfs(cities[i], visited, path)
    path.pop()
    return dfs(path[-1], visited, path)

# Call the DFS function
path = dfs(start, visited, path)

# Print the path
print(path)
