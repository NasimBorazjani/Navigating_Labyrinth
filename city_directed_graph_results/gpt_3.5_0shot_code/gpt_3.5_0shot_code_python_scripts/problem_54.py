
def dfs(city, visited, path, target, count_A, count_Y, adj_matrix):
    visited[city] = True
    path.append(city)
    
    if city == target:
        if count_A == 2 and count_Y == 2:
            return path
        else:
            path.pop()
            visited[city] = False
            return None
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[i]:
            new_count_A = count_A
            new_count_Y = count_Y
            if i == 'A':
                new_count_A += 1
            elif i == 'Y':
                new_count_Y += 1
            
            result = dfs(i, visited, path, target, new_count_A, new_count_Y, adj_matrix)
            if result:
                return result
    
    path.pop()
    visited[city] = False
    return None

adj_matrix = {
    'G': [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    'T': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    'M': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'U': [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'K': [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    'Y': [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    'D': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    'A': [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    'P': [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    'R': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    'E': [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    'S': [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    'I': [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0]
}

start_city = 'R'
target_city = 'A'
visited = {city: False for city in adj_matrix.keys()}
path = []

result = dfs(start_city, visited, path, target_city, 0, 0, adj_matrix)
print(result)
