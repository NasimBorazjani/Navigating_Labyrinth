
def dfs(city, visited, path, target, count, result):
    visited[city] = True
    path.append(city)
    
    if city == target:
        count[target] += 1
    
    if count['K'] == 2 and count['S'] == 2:
        result.append(path.copy())
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[city]:
            dfs(chr(65 + i), visited, path, target, count, result)
    
    visited[city] = False
    path.pop()
    if city == target:
        count[target] -= 1

adj_matrix = [
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
]

visited = {chr(65 + i): False for i in range(len(adj_matrix))}
path = []
result = []
count = {'K': 0, 'S': 0}

dfs('Y', visited, path, 'K', count, result)

print(result[0])  # Print the quickest route
