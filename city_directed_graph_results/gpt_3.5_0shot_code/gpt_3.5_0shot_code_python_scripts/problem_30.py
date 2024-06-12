
def dfs(city, visited, path, target, count, result):
    if count[target] == 2:
        return
    if city == target:
        count[target] += 1
        result.append(city)
        return
    visited[city] = True
    path.append(city)
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[i]:
            dfs(i, visited, path, target, count, result)
    path.pop()
    visited[city] = False

adj_matrix = [
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0]
]

cities = ['S', 'V', 'U', 'W', 'G', 'E', 'H', 'P', 'T', 'Q', 'Z']
start_city = 'G'
target_cities = ['H', 'P']

visited = [False] * len(cities)
count = {city: 0 for city in target_cities}
result = []

dfs(cities.index(start_city), visited, [], cities.index(target_cities[0]), count, result)
dfs(cities.index(start_city), visited, [], cities.index(target_cities[1]), count, result)

print([cities[i] for i in result])
