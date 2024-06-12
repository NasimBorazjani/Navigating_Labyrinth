
def dfs(city, visited, path, adj_matrix, target_cities, target_count, current_count):
    visited[city] = True
    path.append(city)
    
    if city in target_cities:
        current_count[city] += 1
    
    if current_count == target_count:
        return path
    
    for next_city, connected in enumerate(adj_matrix[city]):
        if connected == 1 and not visited[next_city]:
            result = dfs(next_city, visited.copy(), path.copy(), adj_matrix, target_cities, target_count, current_count)
            if result:
                return result
    
    return None

adj_matrix = [
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0]
]

start_city = 3  # City 'Q'
target_cities = [6, 8]  # Cities 'K' and 'Y'
target_count = {6: 2, 8: 2}  # Visit 'K' and 'Y' twice each

visited = [False] * len(adj_matrix)
path = []
current_count = {city: 0 for city in target_cities}

result = dfs(start_city, visited, path, adj_matrix, target_cities, target_count, current_count)

if result:
    print(result)
else:
    print("No valid path found")
