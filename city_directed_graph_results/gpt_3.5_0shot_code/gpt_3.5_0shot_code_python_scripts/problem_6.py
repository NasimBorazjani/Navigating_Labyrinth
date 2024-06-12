
def dfs(city, visited, path, adj_matrix, target_cities, target_count, current_count):
    visited[city] = True
    path.append(city)
    
    if city in target_cities:
        current_count[city] += 1
    
    if current_count == target_count:
        return path
    
    for next_city, connected in enumerate(adj_matrix[city]):
        if connected == 1 and not visited[next_city]:
            new_path = dfs(next_city, visited.copy(), path.copy(), adj_matrix, target_cities, target_count, current_count)
            if new_path:
                return new_path
    
    return None

adj_matrix = [
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
]

city_names = ['F', 'I', 'O', 'J', 'K', 'D', 'N', 'R', 'M', 'B']
start_city = city_names.index('N')
target_cities = [city_names.index('D'), city_names.index('F')]
target_count = {city: 2 for city in target_cities}
current_count = {city: 0 for city in target_cities}

visited = [False] * len(adj_matrix)
path = []

result = dfs(start_city, visited, path, adj_matrix, target_cities, target_count, current_count)

if result:
    result = [city_names[city] for city in result]
    print(result)
else:
    print("No valid path found")
