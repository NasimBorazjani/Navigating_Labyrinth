
from collections import defaultdict

# Define the adjacency matrix
matrix = [
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
]

# Define the cities
cities = ['J', 'H', 'X', 'L', 'F', 'A', 'P', 'M', 'D', 'R', 'T', 'Z', 'N', 'K']

# Create a dictionary to store the graph
graph = defaultdict(list)

# Populate the graph with the adjacency matrix
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[cities[i]].append(cities[j])

# Define the DFS function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

# Define the function to find the quickest route
def find_route(graph, start, destinations):
    visited = dfs(graph, start)
    route = [start]
    for destination in destinations:
        if destination not in visited:
            return None
        route.append(destination)
        visited.remove(destination)
    return route

# Find the quickest route
route = find_route(graph, 'X', ['K', 'N', 'K', 'N'])

# Print the route
print(route)
