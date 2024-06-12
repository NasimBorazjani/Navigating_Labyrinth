
# Adjacency matrix
adjacency_matrix = [
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
]

# Convert adjacency matrix to dictionary
graph = {city: {} for city in 'KBAZSHOEUV'}
for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] == 1:
            graph[chr(i+65)][chr(j+65)] = True

# DFS function
def dfs(graph, city, path, visited):
    path.append(city)
    visited[city] = visited.get(city, 0) + 1

    if visited[city] == 2 and city in ['K', 'Z']:
        return path

    for next_city in graph[city]:
        if next_city not in visited or visited[next_city] < 2:
            result = dfs(graph, next_city, path, visited)
            if result:
                return result

    path.pop()
    visited[city] -= 1

# Start DFS from 'H'
path = dfs(graph, 'H', [], {})

# Print the path
print(path)
