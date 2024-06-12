
def dfs(city, visited, path, adj_matrix, target_cities, current_count, min_path, min_time):
    if current_count == 4 and city in target_cities:
        if min_time[0] == -1 or path[-1] < min_time[0]:
            min_time[0] = path[-1]
            min_path[:] = path
        return
    
    visited[city] = True
    for i, connected in enumerate(adj_matrix[city]):
        if connected == 1 and not visited[i]:
            path.append(path[-1] + 1)
            dfs(i, visited, path, adj_matrix, target_cities, current_count + 1, min_path, min_time)
            path.pop()
    
    visited[city] = False

adj_matrix = [
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0]
]

start_city = 1  # City 'E'
target_cities = {6, 10}  # Cities 'N' and 'O'

visited = [False] * len(adj_matrix)
path = [0]  # Start with time 0
min_path = []
min_time = [-1]

dfs(start_city, visited, path, adj_matrix, target_cities, 0, min_path, min_time)

city_names = ['I', 'E', 'A', 'G', 'V', 'K', 'B', 'N', 'F', 'W', 'J', 'O']
result = [city_names[city] for city in min_path]

print(result)
