
import sys

# Adjacency matrix
matrix = [
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
]

# Convert adjacency matrix into dictionary
graph = {city: [] for city in 'ABCDEFGHIJKL'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[chr(i + 65)].append(chr(j + 65))

# Depth-first search function
def dfs(city, visited, to_visit_twice, path):
    visited.add(city)
    path.append(city)

    if set(graph[city]) - visited.union(to_visit_twice) == set(graph.keys()) - {'R', 'S', 'F'} - visited - to_visit_twice:
        path.append('F')
        return path

    for next_city in graph[city]:
        if next_city not in visited:
            result = dfs(next_city, visited, to_visit_twice, path)
            if result:
                return result
        elif next_city in to_visit_twice:
            to_visit_twice.remove(next_city)
            result = dfs(next_city, visited, to_visit_twice, path)
            if result:
                return result

    path.pop()
    visited.remove(city)
    return None

# Find quickest route
visited = set()
to_visit_twice = {'R', 'S'}
path = []
result = dfs('F', visited, to_visit_twice, path)
print(result)
