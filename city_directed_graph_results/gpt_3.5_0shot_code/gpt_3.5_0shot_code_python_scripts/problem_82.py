
def dfs(city, visited, path, target, count, result):
    visited[city] = True
    path.append(city)
    
    if city == target:
        count[target] += 1
    
    if count['F'] == 2 and count['L'] == 2:
        result.append(path.copy())
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[chr(65+i)]:
            dfs(chr(65+i), visited, path, target, count, result)
    
    visited[city] = False
    path.pop()
    if city == target:
        count[target] -= 1

adj_matrix = [
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
]

visited = {chr(i): False for i in range(65, 65+len(adj_matrix))}
path = []
result = []
count = {'F': 0, 'L': 0}

dfs('J', visited, path, 'F', count, result)

quickest_route = min(result, key=len)
print(quickest_route)
