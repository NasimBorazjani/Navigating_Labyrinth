
# Adjacency matrix
matrix = [
    "000001000100",
    "000010000000",
    "010000011000",
    "100010001000",
    "000100000101",
    "010000000110",
    "001000100010",
    "010000000110",
    "001000000101",
    "001000100010",
    "100000010100",
    "010001000100"
]

# Convert the adjacency matrix into a dictionary
graph = {city: [] for city in 'ZOFMCKBDURSJ'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '1':
            graph[chr(i+65)].append(chr(j+65))

# Recursive function for depth-first search
def dfs(city, visited, to_visit_twice):
    visited.append(city)
    if city in to_visit_twice:
        to_visit_twice.remove(city)
    for next_city in graph[city]:
        if next_city not in visited:
            dfs(next_city, visited, to_visit_twice)
    return visited

# List of cities to visit twice
to_visit_twice = ['C', 'D']

# Start the search from city 'Z'
path = dfs('Z', [], to_visit_twice)

# Return to city 'Z'
path.append('Z')

print(path)
