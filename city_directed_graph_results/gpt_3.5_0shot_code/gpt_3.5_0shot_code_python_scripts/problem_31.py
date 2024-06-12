
def dfs(city, visited, count_U, count_E, path, adj_matrix):
    visited[city] = True
    path.append(city)
    
    if city == 'U':
        count_U += 1
    elif city == 'E':
        count_E += 1
    
    if count_U > 2 or count_E > 2:
        return None
    
    if count_U == 2 and count_E == 2:
        return path
    
    for i, connected in enumerate(adj_matrix[city]):
        if connected == 1 and not visited[chr(65+i)]:
            new_path = dfs(chr(65+i), visited.copy(), count_U, count_E, path.copy(), adj_matrix)
            if new_path:
                return new_path
    
    return None

adj_matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0]
]

visited = {chr(65+i): False for i in range(11)}
start_city = 'J'
path = dfs(start_city, visited, 0, 0, [], adj_matrix)

print(path)
