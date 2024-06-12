
def dfs(city, visited, path, target, count, result):
    visited[city] = True
    path.append(city)
    
    if city == target:
        count[target] += 1
    
    if count['G'] == 2 and count['Q'] == 2:
        result.append(path.copy())
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[city]:
            dfs(chr(65+i), visited, path, target, count, result)
    
    visited[city] = False
    path.pop()

adj_matrix = [
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0]
]

visited = {chr(i): False for i in range(65, 76)}
path = []
result = []
count = {'G': 0, 'Q': 0}

dfs('D', visited, path, 'G', count, result)

print(result[0])  # Print the quickest route
