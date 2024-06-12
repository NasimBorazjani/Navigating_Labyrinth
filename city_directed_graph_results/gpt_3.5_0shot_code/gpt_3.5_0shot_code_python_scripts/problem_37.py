
def dfs(city, path, visited, count_M, count_Q, adj_matrix):
    path.append(city)
    visited.add(city)
    
    if city == 'M':
        count_M += 1
    elif city == 'Q':
        count_Q += 1
    
    if count_M > 2 or count_Q > 2:
        return None
    
    if count_M == 2 and count_Q == 2:
        return path
    
    for i, connected in enumerate(adj_matrix[city]):
        if connected == 1 and i not in visited:
            new_path = dfs(chr(65 + i), path.copy(), visited.copy(), count_M, count_Q, adj_matrix)
            if new_path:
                return new_path
    
    return None

adj_matrix = [
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
]

start_city = 'L'
visited = set()
count_M = 0
count_Q = 0

path = dfs(start_city, [], visited, count_M, count_Q, adj_matrix)

if path:
    print(path)
else:
    print("No valid path found")
