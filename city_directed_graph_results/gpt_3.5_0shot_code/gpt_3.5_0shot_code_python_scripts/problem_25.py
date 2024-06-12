
def dfs(city, visited, path, target_cities, adjacency_matrix):
    visited[city] = True
    path.append(city)
    
    if len(path) == 5:  # We have visited all cities twice (including start city 'M')
        return path
    
    for next_city in range(len(adjacency_matrix[city])):
        if adjacency_matrix[city][next_city] == 1 and not visited[next_city]:
            result = dfs(next_city, visited.copy(), path.copy(), target_cities, adjacency_matrix)
            if result:
                return result
    
    return None

adjacency_matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]
]

start_city = 1  # City 'M'
target_cities = [8, 2]  # Cities 'X' and 'Y'

visited = [False] * len(adjacency_matrix)
path = []

result = dfs(start_city, visited, path, target_cities, adjacency_matrix)

city_names = ['O', 'M', 'Y', 'J', 'Z', 'V', 'K', 'F', 'X', 'L', 'R']
city_path = [city_names[city] for city in result]

print(city_path)
