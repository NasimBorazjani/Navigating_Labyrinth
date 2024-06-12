
# Adjacency matrix
matrix = [
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
]

# Convert the adjacency matrix into a dictionary
graph = {city: {} for city in 'ZHMPBIEQLYVC'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[chr(i+65)][chr(j+65)] = matrix[i][j]
            graph[chr(j+65)][chr(i+65)] = matrix[i][j]

# DFS function
def dfs(graph, city, path, visited):
    path.append(city)
    visited[city] -= 1
    if len(path) == len(graph)*2:
        yield path
    else:
        for city in graph[path[-1]]:
            if visited.get(city, 0) > 0:
                for p in dfs(graph, city, list(path), visited):
                    yield p
    path.pop()
    visited[city] += 1

# Find the shortest route
shortest_route = None
for path in dfs(graph, 'C', ['C'], {'C': 2, 'M': 2, 'Q': 2}):
    if shortest_route is None or sum(graph[path[i]][path[i+1]] for i in range(len(path)-1)) < sum(graph[shortest_route[i]][shortest_route[i+1]] for i in range(len(shortest_route)-1)):
        shortest_route = path

print(shortest_route)
