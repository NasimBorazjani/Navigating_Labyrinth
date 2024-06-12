
import heapq

# Define the adjacency matrix and the names of the cities
adjacency_matrix = [
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
]

city_names = ['Y', 'O', 'Q', 'X', 'K', 'R', 'A', 'U', 'M', 'L']

# Define a function to find the shortest path using Dijkstra's algorithm
def shortest_path(start, end, visited=None):
    if visited is None:
        visited = set()

    heap = [(0, start, [])]
    while heap:
        (cost, city, path) = heapq.heappop(heap)
        if city not in visited:
            path = path + [city_names[city]]
            visited.add(city)
            if city == end:
                return cost, path

            for i, edge in enumerate(adjacency_matrix[city]):
                if edge and i not in visited:
                    heapq.heappush(heap, (cost + edge, i, path))

    return float('inf')

# Find the shortest path to cities 'A' and 'X'
path_to_A = shortest_path(0, 6)
path_to_X = shortest_path(0, 3)

# Combine the paths and remove duplicates
path = list(set(path_to_A[1] + path_to_X[1]))

# Print the final path
print(path)
