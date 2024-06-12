
# Define the adjacency matrix
matrix = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0]
]

# Define the cities
cities = ['D', 'Z', 'T', 'X', 'L', 'K', 'N', 'H', 'U', 'A', 'Q', 'B', 'Y']

# Define the start city
start = 'H'

# Define the destination cities
destinations = ['B', 'X']

# Define the visited cities
visited = []

# Define the path
path = []

# Define the DFS function
def dfs(city, visited, path):
    visited.append(city)
    path.append(city)
    if len(path) == len(cities) and path.count('B') == 2 and path.count('X') == 2:
        return path
    for i in range(len(matrix[cities.index(city)])):
        if matrix[cities.index(city)][i] == 1 and cities[i] not in visited:
            result = dfs(cities[i], visited, path)
            if result:
                return result
    path.pop()
    visited.pop()

# Call the DFS function
result = dfs(start, visited, path)

# Print the result
print(result)
