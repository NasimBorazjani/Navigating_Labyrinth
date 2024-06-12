
def dfs(city, visited, path, adj_matrix, target_cities, target_count):
    visited[city] = True
    path.append(city)
    
    if city in target_cities:
        target_count[city] += 1
    
    if all(count == 2 for count in target_count.values()):
        return path
    
    for next_city, connected in enumerate(adj_matrix[city]):
        if connected == 1 and not visited[next_city]:
            result = dfs(next_city, visited.copy(), path.copy(), adj_matrix, target_cities, target_count)
            if result:
                return result
    
    return None

adj_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0]
]

city_names = ['F', 'I', 'C', 'G', 'N', 'L', 'X', 'Q', 'U', 'R', 'O', 'B']
city_index = {city: index for index, city in enumerate(city_names)}

start_city = 'G'
target_cities = {'O', 'R'}
target_count = {city_index[city]: 0 for city in target_cities}

start_city_index = city_index[start_city]
visited = [False] * len(city_names)
path = []

result = dfs(start_city_index, visited, path, adj_matrix, target_cities, target_count)

if result:
    print([city_names[city] for city in result])
else:
    print("No valid path found")
