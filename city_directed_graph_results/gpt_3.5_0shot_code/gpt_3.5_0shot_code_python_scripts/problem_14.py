
def dfs(city, path, visited, target, count, adj_matrix):
    if count[city] == 2 and city != target:
        return False
    
    path.append(city)
    visited[city] = True
    
    if city == target:
        count[city] += 1
    
    if count[target] == 2:
        return True
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[i]:
            if dfs(i, path, visited.copy(), target, count.copy(), adj_matrix):
                return True
    
    path.pop()
    return False

adj_matrix = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 0]
]

start = 'N'
target1 = 'H'
target2 = 'M'

visited = {chr(i+65): False for i in range(10)}
count = {chr(i+65): 0 for i in range(10)}
path = []

dfs(start, path, visited, target1, count, adj_matrix)
dfs(start, path, visited, target2, count, adj_matrix)

print(path)
