
def dfs(city, visited, path, target, count, graph):
    visited[city] = True
    path.append(city)
    
    if city == target and count == 2:
        return path
    
    for i, connected in enumerate(graph[city]):
        if connected == 1 and not visited[i]:
            new_path = dfs(i, visited.copy(), path.copy(), target, count + (i == target), graph)
            if new_path:
                return new_path
    
    return None

adjacency_matrix = [
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
]

start_city = 'T'
target_cities = ['V', 'I']

for target_city in target_cities:
    visited = [False] * len(adjacency_matrix)
    path = []
    result = dfs(start_city, visited, path, target_city, 0, adjacency_matrix)
    
    if result:
        print(result)
        break
