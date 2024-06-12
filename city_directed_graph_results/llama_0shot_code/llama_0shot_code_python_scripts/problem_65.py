
import sys

# Adjacency matrix
matrix = [
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
]

# Convert the adjacency matrix into a dictionary of lists
graph = {city: [] for city in 'F DEZGYNIXPQSC'}
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col == 1:
            graph['F DEZGYNIXPQSC'.split()[i]].append('F DEZGYNIXPQSC'.split()[j])

# DFS function
def dfs(current, dests, counts, path):
    if current in dests:
        index = dests.index(current)
        if counts[index] > 0:
            counts[index] -= 1
            path.append(current)
            for city in graph[current]:
                if city not in path:
                    new_path = dfs(city, dests, counts, path)
                    if new_path:
                        return new_path
            counts[index] += 1
            path.pop()
    else:
        for city in graph[current]:
            if city not in path:
                new_path = dfs(city, dests, counts, path+[current])
                if new_path:
                    return new_path
    return path if len(path) == len(dests)*2+1 else None

# Start the search from city 'Q'
dests = ['F', 'N']
counts = [2, 2]
shortest_path = dfs('Q', dests, counts, [])
print(shortest_path)
