
import itertools
import networkx as nx

# Adjacency matrix
matrix = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
          [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
          [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
          [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0]]

# Create a graph from the adjacency matrix
G = nx.DiGraph(matrix)

# Find the shortest path between each pair of cities
shortest_paths = dict(nx.all_pairs_dijkstra_path(G))

# List of cities
cities = list(G.nodes)

# Permutations of cities (excluding start city 'T' and cities N and W)
perm = list(itertools.permutations(cities[:cities.index('N')] + cities[cities.index('N')+1:cities.index('W')] + cities[cities.index('W')+1:]))

# Function to check if a path visits cities N and W exactly twice
def check_path(path):
    count_n = count_w = 0
    for city in path:
        if city == 'N':
            count_n += 1
        elif city == 'W':
            count_w += 1
    return count_n == 2 and count_w == 2

# Find the shortest path that visits cities N and W exactly twice
shortest_path = None
shortest_path_length = float('inf')
for path in perm:
    path = ['T'] + list(path) + ['N', 'W']
    length = sum(shortest_paths[path[i]][path[i+1]] for i in range(len(path)-1))
    if length < shortest_path_length and check_path(path[1:-2]):
        shortest_path = path
        shortest_path_length = length

print(shortest_path)
