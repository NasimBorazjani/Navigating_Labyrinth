
def dfs(city, visited, count_F, count_U, path):
    visited[city] = True
    path.append(city)
    
    if city == 'F':
        count_F += 1
    elif city == 'U':
        count_U += 1
    
    if count_F == 2 and count_U == 2:
        return path
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[city]:
            new_path = dfs(cities[i], visited.copy(), count_F, count_U, path.copy())
            if new_path:
                return new_path
    
    return None

cities = ['O', 'C', 'F', 'W', 'I', 'P', 'U', 'B', 'H', 'Q', 'G', 'S']
adj_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0]
]

start_city = 'G'
visited = {city: False for city in cities}
path = []

result = dfs(start_city, visited, 0, 0, path)

if result:
    print(result)
else:
    print("No path found")
