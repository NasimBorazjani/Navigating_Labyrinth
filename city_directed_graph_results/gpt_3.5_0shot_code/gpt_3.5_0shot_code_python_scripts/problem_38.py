
def dfs(city, visited, path, target, count_V, count_F, adj_matrix):
    visited[city] = True
    path.append(city)
    
    if city == target:
        if target == 'V':
            count_V += 1
        elif target == 'F':
            count_F += 1
        
        if count_V == 2 and count_F == 2:
            return path
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[i]:
            new_path = dfs(chr(65 + i), visited.copy(), path.copy(), target, count_V, count_F, adj_matrix)
            if new_path:
                return new_path
    
    return None

adj_matrix = [
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]
]

start_city = 'Q'
visited = [False] * len(adj_matrix)
path = []
count_V = 0
count_F = 0

result = dfs(start_city, visited, path, 'V', count_V, count_F, adj_matrix)

if result:
    print(result)
else:
    print("No valid path found")
