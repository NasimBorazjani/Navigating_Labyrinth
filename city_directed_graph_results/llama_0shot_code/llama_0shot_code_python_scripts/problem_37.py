
# Adjacency matrix
adjacency_matrix = [
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

# Convert adjacency matrix into dictionary
graph = {city: [] for city in 'RQYUFKMTXWHLA'}
for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] == 1:
            graph[chr(i + ord('A'))].append(chr(j + ord('A')))

# Depth-first search function
def dfs(city, visited):
    if city == 'M' and visited.count('M') == 2:
        return [city]
    if city == 'Q' and visited.count('Q') == 2:
        return [city]
    if city not in visited:
        visited.append(city)
        for next_city in graph[city]:
            path = dfs(next_city, visited)
            if path:
                return [city] + path
        visited.remove(city)
    return []

# Find quickest route
route = dfs('L', [])
print(route)
