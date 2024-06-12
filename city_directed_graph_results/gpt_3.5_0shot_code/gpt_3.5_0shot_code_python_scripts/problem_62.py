
def dfs(city, visited, count_U, count_Y, path):
    visited[city] = True
    path.append(city)
    
    if city == 'U':
        count_U += 1
    elif city == 'Y':
        count_Y += 1
    
    if count_U == 2 and count_Y == 2:
        return path
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[city]:
            new_path = dfs(cities[i], visited.copy(), count_U, count_Y, path.copy())
            if new_path:
                return new_path
    
    return None

cities = ['Z', 'C', 'M', 'X', 'N', 'A', 'B', 'L', 'U', 'K', 'G', 'Y', 'O']
adj_matrix = [
    [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0]
]

start_city = 'K'
visited = {city: False for city in cities}
count_U = 0
count_Y = 0
path = []

result = dfs(start_city, visited, count_U, count_Y, path)

if result:
    print(result)
else:
    print("No valid path found")
