
def dfs(city, path, visited, target, count, adj_matrix):
    if count[city] == 2 and city != target:
        return False
    
    path.append(city)
    visited[city] = True
    
    if city == target:
        count[city] += 1
    
    if count['N'] == 2 and count['J'] == 2:
        return True
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[i]:
            if dfs(i, path, visited.copy(), target, count.copy(), adj_matrix):
                return True
    
    path.pop()
    return False

adj_matrix = [
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
]

start_city = 'F'
target_cities = ['N', 'J']

visited = {chr(ord('A') + i): False for i in range(len(adj_matrix))}
count = {chr(ord('A') + i): 0 for i in range(len(adj_matrix)}

path = []
dfs(ord(start_city) - ord('A'), path, visited, target_cities[0], count, adj_matrix)

print([chr(city + ord('A')) for city in path])
