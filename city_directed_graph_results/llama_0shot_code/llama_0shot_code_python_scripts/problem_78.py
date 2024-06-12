
# Adjacency matrix
matrix = [
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
]

# List of cities
cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']

# Function to perform DFS
def dfs(city, visited, path):
    # Mark the current city as visited
    visited[city] = True
    # Add the current city to the path
    path.append(cities[city])

    # Visit all the cities that can be reached directly from the current city
    for i in range(len(matrix[city])):
        if matrix[city][i] == 1 and not visited[i]:
            dfs(i, visited, path)

    return path

# Start from city A
start_city = 0
# Perform DFS
path = dfs(start_city, [False]*len(matrix), [])

# Print the path
print(path)
