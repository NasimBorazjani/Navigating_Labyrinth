
import numpy as np

# Create the matrix map of the city
city_map = np.array([[18, 15, np.inf, np.inf, 1, np.inf, np.inf, 5, 8, 18, 18, 2, np.inf, 11, 8],
                      [np.inf, 17, np.inf, np.inf, 2, np.inf, 16, 9, 7, 13, 16, 17, np.inf, np.inf, np.inf],
                      [10, np.inf, 1, 14, 1, 10, 15, 4, np.inf, np.inf, 8, 11, 10, np.inf, np.inf],
                      [19, np.inf, np.inf, 9, 8, 18, 5, 2, 12, np.inf, 13, np.inf, np.inf, 15, 11],
                      [1, np.inf, 14, 6, 6, 6, np.inf, np.inf, np.inf, 13, 13, np.inf, np.inf, np.inf, np.inf],
                      [2, 3, 8, 5, 7, np.inf, np.inf, np.inf, 19, np.inf, 16, np.inf, np.inf, np.inf, np.inf],
                      [np.inf, np.inf, 17, 18, np.inf, 19, np.inf, np.inf, np.inf, 7, 8, 17, np.inf, np.inf, np.inf],
                      [4, np.inf, 4, 14, 17, 6, np.inf, 2, np.inf, np.inf, 15, 6, np.inf, 18, 10],
                      [7, np.inf, 3, 11, 10, np.inf, np.inf, 12, np.inf, np.inf, 8, np.inf, 10, np.inf, np.inf],
                      [4, 16, 2, 11, np.inf, np.inf, 14, np.inf, 13, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
                      [14, 20, 7, 14, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 5, np.inf, 10, 16, np.inf],
                      [1, 14, np.inf, np.inf, np.inf, 4, 14, 19, np.inf, 18, np.inf, np.inf, 17, 15, 14],
                      [np.inf, np.inf, 15, np.inf, 4, 5, 19, 18, np.inf, 19, 11, 3, 12, np.inf, 10],
                      [1, np.inf, 1, np.inf, np.inf, 13, np.inf, 16, 4, np.inf, np.inf, 8, np.inf, 9, np.inf],
                      [np.inf, np.inf, 12, 11, 7, np.inf, 8, 14, 3, np.inf, 11, np.inf, 14, 13, np.inf]])

# Define the districts
districts = {1: [0, 1], 2: [2, 9], 3: [10, 14]}

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

        if current == end:
            path = []
            while prev[current] is not None:
                path.insert(0, current)
                current = prev[current]
            path.insert(0, start)
            return path

        for neighbor, weight in enumerate(graph[current]):
            if weight != np.inf and neighbor in unvisited:
                alt = dist[current] + weight
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = current

# Find the shortest path that satisfies the conditions
shortest_path = None
for workshop in range(len(city_map)):
    if districts[1][0] <= workshop <= districts[1][1]:
        path1 = dijkstra_shortest_path(city_map, 1*15 + 11, workshop)
        for workshop2 in range(len(city_map)):
            if districts[2][0] <= workshop2 <= districts[2][1]:
                path2 = dijkstra_shortest_path(city_map, workshop, workshop2)
                for workshop3 in range(len(city_map)):
                    if districts[3][0] <= workshop3 <= districts[3][1]:
                        path3 = dijkstra_shortest_path(city_map, workshop2, workshop3)
                        path = path1 + path2[1:] + path3[1:]
                        if shortest_path is None or len(path) < len(shortest_path):
                            shortest_path = path

print([(workshop // 15, workshop % 15) for workshop in shortest_path])
