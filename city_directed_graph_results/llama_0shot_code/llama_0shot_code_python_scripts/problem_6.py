
# Adjacency matrix
adj_matrix = [
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
]

# Convert adjacency matrix into dictionary
graph = {city: [] for city in 'FIONJKDNRMB'}
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix[i])):
        if adj_matrix[i][j] == 1:
            graph[chr(i+65)].append(chr(j+65))

# Function to perform depth-first search
def dfs(city, visited, path):
    visited.add(city)
    path.append(city)
    
    if len(path) == len(graph) - 2:  # Visit F and D twice each
        return path + [city] * 4       # Add two more visits to the current city
    
    for neighbour in graph[city]:
        if neighbour not in visited:
            result = dfs(neighbour, visited, path)
            if result:
                return result
    
    path.pop()  # Backtrack
    return None

# Start from city 'N'
start_city = 'N'
visited = set()
path = []
result = dfs(start_city, visited, path)
print(result)
