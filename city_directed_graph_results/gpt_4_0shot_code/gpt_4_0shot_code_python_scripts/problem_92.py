
# Define the adjacency matrix
adj_matrix = {
    'I': ['E', 'J', 'L'],
    'H': ['I', 'G', 'S', 'W'],
    'R': ['H', 'E', 'G', 'W', 'B', 'V', 'L'],
    'E': ['H', 'Q', 'C'],
    'G': ['I'],
    'S': ['I', 'W', 'Q', 'J', 'L'],
    'W': ['I', 'R'],
    'Q': ['I', 'S', 'C', 'A', 'B'],
    'C': ['I', 'H', 'R', 'G', 'W', 'A', 'F', 'J', 'V'],
    'A': ['I', 'H', 'W'],
    'B': ['E', 'S', 'W', 'A', 'L'],
    'F': ['I', 'H', 'L'],
    'J': ['E', 'S', 'B'],
    'V': ['E', 'G', 'Q', 'A', 'B'],
    'L': ['E', 'G', 'Q']
}

# Define the DFS function
def dfs(city, visited, path):
    visited.add(city)
    path.append(city)
    
    if len(path) == 2 and path[-1] == 'R' and path[-2] == 'S':
        return path
    if len(path) == 2 and path[-1] == 'S' and path[-2] == 'R':
        return path
    
    for next_city in adj_matrix[city]:
        if next_city not in visited or (next_city in ['R', 'S'] and path.count(next_city) < 2):
            result = dfs(next_city, visited, path)
            if result:
                return result
    
    path.pop()
    visited.remove(city)

# Call the DFS function
visited = set()
path = []
result = dfs('F', visited, path)
print(result)
