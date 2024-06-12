
import numpy as np

# Define the matrix map of the city
city_map = np.array([[19, 12, np.inf, np.inf, 2, 5, 4, 13, 17, 19, np.inf, 2],
                      [np.inf, 18, np.inf, 5, 5, np.inf, np.inf, 8, 12, 18, np.inf, 15],
                      [np.inf, 9, 4, 10, 7, 20, np.inf, 16, 20, 13, 15, np.inf],
                      [8, np.inf, np.inf, 11, 1, 19, np.inf, 14, 6, np.inf, 3, np.inf],
                      [10, np.inf, 4, 8, 17, np.inf, 18, np.inf, 7, np.inf, 6, 5],
                      [np.inf, np.inf, 3, 1, 8, 18, np.inf, 4, 17, np.inf, np.inf, 13],
                      [np.inf, np.inf, 6, np.inf, np.inf, np.inf, 14, np.inf, np.inf, 10, 10, np.inf],
                      [np.inf, np.inf, 15, np.inf, np.inf, np.inf, np.inf, 2, np.inf, np.inf, np.inf, np.inf],
                      [np.inf, np.inf, 5, 11, 6, 1, np.inf, 6, 14, np.inf, np.inf, np.inf],
                      [np.inf, 1, 17, 10, 15, np.inf, 14, 6, np.inf, np.inf, np.inf, np.inf],
                      [12, 2, np.inf, 10, np.inf, np.inf, 7, np.inf, np.inf, np.inf, np.inf, np.inf],
                      [np.inf, 9, 14, np.inf, 9, 18, 14, np.inf, np.inf, np.inf, 6, np.inf]])

# Define the districts
districts = {1: [0, 1], 2: [2, 5], 3: [6, 11]}

# Define the start and end workshops
start_workshop = (6, 2)
end_workshop = (2, 10)

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
    district_workshops = []
    for i in range(district[0], district[1]+1):
        for j in range(city_map.shape[1]):
            if city_map[i, j] != np.inf and (i, j) != start_workshop and (i, j) != end_workshop:
                district_workshops.append((i, j))
    for workshop in district_workshops:
        path1 = dijkstra_shortest_path(graph, start_workshop, workshop)
        path2 = dijkstra_shortest_path(graph, workshop, end_workshop)
        if path1 and path2:
            shortest_path = path1 + path2[1:]
            break
    if shortest_path:
        break

print(shortest_path)
