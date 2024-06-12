
# Adjacency matrix
adjacency_matrix = [
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
]

# Convert adjacency matrix to dictionary
graph = {city: [] for city in 'JXUIRTYBMD'}
for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] == 1:
            graph[chr(i + ord('J'))].append(chr(j + ord('J')))

# DFS function
def dfs(current, to_visit, path):
    if not to_visit:  # All cities have been visited
        return path + [current]  # Return to the starting city
    for city in graph[current]:  # For each city that can be reached directly
        if city in to_visit:  # If the city is in the list of cities left to visit
            to_visit.remove(city)  # Remove it from the list
            path.append(current)  # Append the current city to the path
            return dfs(city, to_visit, path)  # Call the DFS function recursively

# Call the DFS function
path = dfs('E', list('T' * 2 + 'Y' * 2), [])

# Print the path
print(path)
