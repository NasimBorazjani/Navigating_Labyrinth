
def dfs(city, visited, path, target, target_count, adj_matrix):
    visited[city] = True
    path.append(city)
    
    if city == target:
        target_count[target] += 1
    
    if target_count[target] == 2 and target_count['E'] == 2:
        return path
    
    for i, connected in enumerate(adj_matrix[city]):
        if connected == 1 and not visited[i]:
            result = dfs(i, visited.copy(), path.copy(), target, target_count.copy(), adj_matrix)
            if result:
                return result
    
    return None

adj_matrix = [
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 0]
]

start_city = 'Q'
target_cities = ['T', 'E']
target_count = {city: 0 for city in target_cities}

result = dfs(start_city, [False] * len(adj_matrix), [], 'T', target_count, adj_matrix)

print(result)
