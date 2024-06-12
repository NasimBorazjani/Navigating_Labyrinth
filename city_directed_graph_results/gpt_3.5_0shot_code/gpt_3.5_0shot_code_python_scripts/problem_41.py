
def dfs(city, visited, path, target, count, adj_matrix):
    visited[city] = True
    path.append(city)
    
    if city == target and count == 2:
        return path
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[i]:
            new_path = dfs(i, visited.copy(), path.copy(), target, count + (i == 'A' or i == 'Y'), adj_matrix)
            if new_path:
                return new_path
    
    return None

adj_matrix = [
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0]
]

start_city = 'E'
target_cities = ['A', 'Y']

for target_city in target_cities:
    visited = {chr(i + ord('A')): False for i in range(len(adj_matrix))}
    path = dfs(start_city, visited, [], target_city, 0, adj_matrix)
    
    if path:
        print(path)
