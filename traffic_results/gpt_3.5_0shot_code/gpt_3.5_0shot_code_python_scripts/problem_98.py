
import numpy as np

# Define the city map as a numpy array
city_map = np.array([
    [np.nan, 19, 4, np.nan, 17, 11, np.nan, np.nan, 18, 7, np.nan, 8, 20, np.nan, 1],
    [np.nan, 16, np.nan, 1, 9, 1, np.nan, 8, 16, np.nan, 15, 7, 1, np.nan, np.nan],
    [7, np.nan, 9, 9, 9, np.nan, 18, np.nan, 15, 13, 10, np.nan, 19, 16, 9],
    [np.nan, np.nan, np.nan, 6, np.nan, np.nan, 7, 10, 18, 17, np.nan, 8, 9, 6, 5],
    [4, 17, np.nan, np.nan, 19, 5, 20, 1, 15, 18, np.nan, np.nan, 5, 8, 2],
    [np.nan, np.nan, np.nan, 3, 10, 19, 17, 20, np.nan, np.nan, np.nan, 3, np.nan, 5, np.nan],
    [np.nan, np.nan, np.nan, 3, 8, 2, np.nan, np.nan, 7, 19, np.nan, np.nan, 1, 19, 9],
    [np.nan, 19, 16, 6, 5, 19, np.nan, np.nan, np.nan, 12, np.nan, 3, 8, 10, np.nan],
    [13, 2, np.nan, 18, np.nan, np.nan, 5, np.nan, np.nan, np.nan, 13, 1, np.nan, np.nan, 6],
    [19, 8, 8, 10, np.nan, np.nan, np.nan, 12, 14, 5, 14, 2, 6, np.nan, np.nan],
    [np.nan, np.nan, np.nan, 12, 18, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 16, np.nan, 19, np.nan],
    [11, np.nan, 12, np.nan, np.nan, 5, np.nan, 15, 8, np.nan, 9, np.nan, np.nan, np.nan, np.nan],
    [9, np.nan, 4, np.nan, np.nan, np.nan, np.nan, 2, 18, np.nan, 11, np.nan, 11, np.nan, 19],
    [13, np.nan, 17, 1, np.nan, 14, np.nan, np.nan, np.nan, 16, np.nan, 2, np.nan, np.nan, np.nan],
    [3, 16, np.nan, np.nan, 3, 11, np.nan, 15, np.nan, np.nan, np.nan, np.nan, np.nan, 16, np.nan]
])

# Define the districts
districts = {
    1: (0, 3),
    2: (4, 8),
    3: (9, 14)
}

# Define the start and end workshops
start_workshop = (9, 3)
end_workshop = (4, 14)

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

        for neighbor in nodes - set(path for path, time in enumerate(graph[current]) if not np.isnan(time)):
            alt = dist[current] + graph[current, neighbor]
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = current

    return None

# Find the shortest path that satisfies the conditions
path = None
for district in districts.values():
    for workshop in range(district[0], district[1] + 1):
        path_to_end = dijkstra_shortest_path(city_map, start_workshop[0]*15 + start_workshop[1], workshop)
        if path_to_end:
            path_from_start = dijkstra_shortest_path(city_map, workshop, end_workshop[0]*15 + end_workshop[1])
            if path_from_start:
                path = path_to_end + path_from_start[1:]
                break
    if path:
        break

# Convert the path to workshop indices
workshop_path = [(index // 15, index % 15) for index in path]

print(workshop_path)
