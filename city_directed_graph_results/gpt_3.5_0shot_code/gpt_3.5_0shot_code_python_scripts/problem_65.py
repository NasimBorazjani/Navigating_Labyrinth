
def dfs(city, visited, path, target, count, graph):
    visited[city] = True
    path.append(city)
    
    if city == target and count == 2:
        return path
    
    for i, connected in enumerate(graph[city]):
        if connected == 1 and not visited[i]:
            new_path = dfs(i, visited.copy(), path.copy(), target, count + (i == 'F' or i == 'N'), graph)
            if new_path:
                return new_path
    
    return None

# Adjacency matrix representing the connections between cities
graph = [
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0]
]

start_city = 'Q'
target_cities = ['F', 'N']

for target in target_cities:
    visited = {chr(i + ord('A')): False for i in range(len(graph))}
    path = dfs(start_city, visited, [], target, 0, graph)
    
    if path:
        print(path)
        break
