
import numpy as np

# Define the matrix map of the city
city_map = np.array([[6, 9, 19, np.inf, 5, 9, np.inf, 15, np.inf],
                      [8, 10, 16, np.inf, np.inf, np.inf, 5, 11, 4],
                      [5, 11, 20, 1, 14, 16, 7, 1, 5],
                      [10, 5, 3, 5, 12, 8, np.inf, np.inf, 2],
                      [16, 15, 15, 14, np.inf, 13, 10, np.inf, 10],
                      [6, 4, 7, 13, np.inf, np.inf, np.inf, np.inf, 13],
                      [np.inf, 1, 6, 3, np.inf, np.inf, 17, 9, 5],
                      [np.inf, 11, np.inf, 9, np.inf, 5, 7, np.inf, np.inf],
                      [np.inf, np.inf, np.inf, 18, np.inf, 2, np.inf, np.inf, 12]])

# Define the districts
districts = {1: [0, 1], 2: [2, 3, 4], 3: [5, 6, 7, 8]}

# Define the start and end workshops
start_workshop = (1, 8)
end_workshop = (4, 0)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, end):
    distances = {vertex: np.inf for vertex in graph}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}
    vertices = graph.copy()

    while vertices:
        current_vertex = min(vertices, key=lambda vertex: distances[vertex])
        vertices.remove(current_vertex)
        if distances[current_vertex] == np.inf:
            break
        for neighbor, weight in graph[current_vertex].items():
            alternative_route = distances[current_vertex] + weight
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_vertices[neighbor] = current_vertex

    path, current_vertex = [], end
    while previous_vertices[current_vertex] is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]
    if path:
        path.insert(0, start)
    return path

# Create a graph representation of the city map
graph = {}
for i in range(city_map.shape[0]):
    for j in range(city_map.shape[1]):
        if city_map[i, j] != np.inf:
            graph[(i, j)] = {}
            if i > 0 and city_map[i-1, j] != np.inf:
                graph[(i, j)][(i-1, j)] = city_map[i-1, j]
            if i < city_map.shape[0]-1 and city_map[i+1, j] != np.inf:
                graph[(i, j)][(i+1, j)] = city_map[i+1, j]
            if j > 0 and city_map[i, j-1] != np.inf:
                graph[(i, j)][(i, j-1)] = city_map[i, j-1]
            if j < city_map.shape[1]-1 and city_map[i, j+1] != np.inf:
                graph[(i, j)][(i, j+1)] = city_map[i, j+1]

# Find the shortest path from start to end workshop visiting at least one workshop in each district
shortest_path = []
for district in districts.values():
    for workshop in district:
        path = dijkstra_shortest_path(graph, start_workshop, (workshop // city_map.shape[1], workshop % city_map.shape[1]))
        if path:
            shortest_path.extend(path)

shortest_path.extend(dijkstra_shortest_path(graph, shortest_path[-1], end_workshop))

print(shortest_path)
