
def dfs(city, visited, path, target, target_count, adjacency_matrix):
    visited[city] = True
    path.append(city)
    
    if city == target:
        target_count[target] += 1
    
    if target_count['B'] == 2 and target_count['L'] == 2:
        return path
    
    for i, connected in enumerate(adjacency_matrix[city]):
        if connected == 1 and not visited[i]:
            result = dfs(chr(65 + i), visited.copy(), path.copy(), target, target_count, adjacency_matrix)
            if result:
                return result
    
    return None

adjacency_matrix = [
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]
]

visited = {chr(65 + i): False for i in range(len(adjacency_matrix))}
target_count = {city: 0 for city in ['B', 'L']}
path = []

result = dfs('D', visited, path, 'B', target_count, adjacency_matrix)

if result:
    print(result)
else:
    print("No valid path found")
