
import numpy as np

# Create the matrix map of the city
city_map = np.array([[np.inf, 14, 15, 10, np.inf, 14, np.inf, np.inf, 18, 6, np.inf, np.inf, 4],
                     [6, np.inf, np.inf, np.inf, 1, np.inf, 15, np.inf, np.inf, 2, np.inf, 17, np.inf],
                     [np.inf, 4, np.inf, 17, 3, 14, 4, 2, np.inf, 3, np.inf, 11, np.inf],
                     [6, 6, np.inf, 19, np.inf, 13, np.inf, 11, 13, 6, 3, np.inf, np.inf],
                     [3, 10, 11, np.inf, np.inf, 4, 4, 1, 19, np.inf, np.inf, np.inf, 17],
                     [8, np.inf, np.inf, 8, 11, 18, 17, 19, 18, np.inf, 1, 1, np.inf],
                     [14, 14, 1, 19, 6, np.inf, 19, 19, 18, 9, np.inf, 12, 18],
                     [17, 6, 8, np.inf, 1, 14, 19, 13, np.inf, np.inf, 9, np.inf, 3],
                     [16, 4, np.inf, np.inf, np.inf, 9, 5, np.inf, np.inf, np.inf, 18, np.inf, np.inf],
                     [np.inf, np.inf, 10, np.inf, 18, np.inf, 1, np.inf, np.inf, 12, 9, 8, 3],
                     [np.inf, 13, 17, np.inf, np.inf, np.inf, 5, 8, 1, np.inf, 1, 10, np.inf],
                     [10, 11, np.inf, 12, np.inf, 6, 11, np.inf, 9, 9, 15, np.inf, 10],
                     [5, 15, 1, np.inf, 8, 5, np.inf, 6, np.inf, 9, 18, np.inf, np.inf]])

# Define the districts
districts = {1: range(0, 4), 2: range(4, 8), 3: range(8, 13)}

# Define the destination workshop
destination = (8, 0)

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
    for workshop in district:
        path = dijkstra_shortest_path(city_map, 3*8 + 8, workshop)
        if path and path[-1] == workshop:
            shortest_path.extend(path)
            break

shortest_path.extend(dijkstra_shortest_path(city_map, shortest_path[-1], 8*8))

# Print the shortest path
print([(index // 13, index % 13) for index in shortest_path])
