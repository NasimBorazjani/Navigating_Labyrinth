
import sys

# Adjacency matrix
adj_matrix = [
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0]
]

# List of city names
city_names = list('CQTKMBAJDYVONP')

# Function to perform DFS
def dfs(city, path, visited, adj_matrix):
    # Mark the current city as visited
    visited[city] = True
    # Add the current city to the path
    path.append(city)

    # Visit all the cities that can be reached directly from the current city
    for i in range(len(adj_matrix)):
        if adj_matrix[city][i] == 1 and not visited[i]:
            dfs(i, path, visited, adj_matrix)

    # Backtrack: remove the current city from the path
    path.pop()
    # Mark the current city as unvisited
    visited[city] = False

# Start from city 'M'
start_city = city_names.index('M')
# List to store the path
path = []
# Boolean array to mark the visited cities
visited = [False] * len(city_names)

# Call the DFS function
dfs(start_city, path, visited, adj_matrix)

# Print the path
print(path)
