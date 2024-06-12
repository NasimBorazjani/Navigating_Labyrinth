
def dfs(city, visited, path, count_J, count_K):
    visited[city] = True
    path.append(city)
    
    if city == 'J':
        count_J += 1
    elif city == 'K':
        count_K += 1
    
    if count_J > 2 or count_K > 2:
        return
    
    if count_J == 2 and count_K == 2:
        print(path)
        return
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[city]:
            dfs(cities[i], visited.copy(), path.copy(), count_J, count_K)

cities = ['L', 'A', 'J', 'U', 'E', 'P', 'Q', 'Y', 'H', 'R', 'K', 'M', 'F']
adj_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0]
]

visited = {city: False for city in cities}
dfs('L', visited, [], 0, 0)
