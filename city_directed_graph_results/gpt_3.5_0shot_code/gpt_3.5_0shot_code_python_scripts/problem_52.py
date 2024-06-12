
def dfs(city, visited, path, target, count, result):
    visited[city] = True
    path.append(city)
    
    if city == target and count[target] < 2:
        count[target] += 1
        if count['D'] == 2 and count['J'] == 2:
            result.append(path.copy())
    else:
        for i, connected in enumerate(adj_matrix[city]):
            if connected == 1 and not visited[i]:
                dfs(i, visited, path, target, count, result)
    
    visited[city] = False
    path.pop()

# Adjacency matrix representing the connections between cities
adj_matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0]
]

# Initialize variables
visited = [False] * len(adj_matrix)
path = []
result = []
count = {'D': 0, 'J': 0}

# Start DFS from city 'C'
dfs(0, visited, path, 'D', count, result)

# Print the quickest route
print(result[0])
