
# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0]
]

# Dictionary of lists
graph = {city: [] for city in 'GJYQCDRFKHN'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[chr(i+65)].append(chr(j+65))

# DFS function
def dfs(city, path, visited):
    # If we have visited all cities twice, and no city is visited more than twice, we have found a solution
    if visited.count(2) == len(visited) - 2:
        return [city] + path
    # Otherwise, we continue the DFS
    for next_city in graph[city]:
        if visited[cities.index(next_city)] < 2:
            new_visited = visited[:]
            new_visited[cities.index(next_city)] += 1
            result = dfs(next_city, [city] + path, new_visited)
            if result:
                return result

# List of cities
cities = list(graph.keys())

# Start the DFS from 'Q'
path = dfs('Q', [], [0]*len(cities))

print(path)
