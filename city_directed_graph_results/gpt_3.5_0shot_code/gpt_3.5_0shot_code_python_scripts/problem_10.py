
def dfs(city, visited, path, count_PE):
    visited[city] = True
    path.append(city)
    
    if city == 'P' or city == 'E':
        count_PE[city] += 1
    
    if count_PE['P'] == 2 and count_PE['E'] == 2:
        return path
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[city]:
            new_path = dfs(cities[i], visited.copy(), path.copy(), count_PE.copy())
            if new_path:
                return new_path
    
    return None

cities = ['Q', 'O', 'P', 'T', 'W', 'E', 'X', 'M', 'D', 'V']
adj_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 0]
]

visited = {city: False for city in cities}
count_PE = {'P': 0, 'E': 0}

start_city = 'Q'
path = dfs(start_city, visited, [], count_PE)

print(path)
