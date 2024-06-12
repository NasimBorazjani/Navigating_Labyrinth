
def dfs(adj_matrix, current_city, visited, path, target_cities, target_count):
    visited[current_city] = True
    path.append(current_city)
    
    if current_city in target_cities:
        target_count[current_city] += 1
    
    if target_count[target_cities[0]] == 2 and target_count[target_cities[1]] == 2:
        return path
    
    for next_city, connected in enumerate(adj_matrix[current_city]):
        if connected == 1 and not visited[next_city]:
            new_path = dfs(adj_matrix, next_city, visited.copy(), path.copy(), target_cities, target_count)
            if new_path:
                return new_path
    
    return None

adj_matrix = [
    [0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0]
]

city_names = ['L', 'S', 'P', 'R', 'N', 'F', 'O', 'K', 'B', 'H', 'T', 'W', 'U', 'E']
start_city = city_names.index('B')
target_cities = [city_names.index('F'), city_names.index('W')]
target_count = {target_cities[0]: 0, target_cities[1]: 0}

visited = [False] * len(adj_matrix)
path = []

result = dfs(adj_matrix, start_city, visited, path, target_cities, target_count)

if result:
    print([city_names[city] for city in result])
else:
    print("No valid path found")
