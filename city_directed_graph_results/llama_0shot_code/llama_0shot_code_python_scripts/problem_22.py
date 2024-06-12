
# Adjacency matrix
adjacency_matrix = [
    "0011001100",
    "0001100100",
    "0010001100",
    "1000110100",
    "1011000110",
    "1111011101",
    "0100001110",
    "0000111101",
    "0011101100",
    "1000011010",
    "0111100010"
]

# Convert adjacency matrix into dictionary
graph = {city: [] for city in 'XMUNTVZSFEJ'}
for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] == '1':
            graph[chr(i+65)].append(chr(j+65))

# Depth-first search function
def dfs(current, to_visit, path, shortest_path):
    if not to_visit:
        if current == 'X' and len(path) < len(shortest_path):
            return path
    else:
        for city in to_visit:
            if city in graph[current]:
                new_to_visit = to_visit - {city}
                new_path = path + [city]
                shortest_path = dfs(city, new_to_visit, new_path, shortest_path)
    return shortest_path

# Call depth-first search function
shortest_path = dfs('X', set(graph) - {'X', 'E', 'T'}, ['X'], ['X'])

# Print result
print(shortest_path)
