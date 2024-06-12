
# Adjacency matrix
matrix = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# List of city names
cities = ['E', 'V', 'G', 'W', 'U', 'F', 'S', 'H', 'K', 'B', 'Z', 'N', 'L', 'J']

# Start city
start = 'K'

# Function to perform DFS
def dfs(city, path, visited, f_count, z_count):
    # If we have visited the city twice and it's not the start city, add it to the path
    if visited[city] == 2 and city != start:
        path.append(city)
        return True
    # If we have visited the city more than twice or it's the start city, skip it
    if visited[city] >= 2 or city == start:
        return False
    # Mark the city as visited
    visited[city] += 1
    path.append(city)
    # Visit all the cities that can be reached from the current city
    for i in range(len(matrix)):
        if matrix[city][i] == 1:
            if dfs(i, path, visited, f_count, z_count):
                return True
    # If we haven't found the solution, backtrack
    path.pop()
    visited[city] -= 1
    return False

# Function to find the quickest route
def find_route():
    # List to store the path
    path = [start]
    # List to store the number of times each city has been visited
    visited = [0] * len(matrix)
    # Number of times we have visited cities 'F' and 'Z'
    f_count = z_count = 0
    # Perform DFS
    dfs('K', path, visited, f_count, z_count)
    return path

# Print the quickest route
print(find_route())
