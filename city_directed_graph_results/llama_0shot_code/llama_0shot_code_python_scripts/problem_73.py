
import itertools

# Adjacency matrix
adj_matrix = [
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
]

# Convert adjacency matrix to dictionary
graph = {city: [] for city in 'KNYOSITDMBZREBF'}
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix[i])):
        if adj_matrix[i][j] == 1:
            graph[chr(i+65)].append(chr(j+65))

# DFS function
def dfs(city, path, visited):
    path.append(city)
    if city in ['S', 'K'] and path.count(city) == 2:
        return path
    for next_city in graph[city]:
        if next_city not in visited:
            visited.add(next_city)
            result = dfs(next_city, path, visited)
            if result:
                return result
    path.pop()
    visited.remove(city)

# Start DFS from 'Y'
path = dfs('Y', [], set('Y'))

# Print the path
print(path)
