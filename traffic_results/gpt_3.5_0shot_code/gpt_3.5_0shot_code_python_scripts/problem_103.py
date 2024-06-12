
import numpy as np

# Define the matrix map of the city
city_map = np.array([[6, 6, 2, np.inf, 13, np.inf, np.inf, np.inf, np.inf, 11, np.inf, np.inf, np.inf, 3, np.inf],
                      [6, 11, np.inf, 14, np.inf, np.inf, np.inf, 1, 5, 6, 1, 19, 2, 7, 14],
                      [16, 4, 12, 13, 17, 4, np.inf, np.inf, np.inf, 14, np.inf, np.inf, 9, 9, 13],
                      [np.inf, 11, 6, 14, np.inf, 16, np.inf, 1, 10, 18, 11, np.inf, np.inf, 13, np.inf],
                      [np.inf, np.inf, 14, 4, 19, 1, 2, 16, 15, np.inf, 15, np.inf, np.inf, np.inf, np.inf],
                      [13, 6, 16, 13, 5, 9, np.inf, 6, 10, 3, 1, 14, np.inf, 17, np.inf],
                      [np.inf, np.inf, 19, 8, np.inf, 2, 4, np.inf, np.inf, 4, 9, 13, 13, 11, 5],
                      [np.inf, 11, 17, 19, 11, 18, np.inf, 8, np.inf, np.inf, 17, 17, 13, 9, 15],
                      [11, 4, np.inf, 3, 3, 8, 5, np.inf, np.inf, np.inf, 20, 19, np.inf, np.inf, 12],
                      [2, np.inf, np.inf, np.inf, np.inf, 16, 7, 13, 4, np.inf, 7, 16, np.inf, 5, 1],
                      [14, 9, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 19, np.inf, 14, 20, 11, 16, np.inf],
                      [3, np.inf, 1, np.inf, 13, np.inf, 9, np.inf, 15, 19, 4, np.inf, np.inf, 2],
                      [np.inf, 8, np.inf, np.inf, np.inf, 6, np.inf, 16, np.inf, np.inf, np.inf, np.inf, 2, 17, 18],
                      [np.inf, np.inf, 11, np.inf, np.inf, 14, 6, np.inf, 15, np.inf, np.inf, 18, np.inf, np.inf, np.inf],
                      [8, np.inf, 5, 1, 7, 14, np.inf, np.inf, np.inf, np.inf, 14, 7, np.inf, 8, np.inf]])

# Define the districts
districts = {1: [0, 1, 2], 2: [3, 4, 5, 6, 7, 8], 3: [9, 10, 11, 12, 13, 14]}

# Define the start and end workshops
start_workshop = (2, 0)
end_workshop = (6, 14)

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

# Find the shortest path from start to end visiting at least one workshop in each district
path = []
for district in districts.values():
    for workshop in district:
        if workshop != start_workshop and workshop != end_workshop:
            path1 = dijkstra_shortest_path(city_map, start_workshop[0]*15 + start_workshop[1], workshop)
            path2 = dijkstra_shortest_path(city_map, workshop, end_workshop[0]*15 + end_workshop[1])
            if path1 is not None and path2 is not None:
                path = path1 + path2[1:]
                break
    if path:
        break

# Convert the path to workshop indices
workshop_path = [(index // 15, index % 15) for index in path]

print(workshop_path)
