
from collections import defaultdict

def dfs(city, graph, visited, path, destinations):
    path.append(city)
    if city in destinations:
        visited[city] += 1
    if visited['D'] == 2 and visited['J'] == 2:
        return path
    for next_city in graph[city]:
        if visited[next_city] < 2:
            result = dfs(next_city, graph, visited, path, destinations)
            if result:
                return result
    path.pop()
    if city in destinations:
        visited[city] -= 1

def solve():
    cities = ['C', 'L', 'D', 'O', 'A', 'Z', 'M', 'H', 'K', 'R', 'Q', 'N', 'J']
    matrix = [
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
    graph = defaultdict(list)
    for i, city in enumerate(cities):
        for j, connected in enumerate(matrix[i]):
            if connected:
                graph[city].append(cities[j])
    visited = defaultdict(int)
    destinations = ['D', 'J']
    path = dfs('C', graph, visited, [], destinations)
    return path

print(solve())
