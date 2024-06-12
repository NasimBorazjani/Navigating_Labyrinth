
def dfs(city, visited, path, target, count, result):
    visited[city] = True
    path.append(city)
    
    if city == target and count[target] < 2:
        count[target] += 1
        if count['G'] == 2 and count['J'] == 2:
            result.append(path.copy())
    else:
        for i in range(len(adj_matrix[city])):
            if adj_matrix[city][i] == 1 and not visited[i]:
                dfs(i, visited, path, target, count, result)
    
    visited[city] = False
    path.pop()

adj_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
]

cities = ['P', 'G', 'W', 'V', 'L', 'M', 'B', 'S', 'J', 'H', 'D', 'N', 'R']
start_city = 'P'
target_cities = ['G', 'J']

visited = {city: False for city in cities}
count = {city: 0 for city in target_cities}
result = []

dfs(cities.index(start_city), visited, [], cities.index('G'), count, result)

print([cities[i] for i in result[0]])
