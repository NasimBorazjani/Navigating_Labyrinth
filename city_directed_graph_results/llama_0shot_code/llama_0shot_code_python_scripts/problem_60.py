
# Adjacency matrix
adjacency_matrix = [
    "000001011000",
    "000010100000",
    "100010000000",
    "010000000000",
    "000000000101",
    "000000010011",
    "110000000100",
    "011000010000",
    "001100010000",
    "001000100000",
    "000000000000",
    "000110000100",
    "000001100000"
]

# Convert adjacency matrix into dictionary
graph = {city: [] for city in 'HTRFLEUQGNEYIX'}
for i, row in enumerate(adjacency_matrix):
    for j, col in enumerate(row):
        if col == '1':
            graph[chr(i+65)].append(chr(j+65))

# DFS function
def dfs(city, visited, path):
    # Add city to visited list and to path
    visited.append(city)
    path.append(city)

    # Visit all cities that can be reached from current city and that have not been visited yet
    for next_city in graph[city]:
        if next_city not in visited or (next_city in ['F', 'U'] and visited.count(next_city) < 2):
            dfs(next_city, visited, path)

    # Backtrack
    path.pop()
    visited.pop()

# Start DFS
path = []
dfs('I', [], path)

# Print solution
print(path)
