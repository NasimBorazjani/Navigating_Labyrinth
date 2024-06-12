
import numpy as np

# Define the matrix map of the city
city_map = np.array([[10, np.inf, np.inf, np.inf, 16, 9, np.inf, 13, 12, 8, np.inf, 16, 17],
                      [9, 2, np.inf, np.inf, 5, np.inf, np.inf, np.inf, 12, np.inf, 3, np.inf, np.inf],
                      [np.inf, np.inf, 7, 3, 12, np.inf, 11, 18, 10, np.inf, np.inf, 13, np.inf],
                      [np.inf, 6, np.inf, 19, 2, np.inf, np.inf, 11, 13, 13, 1, np.inf, 7],
                      [np.inf, np.inf, 11, np.inf, 16, 16, 4, 12, 5, 20, 2, 4, 15],
                      [19, np.inf, 18, 5, 11, np.inf, np.inf, 3, 17, 18, 3, 8, 18],
                      [12, np.inf, 9, np.inf, np.inf, np.inf, np.inf, 9, 4, 15, 16, np.inf, 9],
                      [np.inf, 15, np.inf, 6, 10, np.inf, 1, 1, np.inf, 9, 4, 7, 1],
                      [np.inf, 19, 15, np.inf, 1, 10, 5, 17, np.inf, 8, np.inf, 1, np.inf],
                      [np.inf, np.inf, np.inf, np.inf, 5, np.inf, 1, np.inf, np.inf, 7, 4, np.inf, np.inf],
                      [9, np.inf, 4, np.inf, 5, 13, np.inf, 15, np.inf, np.inf, 18, 9, 15],
                      [17, 2, np.inf, np.inf, np.inf, 18, 8, np.inf, 8, np.inf, np.inf, 8, 7],
                      [np.inf, np.inf, 5, np.inf, np.inf, 8, np.inf, 8, np.inf, 15, 19, np.inf, np.inf]])

# Define the districts
districts = {1: (0, 3), 2: (4, 6), 3: (7, 12)}

# Define the start and end workshops
start_workshop = (3, 12)
end_workshop = (7, 3)

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

# Find the shortest path from start to end workshop visiting at least one workshop in each district
shortest_path = []
for district in districts.values():
    district_path = dijkstra_shortest_path(city_map, start_workshop[0]*13 + start_workshop[1], end_workshop[0]*13 + end_workshop[1])
    shortest_path.extend(district_path)
    start_workshop = (district_path[-1] // 13, district_path[-1] % 13)

# Print the shortest path
print([(workshop // 13, workshop % 13) for workshop in shortest_path])
