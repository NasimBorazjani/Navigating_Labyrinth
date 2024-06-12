
import numpy as np

# Define the matrix map of the city
city_map = np.array([[np.inf, 5, 9, 6, 13, 13, 8, 6, 13, np.inf, 13, np.inf, np.inf, np.inf],
                      [3, 10, 16, np.inf, np.inf, 3, 13, 1, 11, 9, 7, 6, np.inf, 18],
                      [9, 11, 3, np.inf, np.inf, 6, 13, np.inf, 14, np.inf, 12, 1, 2, 4],
                      [np.inf, 17, 13, np.inf, 14, 4, 6, 8, np.inf, np.inf, 1, np.inf, 6, 2],
                      [7, np.inf, 11, np.inf, 14, np.inf, 11, 7, np.inf, 5, np.inf, 1, 12, np.inf],
                      [np.inf, 20, 20, 19, np.inf, 18, 2, 19, 1, 6, 12, np.inf, np.inf, 16],
                      [8, 5, 7, 11, np.inf, 1, np.inf, np.inf, np.inf, 11, 4, np.inf, np.inf, 3],
                      [np.inf, 11, np.inf, 11, 11, np.inf, np.inf, 18, np.inf, np.inf, np.inf, 7, 6, np.inf],
                      [2, 2, 14, 5, 5, np.inf, np.inf, 11, 19, 16, np.inf, 14, 7, 19],
                      [np.inf, 5, np.inf, np.inf, 7, np.inf, 10, np.inf, np.inf, np.inf, 3, 15, np.inf, np.inf],
                      [19, np.inf, np.inf, np.inf, np.inf, 8, 3, 19, np.inf, 18, np.inf, np.inf, np.inf, 9],
                      [17, np.inf, 19, np.inf, np.inf, np.inf, 5, 3, np.inf, np.inf, 7, 4, np.inf, np.inf],
                      [np.inf, np.inf, np.inf, np.inf, np.inf, 12, 11, np.inf, np.inf, np.inf, np.inf, np.inf, 6, 6],
                      [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 4, np.inf, np.inf, np.inf, 7, np.inf, 6, 3]])

# Define the districts
districts = {1: [0, 1], 2: [2, 3, 4, 5], 3: [6, 7, 8, 9, 10, 11, 12, 13]}

# Define the destination workshop
destination = (3, 13)

# Define a function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, end):
    nodes = set(graph.keys())
    dist = {node: np.inf for node in nodes}
    dist[start] = 0
    prev = {node: None for node in nodes}
    unvisited = nodes.copy()

    while unvisited:
        current = min(unvisited, key=lambda node: dist[node])
        unvisited.remove(current)

        if current == end:
            path = []
            while prev[current]:
                path.insert(0, current)
                current = prev[current]
            path.insert(0, start)
            return path

        for neighbor, cost in graph[current].items():
            alt = dist[current] + cost
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = current

    return None

# Create a graph representation of the city map
graph = {}
for i in range(city_map.shape[0]):
    for j in range(city_map.shape[1]):
        if city_map[i, j] != np.inf:
            neighbors = {}
            if i > 0 and city_map[i-1, j] != np.inf:
                neighbors[(i-1, j)] = city_map[i-1, j]
            if i < city_map.shape[0]-1 and city_map[i+1, j] != np.inf:
                neighbors[(i+1, j)] = city_map[i+1, j]
            if j > 0 and city_map[i, j-1] != np.inf:
                neighbors[(i, j-1)] = city_map[i, j-1]
            if j < city_map.shape[1]-1 and city_map[i, j+1] != np.inf:
                neighbors[(i, j+1)] = city_map[i, j+1]
            graph[(i, j)] = neighbors

# Find the shortest path from Ben's current workshop to the destination workshop
path = None
for district in districts.values():
    for workshop in district:
        if path is None:
            path = dijkstra_shortest_path(graph, (6, 1), (district, workshop))
        else:
            new_path = dijkstra_shortest_path(graph, (6, 1), (district, workshop))
            if new_path and len(new_path) < len(path):
                path = new_path

print(path)
