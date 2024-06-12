
def dfs(city, visited, path, target, num_visits):
    visited[city] = True
    path.append(city)
    
    if city == target and num_visits[target] < 2:
        num_visits[target] += 1
    elif city == target:
        return
    
    for i, connected in enumerate(adj_matrix[city]):
        if connected == 1 and not visited[i]:
            dfs(i, visited.copy(), path.copy(), target, num_visits)

    if len(path) == len(adj_matrix) and num_visits[target] == 2:
        paths.append(path)

adj_matrix = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0]
]

start_city = 'T'
target_cities = ['N', 'W']
paths = []

for target in target_cities:
    visited = [False] * len(adj_matrix)
    num_visits = {city: 0 for city in target_cities}
    dfs(start_city, visited, [], target, num_visits)

quickest_path = min(paths, key=len)
print(quickest_path)
