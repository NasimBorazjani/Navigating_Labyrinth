
# Define the adjacency matrix
adj_matrix = {
    'A': ['Z', 'O', 'E', 'T', 'G'],
    'P': ['A', 'I'],
    'Z': ['L', 'X', 'D'],
    'O': ['A', 'I', 'G'],
    'R': ['P', 'Z', 'X', 'T', 'W'],
    'I': ['Q'],
    'L': ['A', 'P', 'O', 'R', 'W', 'D', 'S'],
    'X': ['E', 'S'],
    'E': ['O', 'L', 'G'],
    'T': ['I', 'L', 'E'],
    'W': ['Z', 'L', 'E', 'D', 'Q'],
    'D': ['A', 'O', 'I', 'L', 'T', 'Q'],
    'S': ['A', 'P', 'Z', 'I', 'E', 'D', 'Q'],
    'G': ['P', 'X', 'E', 'W'],
    'Q': ['A', 'Z', 'O', 'X', 'T', 'S']
}

# Define the DFS function
def dfs(city, visited, path):
    visited.add(city)
    path.append(city)
    
    if len(path) > 4 and path[0] == 'E' and path.count('A') == 2 and path.count('P') == 2:
        return path
    
    for next_city in adj_matrix[city]:
        if next_city not in visited or (next_city in ['A', 'P'] and path.count(next_city) < 2):
            result = dfs(next_city, visited, path)
            if result:
                return result
    
    path.pop()
    visited.remove(city)

# Call the DFS function
result = dfs('E', set(), [])
print(result)
