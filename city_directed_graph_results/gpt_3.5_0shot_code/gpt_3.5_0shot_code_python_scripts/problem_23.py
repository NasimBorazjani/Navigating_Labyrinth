
def dfs(city, visited, path, graph, target_cities, target_count, current_count):
    visited[city] = True
    path.append(city)
    
    if city in target_cities:
        current_count[city] += 1
    
    if current_count == target_count:
        return path
    
    for next_city, connected in enumerate(graph[city]):
        if connected == 1 and not visited[next_city]:
            new_path = dfs(next_city, visited.copy(), path.copy(), graph, target_cities, target_count, current_count)
            if new_path:
                return new_path
    
    return None

adjacency_matrix = [
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]
]

city_names = ['N', 'W', 'X', 'P', 'J', 'E', 'L', 'M', 'I', 'K', 'Q']
start_city = 'K'
target_cities = ['N', 'P']
target_count = {city: 2 for city in target_cities}
current_count = {city: 0 for city in target_cities}

start_city_index = city_names.index(start_city)
visited = [False] * len(city_names)
path = []

result = dfs(start_city_index, visited, path, adjacency_matrix, target_cities, target_count, current_count)

if result:
    result = [city_names[city] for city in result]
    print(result)
else:
    print("No valid path found")
