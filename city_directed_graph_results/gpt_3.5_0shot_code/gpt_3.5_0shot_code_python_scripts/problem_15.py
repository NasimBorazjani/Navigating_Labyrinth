
def dfs(city, visited, path, count_W, count_X):
    visited[city] = True
    path.append(city)
    
    if city == 'W':
        count_W += 1
    elif city == 'X':
        count_X += 1
    
    if count_W == 2 and count_X == 2:
        return path
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[city]:
            new_path = dfs(cities[i], visited.copy(), path.copy(), count_W, count_X)
            if new_path:
                return new_path
    
    return None

cities = ['U', 'W', 'A', 'J', 'K', 'H', 'E', 'X', 'R', 'T']
adj_matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 0, 1, 0, 0]
]

start_city = 'E'
visited = {city: False for city in cities}
path = []

result = dfs(start_city, visited, path, 0, 0)
print(result)
