
from itertools import permutations

# Adjacency matrix
matrix = [
    "0001011100",
    "0000010000",
    "0100001010",
    "0100100000",
    "0001000100",
    "0101101100",
    "0000101001",
    "0000011010",
    "1000000000",
    "0010111000"
]

# Convert the adjacency matrix into a dictionary
graph = {city: [] for city in 'CVAGYPZSJI'}
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col == '1':
            graph[chr(i+67)].append(chr(j+67))

# Recursive function to generate all possible routes
def generate_routes(start, end, visit_twice, path):
    if len(path) == len(graph)*2:
        if path.count(end) == 2:
            return [path]
        else:
            return []
    routes = []
    for node in graph[start]:
        if node not in path:
            new_path = path + [node]
            routes.extend(generate_routes(node, end, visit_twice, new_path))
    return routes

# Generate all possible routes and calculate their distances
all_routes = generate_routes('S', 'P', 2, ['S'])
distances = [(sum(graph[city1][city2] for city1, city2 in zip(route, route[1:])) +
              sum(graph[city1][city2] for city1, city2 in zip(route[::-1], route[::-1][1:])), route)
             for route in all_routes if route[-1] == 'P' and route[-2] == 'G']

# Sort the routes by their distances and return the shortest
distances.sort()
shortest_route = distances[0][1]
print(shortest_route)
