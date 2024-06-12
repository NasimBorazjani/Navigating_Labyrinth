
from collections import defaultdict

def dfs(city, visited, path):
    visited[city] = visited.get(city, 0) + 1
    path.append(city)

    if len(path) > 2 and path.count('T') == 2 and path.count('C') == 2:
        paths.append(path.copy())
    else:
        for next_city in graph[city]:
            if visited.get(next_city, 0) < 2:
                dfs(next_city, visited, path)

    visited[city] -= 1
    path.pop()

graph = defaultdict(list)
cities = ['M', 'Y', 'Q', 'T', 'E', 'A', 'J', 'S', 'V', 'F', 'W', 'N', 'Z', 'C', 'I']
matrix = [
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[cities[i]].append(cities[j])

paths = []
dfs('S', {}, [])
paths = [path for path in paths if all(path.count(city) == 1 for city in set(path) - {'T', 'C'})]
shortest_path = min(paths, key=len)

print(shortest_path)
