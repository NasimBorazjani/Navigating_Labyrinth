
import numpy as np

# Define the city map as a numpy array
city_map = np.array([[np.inf, np.inf, 12, np.inf, 18, 3, 2, 15, 6, 11, 13, np.inf, 7, 17, np.inf],
                      [13, np.inf, 20, 13, 5, 2, np.inf, np.inf, 10, 12, 19, 19, 16, np.inf, 17],
                      [12, 12, 7, np.inf, np.inf, np.inf, 9, np.inf, np.inf, 10, 10, 18, 4, np.inf, np.inf],
                      [np.inf, 14, 3, 13, 9, 2, 19, 19, np.inf, np.inf, np.inf, 4, np.inf, 2, 15],
                      [np.inf, 14, 2, np.inf, 3, np.inf, 10, 11, np.inf, 4, np.inf, 12, 4, np.inf, np.inf],
                      [np.inf, 9, 7, 16, np.inf, np.inf, 19, 17, 17, 14, 14, 12, 14, 19, 12],
                      [2, np.inf, np.inf, 7, 15, np.inf, np.inf, 13, np.inf, 8, 1, 1, np.inf, 14, 19],
                      [16, np.inf, 14, np.inf, np.inf, 6, np.inf, np.inf, 16, np.inf, np.inf, 9, 10, 18, 4],
                      [3, np.inf, np.inf, 3, np.inf, np.inf, np.inf, np.inf, 9, 8, np.inf, 9, 14, np.inf, 14],
                      [np.inf, np.inf, np.inf, 4, 19, np.inf, 4, 15, np.inf, np.inf, np.inf, 17, np.inf, np.inf, np.inf],
                      [16, 17, np.inf, np.inf, 13, np.inf, 18, 5, np.inf, 14, np.inf, np.inf, np.inf, np.inf, np.inf],
                      [2, np.inf, 17, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 12, 3, 8, np.inf, 2, 9],
                      [np.inf, np.inf, 14, 7, 11, np.inf, np.inf, 10, 9, 3, 7, 16, np.inf, 7, 1],
                      [np.inf, 12, 14, 1, np.inf, np.inf, 3, 12, np.inf, 7, np.inf, np.inf, 8, np.inf, np.inf],
                      [np.inf, 2, np.inf, 15, 2, np.inf, 14, 16, 13, 19, 16, 1, 11, np.inf, np.inf]])

# Define the districts
districts = {1: range(0, 6), 2: range(6, 8), 3: range(8, 15)}

# Define the destination workshop
destination = (8, 14)

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

# Find the shortest path that satisfies the conditions
shortest_path = None
for workshop in districts[1]:
    for workshop2 in districts[2]:
        for workshop3 in districts[3]:
            path1 = dijkstra_shortest_path(city_map, 5*15 + 2, workshop)
            path2 = dijkstra_shortest_path(city_map, workshop, workshop2)
            path3 = dijkstra_shortest_path(city_map, workshop2, workshop3)
            path4 = dijkstra_shortest_path(city_map, workshop3, 8*15 + 14)

            if path1 and path2 and path3 and path4:
                total_path = path1[:-1] + path2[:-1] + path3[:-1] + path4
                if shortest_path is None or len(total_path) < len(shortest_path):
                    shortest_path = total_path

# Convert the indices to (row, column) tuples
path_tuples = [(index // 15, index % 15) for index in shortest_path]

print(path_tuples)
