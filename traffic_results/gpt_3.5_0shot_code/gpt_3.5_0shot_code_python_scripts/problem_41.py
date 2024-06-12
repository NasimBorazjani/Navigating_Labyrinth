
import numpy as np

# Define the matrix map of the city
city_map = np.array([[19, 7, 11, np.inf, 3, 18, 8, np.inf, np.inf, np.inf, np.inf],
                      [12, 18, 6, 1, 13, 12, 14, 11, 13, 5, 19],
                      [11, 10, 10, 18, 15, np.inf, 12, np.inf, 4, 17, 10],
                      [4, 3, 3, 7, np.inf, 19, np.inf, np.inf, np.inf, 12, 9],
                      [np.inf, np.inf, 6, 19, np.inf, 4, 14, np.inf, 9, 4, 15],
                      [4, 7, 6, 5, 8, np.inf, 15, 3, np.inf, 16, 3],
                      [13, np.inf, np.inf, 1, 9, 1, 9, np.inf, np.inf, np.inf, np.inf],
                      [2, 13, 5, 9, 5, np.inf, 6, np.inf, 18, np.inf, 3],
                      [19, np.inf, 2, 9, 4, 13, np.inf, np.inf, np.inf, 16, 6],
                      [np.inf, np.inf, np.inf, 12, np.inf, 7, 9, 3, 9, 8, 1],
                      [np.inf, 10, np.inf, 12, 3, 6, np.inf, 4, 12, 4, np.inf]])

# Define the districts
districts = {1: range(0, 4), 2: range(4, 5), 3: range(5, 11)}

# Define the start and end workshops
start_workshop = (5, 10)
end_workshop = (3, 0)

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

        for neighbor in range(len(graph)):
            if graph[current][neighbor] != np.inf:
                alt = dist[current] + graph[current][neighbor]
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = current

    return None

# Find the shortest path that satisfies the conditions
shortest_path = None
for district in districts.values():
    for workshop in district:
        path1 = dijkstra_shortest_path(city_map, start_workshop[0]*11 + start_workshop[1], workshop)
        if path1 is None:
            continue
        for workshop2 in district:
            if workshop2 == workshop:
                continue
            path2 = dijkstra_shortest_path(city_map, workshop, workshop2)
            if path2 is None:
                continue
            path3 = dijkstra_shortest_path(city_map, workshop2, end_workshop[0]*11 + end_workshop[1])
            if path3 is None:
                continue
            path = path1 + path2[1:] + path3[1:]
            if shortest_path is None or len(path) < len(shortest_path):
                shortest_path = path

# Convert the indices to coordinates
shortest_path_coords = [(index // 11, index % 11) for index in shortest_path]

print(shortest_path_coords)
