
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    # Convert the matrix into a graph
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Run Dijkstra's algorithm
    queue = [(matrix[start[0]][start[1]], start)]
    shortest_distances = {start: 0}
    previous_nodes = {}
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node == end:
            break
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if neighbor not in shortest_distances or distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Backtrack to find the shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes.get(current_node)
    path.reverse()

    # Ensure that the path visits at least one workshop in each district
    districts = [range(0, 4), range(4, 9), range(9, 12)]
    district_workshops = [list(filter(lambda node: node[0] in district, path)) for district in districts]
    for i in range(1, len(districts)):
        if not district_workshops[i]:
            for node in path:
                if node[0] in districts[i - 1]:
                    district_workshops[i].append(node)
                    break
    path = sum((district_workshops[i][::-1] + district_workshops[i + 1]) for i in range(len(districts) - 1), []) + district_workshops[-1]

    return path

matrix = [
    "19 14 16 4 15 16 15 x 9 x x x",
    "x 7 12 6 x 12 x 3 x 14 5 9",
    "1 12 x x 12 x x x x x 10 1",
    "x 1 15 14 x 2 13 x x x 10 9",
    "7 x 13 x 14 1 14 8 x x 8 5",
    "18 x 8 13 12 13 x 12 3 x 14 x",
    "x 15 x x x x x x x x 17 10",
    "x 5 x 4 x x x 3 5 6 6 11",
    "x 15 6 x 4 18 x x 14 10 2 8",
    "13 10 13 7 3 6 x x 10 17 10 15",
    "4 x x 7 19 4 13 13 12 x x 13",
    "5 x x 9 19 18 x x 16 x 2 x"
]
matrix = [[int(x) if x != 'x' else 'x' for x in row.split()] for row in matrix]

start, end = (4, 11), (9, 2)
print(shortest_path(matrix, start, end))
