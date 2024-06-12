
# Define the adjacency matrix
adjacency_matrix = {
    'S': ['H'],
    'E': ['F', 'B', 'I', 'Z'],
    'D': ['B'],
    'Y': ['E', 'D', 'C', 'Z'],
    'F': ['B', 'O', 'U', 'I'],
    'B': ['S', 'D', 'Y', 'U', 'C'],
    'O': ['S', 'C', 'Q', 'J'],
    'H': ['Y', 'F', 'Q', 'J'],
    'U': ['S', 'D', 'Y', 'H', 'C'],
    'I': ['O', 'Z'],
    'C': ['I'],
    'Q': ['D', 'F', 'U', 'J'],
    'Z': ['E', 'D', 'O', 'H'],
    'J': ['E', 'D', 'Y', 'F', 'U']
}

# Define the DFS function
def dfs(city, path, visited, b_count, h_count):
    if city == 'B':
        b_count += 1
    if city == 'H':
        h_count += 1
    if b_count > 2 or h_count > 2:
        return
    if b_count == 2 and h_count == 2:
        print(path)
        return
    visited.add(city)
    for next_city in adjacency_matrix[city]:
        if next_city not in visited or next_city in ['B', 'H']:
            dfs(next_city, path + [next_city], visited.copy(), b_count, h_count)

# Call the DFS function
dfs('O', ['O'], set(), 0, 0)
