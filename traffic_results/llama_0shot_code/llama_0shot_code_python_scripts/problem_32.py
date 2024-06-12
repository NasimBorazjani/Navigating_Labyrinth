
import heapq

def shortest_path(matrix):
    # Step 1: Convert the matrix into a graph
    graph = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 'x':
                node = (i, j)
                if node not in graph:
                    graph[node] = {}
                if i > 0 and matrix[i-1][j] != 'x':
                    graph[node][(i-1, j)] = matrix[i-1][j]
                if i < len(matrix) - 1 and matrix[i+1][j] != 'x':
                    graph[node][(i+1, j)] = matrix[i+1][j]
                if j > 0 and matrix[i][j-1] != 'x':
                    graph[node][(i, j-1)] = matrix[i][j-1]
                if j < len(matrix[i]) - 1 and matrix[i][j+1] != 'x':
                    graph[node][(i, j+1)] = matrix[i][j+1]

    # Step 2: Implement Dijkstra's algorithm
    start = (5, 2)
    end = (2, 10)
    shortest_distances = {node: float('infinity') for node in graph}
    shortest_distances[start] = 0
    unvisited_nodes = [(0, start)]
    while unvisited_nodes:
        current_distance, current_node = heapq.heappop(unvisited_nodes)
        if current_distance > shortest_distances[current_node]:
            continue
        for neighbour, distance in graph[current_node].items():
            distance_from_start = current_distance + distance
            if distance_from_start < shortest_distances[neighbour]:
                shortest_distances[neighbour] = distance_from_start
                heapq.heappush(unvisited_nodes, (distance_from_start, neighbour))

    # Step 3: Check if the path visits at least one node in each district
    districts = {1: [(0, i) for i in range(3)], 2: [(i, j) for i in range(3, 5)], 3: [(i, j) for i in range(5, 11)]}
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node)
        for node, distance in graph[current_node].items():
            if shortest_distances[node] + distance == shortest_distances[current_node]:
                current_node = node
                break
    path.append(start)
    path = path[::-1]
    districts_visited = set()
    for node in path:
        for district, nodes in districts.items():
            if node in nodes and district not in districts_visited:
                districts_visited.add(district)
    if len(districts_visited) != len(districts):
        return "It's not possible to visit at least one workshop in each district."

    # Step 4: Return the path
    return [(i, j) for i, j in path]

matrix = [
    ['x', 'x', 13, 'x', 7, 'x', 13, 3, 'x', 13],
    [10, 4, 'x', 4, 12, 2, 'x', 3, 4, 'x', 15],
    ['x', 3, 'x', 'x', 15, 9, 'x', 'x', 18, 17, 14],
    [5, 'x', 'x', 'x', 3, 'x', 11, 'x', 17, 9, 17],
    [8, 3, 13, 'x', 5, 7, 8, 17, 7, 'x', 'x'],
    ['x', 'x', 13, 2, 2, 11, 6, 8, 'x', 'x', 'x'],
    ['x', 1, 9, 6, 5, 13, 16, 1, 7, 5, 'x'],
    [4, 'x', 13, 'x', 10, 18, 3, 'x', 'x', 19, 19],
    ['x', 'x', 'x', 2, 5, 9, 13, 'x', 7, 1, 'x'],
    ['x', 'x', 7, 'x', 'x', 5, 19, 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 6, 'x', 19, 'x', 'x', 'x', 'x', 1]
]

print(shortest_path(matrix))
