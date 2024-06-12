
import numpy as np

# Define the matrix map of the city
city_map = np.array([[18, 19, 9, np.inf, np.inf, np.inf, 3, np.inf, 8, np.inf],
                      [13, 2, 3, 15, 3, np.inf, 8, 9, np.inf, np.inf],
                      [np.inf, 6, 18, 1, 20, 7, 16, 8, 1, 19],
                      [np.inf, np.inf, np.inf, 20, 14, np.inf, 19, 11, 9, 6],
                      [2, np.inf, np.inf, 6, 5, 6, 7, 1, np.inf, 8],
                      [17, 9, 5, 3, 3, np.inf, 16, 18, np.inf, 8],
                      [10, np.inf, 14, 16, np.inf, 8, np.inf, 9, 6, np.inf],
                      [np.inf, 17, 8, 11, 12, np.inf, 4, 8, np.inf, 13],
                      [np.inf, np.inf, 6, np.inf, np.inf, np.inf, np.inf, 13, np.inf, 7],
                      [9, np.inf, np.inf, np.inf, 3, 10, np.inf, 3, 10, 1]])

# Define the districts
districts = {1: range(0, 4), 2: range(4, 5), 3: range(5, 10)}

# Define the start and end workshops
start_workshop = (5, 1)
end_workshop = (3, 9)

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
            break

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
for district in districts.values():
    for workshop in district:
        path1 = dijkstra_shortest_path(city_map, start_workshop[0]*10 + start_workshop[1], workshop)
        for district2 in districts.values():
            if workshop in district2:
                continue
            for workshop2 in district2:
                path2 = dijkstra_shortest_path(city_map, workshop, workshop2)
                path3 = dijkstra_shortest_path(city_map, workshop2, end_workshop[0]*10 + end_workshop[1])
                if shortest_path is None or len(path1) + len(path2) + len(path3) < len(shortest_path):
                    shortest_path = path1 + path2[1:] + path3

# Convert the path to tuples
path_tuples = [(workshop // 10, workshop % 10) for workshop in shortest_path]

print(path_tuples)
