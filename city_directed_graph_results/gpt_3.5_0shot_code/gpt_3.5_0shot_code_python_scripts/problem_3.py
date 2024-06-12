
def dfs(city, visited, path, target, count, result):
    if count[target] == 2:
        result.append(path.copy())
        return
    
    visited[city] = True
    path.append(city)
    
    for i in range(len(adj_matrix[city])):
        if adj_matrix[city][i] == 1 and not visited[i]:
            if i == target:
                count[i] += 1
            dfs(i, visited, path, target, count, result)
            if i == target:
                count[i] -= 1
    
    visited[city] = False
    path.pop()

adj_matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0]
]

start = 5  # City 'M'
target1 = 4  # City 'A'
target2 = 8  # City 'R'

visited = [False] * len(adj_matrix)
path = []
count = [0] * len(adj_matrix)
result = []

dfs(start, visited, path, target1, count, result)
dfs(start, visited, path, target2, count, result)

quickest_route = min(result, key=len)
print(quickest_route)
