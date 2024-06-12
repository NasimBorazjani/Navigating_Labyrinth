
import numpy as np

# Define the matrix map of the city
city_map = np.array([[13, 13, 16, 8, np.inf, 19, 1, 18, 13, 8, np.inf, 7, np.inf],
                     [np.inf, 13, np.inf, 15, np.inf, 12, 20, 1, 13, 19, 4, 17, np.inf],
                     [np.inf, 12, 9, 11, 13, 12, 2, 12, 19, 5, 19, 16, 8],
                     [np.inf, 12, 18, 19, np.inf, 7, np.inf, 12, 3, 2, np.inf, 16, 11],
                     [np.inf, 7, np.inf, np.inf, 8, 13, 15, 3, 1, np.inf, 15, 15, np.inf],
                     [11, 9, np.inf, 16, 2, 10, 1, 2, 16, 1, np.inf, 10, 12],
                     [np.inf, np.inf, 9, 9, 7, np.inf, 6, np.inf, np.inf, 10, 7, 2, np.inf],
                     [np.inf, 13, 10, 8, 1, 11, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
                     [11, 14, np.inf, np.inf, np.inf, np.inf, 4, 8, np.inf, np.inf, 18, np.inf, np.inf],
                     [13, 14, np.inf, 10, np.inf, np.inf, 16, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
                     [np.inf, np.inf, 16, np.inf, 10, np.inf, 17, np.inf, 12, np.inf, 10, np.inf, 5],
                     [9, np.inf, 10, np.inf, 19, 16, np.inf, 14, 16, 12, 15, 7, np.inf],
                     [1, np.inf, 8, 10, 14, np.inf, 6, 9, np.inf, np.inf, 8, 11, 11]])

# Define the districts
districts = {1: [0, 1], 2: [2, 3, 4, 5], 3: [6, 7, 8, 9, 10, 11, 12]}

# Define the destination workshop
destination = (6, 2)

# Function to find the shortest path using Dijkstra's algorithm
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
    for start in district:
        for end in district:
            if start != end:
                path = dijkstra_shortest_path(city_map, start, end)
                if destination in path:
                    shortest_path = path
                    break
        if shortest_path:
            break
    if shortest_path:
        break

print([(index // city_map.shape[1], index % city_map.shape[1]) for index in shortest_path])
