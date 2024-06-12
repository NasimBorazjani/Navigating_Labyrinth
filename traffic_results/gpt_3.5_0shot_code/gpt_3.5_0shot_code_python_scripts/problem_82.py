
import numpy as np

# Define the matrix map of the city
city_map = np.array([[15, 19, 13, 4, np.inf, np.inf, 13, 7, 16, 6, np.inf, np.inf, 17, np.inf],
                      [2, 2, np.inf, 7, np.inf, 12, 12, np.inf, 19, np.inf, 10, 4, 14, 2],
                      [11, np.inf, np.inf, 3, 7, np.inf, 7, np.inf, np.inf, 6, np.inf, 19, np.inf, 1],
                      [np.inf, np.inf, 11, np.inf, 3, np.inf, 17, np.inf, 1, 20, 17, 8, 15, 1],
                      [np.inf, np.inf, 13, np.inf, 12, 17, 5, 4, np.inf, 16, 9, np.inf, 19, 14],
                      [np.inf, 16, np.inf, np.inf, 13, 17, 14, 6, 2, 17, 19, 6, 13, 6],
                      [np.inf, 1, np.inf, np.inf, 3, 10, 2, 18, 7, 8, np.inf, 8, np.inf, np.inf],
                      [12, 2, 1, 6, 11, 7, 10, np.inf, np.inf, np.inf, 4, 2, 8, np.inf],
                      [np.inf, np.inf, np.inf, 13, 16, 2, np.inf, 6, 9, 2, 11, 7, 14, 6],
                      [np.inf, np.inf, np.inf, np.inf, np.inf, 11, np.inf, 16, np.inf, np.inf, np.inf, np.inf, np.inf, 3],
                      [np.inf, np.inf, np.inf, np.inf, 10, np.inf, 3, np.inf, 18, 9, np.inf, np.inf, np.inf, 15],
                      [np.inf, np.inf, 11, 9, 3, np.inf, np.inf, 16, np.inf, 5, np.inf, 4, 10, np.inf],
                      [18, 1, 13, np.inf, 7, np.inf, 7, 5, np.inf, 11, 10, 2, np.inf, 2],
                      [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 11, np.inf, 10, np.inf, np.inf, 14, 6]])

# Define the districts
districts = {1: [0, 1], 2: [2, 6], 3: [7, 13]}

# Define the destination workshop
destination = (7, 4)

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

# Find the shortest path from Ben's current workshop to the destination workshop
shortest_path = None
for workshop1 in range(len(city_map)):
    if districts[1][0] <= workshop1 <= districts[1][1]:
        for workshop2 in range(len(city_map)):
            if districts[2][0] <= workshop2 <= districts[2][1]:
                for workshop3 in range(len(city_map)):
                    if districts[3][0] <= workshop3 <= districts[3][1]:
                        path1 = dijkstra_shortest_path(city_map, 1*14 + 13, workshop1)
                        path2 = dijkstra_shortest_path(city_map, workshop1, workshop2)
                        path3 = dijkstra_shortest_path(city_map, workshop2, workshop3)
                        path4 = dijkstra_shortest_path(city_map, workshop3, 7*14 + 4)
                        if path1 and path2 and path3 and path4:
                            shortest_path = path1 + path2[1:] + path3[1:] + path4
                            break
                if shortest_path:
                    break
            if shortest_path:
                break
        if shortest_path:
            break

# Convert the indices to coordinates
shortest_path_coords = [(workshop // 14, workshop % 14) for workshop in shortest_path]

print(shortest_path_coords)
