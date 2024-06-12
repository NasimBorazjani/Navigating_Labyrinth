
def dfs(city, visited, path, target, count, result):
    visited[city] = True
    path.append(city)
    
    if city == target and count[target] < 2:
        count[target] += 1
        if count['K'] == 2 and count['Q'] == 2:
            result.append(path.copy())
    else:
        for i, connected in enumerate(adj_matrix[city]):
            if connected == 1 and not visited[i]:
                dfs(i, visited, path, target, count, result)
    
    visited[city] = False
    path.pop()

# Adjacency matrix representing the connections between cities
adj_matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 1, 0]
]

start_city = 'D'
target_cities = ['K', 'Q']

visited = {chr(ord('A') + i): False for i in range(10)}
count = {city: 0 for city in target_cities}
result = []

dfs(start_city, visited, [], 'K', count, result)

if not result:
    print("No valid path found.")
else:
    print(result[0])
