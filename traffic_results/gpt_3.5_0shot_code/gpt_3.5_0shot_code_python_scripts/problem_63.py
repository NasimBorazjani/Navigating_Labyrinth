
import numpy as np

# Create the matrix map of the city
city_map = np.array([[16, 9, 19, 14, 16, 19, 6, np.inf, np.inf, np.inf, 16, 18, np.inf],
                     [19, np.inf, np.inf, 9, 9, np.inf, 17, 16, 3, np.inf, np.inf, 14, np.inf],
                     [np.inf, np.inf, 11, np.inf, 5, np.inf, 15, 15, 17, 10, np.inf, 13, 5],
                     [2, 12, 9, 18, 7, np.inf, np.inf, np.inf, 4, np.inf, 10, np.inf, 3],
                     [8, 9, 19, 1, np.inf, 4, 8, np.inf, 17, 6, np.inf, 18, np.inf],
                     [np.inf, 6, 7, 9, 1, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
                     [np.inf, 5, 4, 12, 13, 13, np.inf, np.inf, np.inf, 11, np.inf, 5, 9],
                     [np.inf, np.inf, 2, 20, 6, 11, 2, np.inf, np.inf, np.inf, 10, 18, np.inf],
                     [np.inf, np.inf, 1, 18, 1, 17, 2, 3, 10, 12, 11, np.inf, 19],
                     [np.inf, 16, 3, np.inf, np.inf, 16, 3, 10, 19, np.inf, np.inf, 9, np.inf],
                     [10, np.inf, np.inf, np.inf, np.inf, 1, 10, 13, np.inf, np.inf, 13, np.inf, np.inf],
                     [np.inf, np.inf, np.inf, np.inf, 13, np.inf, 1, 14, np.inf, 10, np.inf, np.inf, 8],
                     [np.inf, np.inf, np.inf, np.inf, np.inf, 9, 2, 18, 19, 14, 10, np.inf, np.inf]])

# Define the districts
districts = {1: range(0, 4), 2: range(4, 9), 3: range(9, 13)}

# Define the starting and destination workshops
start_workshop = (3, 0)
dest_workshop = (8, 9)

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

    return None

# Find the shortest path from start to destination visiting at least one workshop in each district
path = None
for district in districts.values():
    for workshop in district:
        path_start = dijkstra_shortest_path(city_map, start_workshop[0]*13 + start_workshop[1], workshop)
        path_end = dijkstra_shortest_path(city_map, workshop, dest_workshop[0]*13 + dest_workshop[1])
        if path_start is not None and path_end is not None:
            if path is None or len(path_start) + len(path_end) - 1 < len(path):
                path = path_start + path_end[1:]

# Convert the path indices to workshop coordinates
workshop_path = [(index // 13, index % 13) for index in path]

print(workshop_path)
