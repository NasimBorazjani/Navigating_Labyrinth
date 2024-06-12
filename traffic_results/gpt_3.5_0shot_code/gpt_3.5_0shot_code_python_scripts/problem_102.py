
import numpy as np

# Define the city map as a numpy array
city_map = np.array([[np.inf, 13, np.inf, np.inf, np.inf, np.inf, 3, 4, np.inf, np.inf, 9, np.inf, 18, 7, 2],
                      [1, 10, 17, np.inf, np.inf, np.inf, 11, 13, np.inf, 10, np.inf, 9, 13, np.inf, np.inf],
                      [np.inf, np.inf, 7, 18, np.inf, np.inf, np.inf, np.inf, 7, np.inf, np.inf, np.inf, 1, np.inf, 16],
                      [10, np.inf, np.inf, np.inf, 13, np.inf, 2, 9, np.inf, np.inf, 8, np.inf, np.inf, 5, np.inf],
                      [np.inf, 7, 12, np.inf, 1, 18, 14, np.inf, 7, np.inf, np.inf, 16, np.inf, np.inf, 19],
                      [5, 1, 13, 17, 11, 14, 16, np.inf, 14, np.inf, 18, 5, np.inf, 18, np.inf],
                      [np.inf, 15, 19, 4, np.inf, 13, np.inf, 5, np.inf, np.inf, 18, np.inf, 17, np.inf, np.inf],
                      [3, 7, np.inf, np.inf, np.inf, 12, np.inf, np.inf, 17, 4, np.inf, 13, 19, 3, 10],
                      [11, np.inf, np.inf, np.inf, np.inf, 2, 2, 19, 13, 4, 7, 17, 16, np.inf, 17],
                      [12, 5, 4, np.inf, np.inf, np.inf, np.inf, 12, 8, 11, np.inf, 17, 14, 19, 2],
                      [4, 10, np.inf, np.inf, 6, 11, 16, 17, np.inf, np.inf, 18, np.inf, 17, np.inf, np.inf],
                      [np.inf, np.inf, np.inf, np.inf, 11, 9, 18, 17, 12, np.inf, np.inf, np.inf, np.inf, 1],
                      [18, 13, 7, np.inf, np.inf, 5, 4, 13, np.inf, np.inf, 19, 12, 1, 18, np.inf],
                      [15, np.inf, 17, np.inf, np.inf, np.inf, 17, np.inf, np.inf, np.inf, 10, np.inf, 15, 16, np.inf],
                      [np.inf, np.inf, 11, 15, np.inf, np.inf, 12, 16, 12, 13, 18, np.inf, 17, 8, 15]])

# Define the districts
districts = {1: range(0, 6), 2: range(6, 7), 3: range(7, 15)}

# Define the destination workshop
destination = (7, 13)

# Define function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, end):
    nodes = set(range(len(graph)))
    dist = {node: np.inf for node in nodes}
    dist[start] = 0
    prev = {node: None for node in nodes}
    unvisited = nodes.copy()
    
    while unvisited:
        current = min(unvisited, key=lambda node: dist[node])
        unvisited.remove(current)
        
        for neighbor, weight in enumerate(graph[current]):
            if weight != np.inf:
                new_dist = dist[current] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    prev[neighbor] = current
    
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = prev[current]
    
    return path

# Find the shortest path from Ben's current workshop to the destination workshop
shortest_path = []
for district in districts.values():
    for workshop in district:
        path = dijkstra_shortest_path(city_map, 5, workshop) + dijkstra_shortest_path(city_map, workshop, destination)[1:]
        if len(path) < len(shortest_path) or not shortest_path:
            shortest_path = path

print(shortest_path)
