
import heapq

def shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start, end = (7, 0), (2, 9)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    # Convert matrix to graph
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Dijkstra's algorithm
    shortest_distances = {node: float('infinity') for node in graph}
    shortest_distances[start] = 0
    unvisited = [(0, start)]
    while unvisited:
        current_distance, current_node = heapq.heappop(unvisited)
        if current_distance > shortest_distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(unvisited, (distance, neighbor))
    
    # Backtrack from end node to find the path
    path = [end]
    while path[-1] != start:
        for node in graph:
            if node not in path and shortest_distances[node] + graph[node][path[-1]] == shortest_distances[path[-1]]:
                path.append(node)
                break
    path.reverse()

    # Ensure that the path visits at least one node from each district
    districts = {0: [], 1: [], 2: []}
    for node in path:
        districts[node[0] // 3].append(node)
    for district in districts.values():
        if not district:
            district_nodes = [node for node in path if node[0] in {0, 1, 2}]
            district.append(min(district_nodes, key=lambda node: shortest_distances[node]))

    return [(i, j) for i, j in path if i != 2 or j not in {0, 1, 2, 3, 4, 5, 6, 7, 8}]

matrix = [
    "12 11 14 10 2 11 13 16 3 x 12",
    "10 9 x 8 x x 1 16 11 x 15",
    "1 18 1 x x x x x 12 9 x",
    "1 14 15 10 7 15 17 10 15 15 6",
    "18 11 x x x 15 x x 1 1 x",
    "14 x x x 18 14 16 7 x 1 x",
    "11 15 x x 15 3 11 13 x x x",
    "5 x x x x x 15 x 6 x x",
    "12 11 7 2 11 x 10 2 17 x x",
    "7 x x x 4 x 4 x x 5 x",
    "x 19 10 7 x 2 3 9 2 6 x"
]
matrix = [[int(x) if x.isdigit() else x for x in row.split()] for row in matrix]

print(shortest_path(matrix))
