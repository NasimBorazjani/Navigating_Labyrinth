
def dfs(city, visited, count_K, count_Z, path):
    visited[city] = True
    path.append(city)
    
    if city == 'K':
        count_K += 1
    elif city == 'Z':
        count_Z += 1
    
    if count_K == 2 and count_Z == 2:
        return path
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[city]:
            new_path = dfs(chr(65+i), visited.copy(), count_K, count_Z, path.copy())
            if new_path:
                return new_path
    
    return None

adj_matrix = [
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
]

start_city = 'H'
visited = {chr(65+i): False for i in range(len(adj_matrix))}
path = []

result = dfs(start_city, visited, 0, 0, path)

if result:
    print(result)
else:
    print("No valid path found")
