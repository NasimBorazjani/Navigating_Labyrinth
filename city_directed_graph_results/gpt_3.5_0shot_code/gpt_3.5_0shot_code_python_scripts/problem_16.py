
def dfs(city, path, visited, target, count, adj_matrix):
    if count[city] == 2 and city != target:
        return False
    
    path.append(city)
    visited.add(city)
    
    if city == target:
        count[city] += 1
    
    if count[target] == 2:
        return True
    
    for next_city, connected in enumerate(adj_matrix[city]):
        if connected == 1 and next_city not in visited:
            if dfs(next_city, path, visited, target, count, adj_matrix):
                return True
    
    path.pop()
    visited.remove(city)
    if city == target:
        count[city] -= 1
    
    return False

adj_matrix = [
    [0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0]
]

cities = ['C', 'V', 'A', 'G', 'Y', 'P', 'Z', 'S', 'J', 'I']
start_city = 'S'
target_cities = ['P', 'G']

for target in target_cities:
    path = []
    visited = set()
    count = {city: 0 for city in cities}
    
    if dfs(cities.index(start_city), path, visited, cities.index(target), count, adj_matrix):
        print(path)
