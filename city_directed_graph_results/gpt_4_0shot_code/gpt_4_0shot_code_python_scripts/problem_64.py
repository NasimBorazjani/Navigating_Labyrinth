
from collections import defaultdict

# Define the adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0]
]

# Define the cities
cities = ['Z', 'J', 'T', 'D', 'W', 'L', 'P', 'Y', 'V', 'H', 'R', 'I', 'A']

# Create a dictionary to map cities to their indices
city_to_index = {city: index for index, city in enumerate(cities)}

# Create a graph from the adjacency matrix
graph = defaultdict(list)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[cities[i]].append(cities[j])

# Define the start city and the destination cities
start_city = 'Y'
destination_cities = ['D', 'R']

# Define a function to perform depth-first search
def dfs(city, visited, path):
    visited[city] += 1
    path.append(city)
    
    if len(path) > 2 and city == start_city:
        if all(visited[city] == 2 for city in destination_cities):
            result.append(path.copy())
    else:
        for next_city in graph[city]:
            if visited[next_city] < 2:
                dfs(next_city, visited, path)
    
    visited[city] -= 1
    path.pop()

# Initialize the visited dictionary and the result list
visited = defaultdict(int)
result = []

# Perform depth-first search
dfs(start_city, visited, [])

# Print the quickest route
print(result[0])
