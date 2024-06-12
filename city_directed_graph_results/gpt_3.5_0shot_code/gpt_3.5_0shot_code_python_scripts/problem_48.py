
def dfs(city, path, visited, adj_matrix, target, count):
    if count == target:
        return path
    
    visited[city] = True
    for i, connected in enumerate(adj_matrix[city]):
        if connected == 1 and not visited[i]:
            new_path = dfs(i, path + [i], visited.copy(), adj_matrix, target, count + 1)
            if new_path:
                return new_path
    
    return None

adj_matrix = [
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
]

start_city = 6  # City 'I'
target_cities = ['A', 'X']
target_count = 2

visited = [False] * len(adj_matrix)
path = dfs(start_city, [start_city], visited, adj_matrix, target_count, 0)

city_names = ['A', 'Q', 'S', 'O', 'N', 'V', 'I', 'X', 'D', 'B', 'E', 'Y']
city_path = [city_names[city] for city in path]

print(city_path)
