
def dfs(city, visited, count_F, count_W, path):
    visited[city] = True
    path.append(city)
    
    if city == 'F':
        count_F += 1
    elif city == 'W':
        count_W += 1
    
    if count_F > 2 or count_W > 2:
        return None
    
    if count_F == 2 and count_W == 2:
        return path
    
    for i, connected in enumerate(adj_matrix[city]):
        if connected == 1 and not visited[cities[i]]:
            result = dfs(cities[i], visited.copy(), count_F, count_W, path.copy())
            if result:
                return result
    
    return None

cities = ['R', 'T', 'C', 'F', 'S', 'X', 'Y', 'E', 'A', 'W']
adj_matrix = [
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 0]
]

start_city = 'C'
visited = {city: False for city in cities}
count_F = 0
count_W = 0
path = []

result = dfs(start_city, visited, count_F, count_W, path)

if result:
    print(result)
else:
    print("No valid path found")
