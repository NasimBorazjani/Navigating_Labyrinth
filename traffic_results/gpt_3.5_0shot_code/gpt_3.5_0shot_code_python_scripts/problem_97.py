
import numpy as np

# Define the matrix map of the city
city_map = np.array([[17, 8, -1, 3, -1, 13, -1, -1, 14, 11, -1, -1, -1, -1, -1],
                      [-1, -1, -1, 7, -1, -1, 13, -1, -1, -1, -1, -1, 16, -1, 13],
                      [-1, -1, 2, -1, -1, 12, 10, -1, -1, -1, 2, -1, -1, 5, 17],
                      [4, 3, -1, 14, -1, -1, 16, -1, -1, -1, 1, -1, -1, -1, -1],
                      [9, -1, 18, 11, 19, 5, -1, -1, -1, -1, -1, -1, 3, -1, -1],
                      [-1, 14, -1, 4, 14, 12, 1, -1, 13, 7, 10, 8, 8, 6, 9],
                      [7, 10, -1, 18, 15, 8, 13, 14, 15, -1, -1, -1, 13, -1, 17],
                      [17, 7, 19, 15, 20, 19, -1, 15, 13, -1, 9, -1, 11, -1, 1],
                      [-1, 9, 6, 17, 14, -1, 16, -1, 19, 11, -1, 14, 11, -1, -1],
                      [-1, 18, 8, 2, 14, 2, 4, -1, 4, 4, 4, -1, -1, 8, 19],
                      [-1, -1, 5, -1, -1, -1, 1, 5, -1, 11, -1, -1, 1, 14, -1],
                      [-1, -1, -1, -1, 5, -1, 10, -1, -1, -1, -1, 10, 18, -1, 19],
                      [-1, -1, 2, -1, 1, -1, -1, -1, -1, -1, -1, -1, 6, 16, -1],
                      [x, 12, 1, 12, -1, -1, 15, 7, 18, 15, 13, 19, -1, 2, -1],
                      [x, 13, 8, 19, 5, 1, -1, 13, -1, -1, -1, 17, -1, 3, -1]])

# Define the districts
districts = {1: range(0, 6), 2: range(6, 9), 3: range(9, 15)}

# Define the starting and ending workshops
start_workshop = (9, 1)
end_workshop = (7, 14)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, end):
    nodes = set(range(len(graph)))
    dist = {node: float('inf') for node in nodes}
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
            if weight != -1 and neighbor in unvisited:
                alt = dist[current] + weight
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = current

    return None

# Find the shortest path from start to end visiting at least one workshop in each district
shortest_path = None
for district in districts.values():
    for workshop in district:
        path1 = dijkstra_shortest_path(city_map, start_workshop[0]*15 + start_workshop[1], workshop)
        if path1 is None:
            continue
        for workshop2 in district:
            if workshop2 != workshop:
                path2 = dijkstra_shortest_path(city_map, workshop, workshop2)
                if path2 is None:
                    continue
                path3 = dijkstra_shortest_path(city_map, workshop2, end_workshop[0]*15 + end_workshop[1])
                if path3 is None:
                    continue
                path = path1 + path2[1:] + path3[1:]
                if shortest_path is None or len(path) < len(shortest_path):
                    shortest_path = path

# Convert the indices to coordinates
shortest_path_coords = [(index // 15, index % 15) for index in shortest_path]

print(shortest_path_coords)
