
def dfs(city, visited, path, target, count, result):
    visited[city] = True
    path.append(city)
    
    if city == target and count[target] < 2:
        count[target] += 1
        if count['B'] == 2 and count['V'] == 2:
            result.append(path.copy())
    else:
        for i, connected in enumerate(adj_matrix[city]):
            if connected == 1 and not visited[i]:
                dfs(i, visited, path, target, count, result)
    
    visited[city] = False
    path.pop()

# Adjacency matrix representing the connections between cities
adj_matrix = [
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0]
]

start_city = 'S'
target_cities = ['B', 'V']
visited = {chr(ord('A') + i): False for i in range(len(adj_matrix))}
count = {city: 0 for city in target_cities}
result = []

dfs(start_city, visited, [], target_cities[0], count, result)

if result:
    print(result[0])
else:
    print("No valid path found")
