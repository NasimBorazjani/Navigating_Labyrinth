
# Adjacency matrix
adjacency_matrix = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 0]
]

# Dictionary representation of the adjacency matrix
graph = {
    'M': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    'U': [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    'B': [1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    'F': [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    'V': [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    'Z': [0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    'P': [1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    'N': [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    'E': [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    'H': [1, 0, 1, 0, 1, 1, 0, 0, 0, 0]
}

# Function to perform depth-first search
def dfs(graph, city, visited, path):
    # Mark the current city as visited
    visited[city] = True
    # Add the current city to the path
    path.append(city)

    # If we have visited all cities twice, return the path
    if path.count('M') == 2 and path.count('H') == 2:
        return path

    # Visit all neighbors of the current city
    for neighbor in graph[city]:
        if neighbor not in visited:
            # Recursively visit the neighbor
            result = dfs(graph, chr(ord('A') + neighbor), visited, path)
            # If we have found a path, return it
            if result is not None:
                return result

    # If no path is found, backtrack and remove the current city from the path
    path.pop()
    visited[city] = False
    return None

# Start from city 'N'
start_city = 'N'
# Create a set to keep track of visited cities
visited = [False] * len(graph)
# Create a list to store the path
path = []
# Perform depth-first search
result = dfs(graph, start_city, visited, path)
# Print the path as a list of city names
print(result)
