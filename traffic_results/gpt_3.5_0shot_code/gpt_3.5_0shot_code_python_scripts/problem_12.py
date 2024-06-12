
import numpy as np

# Define the matrix map of the city
city_map = np.array([[19, -1, 17, 14, 3, -1, 10, 5, 2],
                      [-1, -1, 1, -1, -1, -1, -1, 19, 7],
                      [16, 12, -1, 3, 19, 2, 14, 1, 14],
                      [-1, 1, 16, -1, 12, 3, 13, -1, 3],
                      [-1, -1, 7, 19, 10, -1, 5, -1, 19],
                      [5, -1, -1, 6, 14, -1, -1, 10, 12],
                      [-1, -1, -1, -1, 18, -1, -1, 15, 12],
                      [-1, -1, 16, 8, -1, 3, 4, -1, -1],
                      [-1, -1, -1, 16, -1, -1, 8, 14, 7]])

# Define the districts
districts = {1: range(0, 4), 2: range(4, 5), 3: range(5, 9)}

# Define the start and end workshops
start_workshop = (3, 1)
end_workshop = (5, 8)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    parents = {}
    visited = set()

    while len(visited) < len(graph):
        current_vertex = min({vertex: distances[vertex] for vertex in distances if vertex not in visited}, key=distances.get)
        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            if weight + distances[current_vertex] < distances[neighbor]:
                distances[neighbor] = weight + distances[current_vertex]
                parents[neighbor] = current_vertex

    path = []
    while end is not None:
        path.insert(0, end)
        end = parents.get(end)

    return path

# Create a graph representation of the city map
graph = {}
for i in range(city_map.shape[0]):
    for j in range(city_map.shape[1]):
        if city_map[i, j] != -1:
            graph[(i, j)] = {}
            if i > 0 and city_map[i-1, j] != -1:
                graph[(i, j)][(i-1, j)] = city_map[i-1, j]
            if i < city_map.shape[0]-1 and city_map[i+1, j] != -1:
                graph[(i, j)][(i+1, j)] = city_map[i+1, j]
            if j > 0 and city_map[i, j-1] != -1:
                graph[(i, j)][(i, j-1)] = city_map[i, j-1]
            if j < city_map.shape[1]-1 and city_map[i, j+1] != -1:
                graph[(i, j)][(i, j+1)] = city_map[i, j+1]

# Find the shortest path from start to end workshop visiting at least one workshop in each district
shortest_path = []
for district in districts.values():
    for workshop in district:
        path = dijkstra_shortest_path(graph, start_workshop, (workshop, start_workshop[1]))
        if path:
            shortest_path.extend(path)
            start_workshop = (workshop, start_workshop[1])
            break

path = dijkstra_shortest_path(graph, start_workshop, end_workshop)
shortest_path.extend(path)

print(shortest_path)
