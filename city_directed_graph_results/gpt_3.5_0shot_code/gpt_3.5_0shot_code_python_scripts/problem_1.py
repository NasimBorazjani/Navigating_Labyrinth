
def dfs(city, visited, count_A, count_H, path):
    visited[city] = True
    path.append(city)
    
    if city == 'A':
        count_A += 1
    elif city == 'H':
        count_H += 1
    
    if count_A == 2 and count_H == 2:
        return path
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[city_list[i]]:
            new_path = dfs(city_list[i], visited.copy(), count_A, count_H, path.copy())
            if new_path:
                return new_path
    
    return None

city_list = ['G', 'D', 'X', 'N', 'Y', 'W', 'A', 'P', 'V', 'H']
adj_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 1, 0, 0]
]

start_city = 'W'
visited = {city: False for city in city_list}
count_A = 0
count_H = 0
path = []

result = dfs(start_city, visited, count_A, count_H, path)

if result:
    print(result)
else:
    print("No path found")
