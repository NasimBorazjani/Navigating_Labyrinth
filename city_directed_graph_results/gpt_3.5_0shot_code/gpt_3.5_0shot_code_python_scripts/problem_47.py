
def dfs(city, visited, path, adj_matrix, target, count):
    visited[city] = True
    path.append(city)
    
    if city == target and count == 2:
        return path
    
    for i, connected in enumerate(adj_matrix[city]):
        if connected == 1 and not visited[i]:
            new_path = dfs(i, visited.copy(), path.copy(), adj_matrix, target, count + (i == 'C') + (i == 'D'))
            if new_path:
                return new_path
    
    return None

adj_matrix = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0]
]

start_city = 'Z'
target_cities = ['C', 'D']

for target_city in target_cities:
    visited = {chr(i + ord('A')): False for i in range(12)}
    path = dfs(start_city, visited, [], adj_matrix, target_city, 0)
    
    if path:
        print(path)
