
def dfs(city, visited, count_Y, count_I, path):
    visited[city] = True
    path.append(city)
    
    if city == 'Y':
        count_Y += 1
    elif city == 'I':
        count_I += 1
    
    if count_Y == 2 and count_I == 2:
        return path
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[city]:
            new_path = dfs(cities[i], visited.copy(), count_Y, count_I, path.copy())
            if new_path:
                return new_path
    
    return None

cities = ['I', 'V', 'F', 'E', 'Y', 'A', 'Z', 'T', 'H', 'Q']
adj_matrix = [
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
]

start_city = 'V'
visited = {city: False for city in cities}
path = []

result = dfs(start_city, visited, 0, 0, path)

if result:
    print(result)
else:
    print("No path found")
