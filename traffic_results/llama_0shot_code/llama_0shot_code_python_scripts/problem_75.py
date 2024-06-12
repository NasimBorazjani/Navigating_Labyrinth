
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    distances = [[float('inf')] * cols for _ in range(rows)]
    previous_nodes = [[None] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    districts = [range(0, 3), range(3, 8), range(8, 13)]
    district_visited = [False, False, False]

    queue = [(0, start)]
    while queue:
        current_distance, (current_row, current_col) = heapq.heappop(queue)
        if visited[current_row][current_col]:
            continue
        visited[current_row][current_col] = 1
        for direction in directions:
            new_row, new_col = current_row + direction[0], current_col + direction[1]
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] != 'x':
                distance = current_distance + matrix[new_row][new_col]
                if distance < distances[new_row][new_col]:
                    distances[new_row][new_col] = distance
                    previous_nodes[new_row][new_col] = (current_row, current_col)
                    heapq.heappush(queue, (distance, (new_row, new_col)))
                if new_row in districts[0] and not district_visited[0]:
                    district_visited[0] = True
                elif new_row in districts[1] and not district_visited[1]:
                    district_visited[1] = True
                elif new_row in districts[2] and not district_visited[2]:
                    district_visited[2] = True
                if all(district_visited):
                    return distances, previous_nodes
    return distances, previous_nodes

def get_path(previous_nodes, start, end):
    path = [end]
    while previous_nodes[path[-1][0]][path[-1][1]]:
        path.append(previous_nodes[path[-1][0]][path[-1][1]])
    path.append(start)
    path.reverse()
    return [(i, j) for i, j in path if matrix[i][j] != 'x']

matrix = [
    ['x', 9, 4, 8, 'x', 'x', 4, 'x', 8, 12, 'x', 'x', 14],
    [17, 'x', 3, 'x', 6, 'x', 'x', 'x', 5, 19],
    ['x', 8, 8, 'x', 5, 'x', 15, 14, 3, 10, 12, 3],
    [4, 'x', 16, 'x', 'x', 12, 'x', 'x', 6, 5, 18, 19],
    ['x', 4, 9, 17, 'x', 'x', 'x', 13, 4, 7, 'x', 2, 16],
    [3, 6, 'x', 'x', 'x', 10, 5, 'x', 18, 10, 9, 20, 4],
    ['x', 'x', 'x', 14, 18, 'x', 'x', 'x', 'x', 16, 'x', 'x', 4],
    [14, 12, 'x', 4, 12, 11, 19, 'x', 3, 2, 'x', 13, 'x'],
    [19, 6, 2, 18, 'x', 'x', 8, 7, 1, 12, 19, 'x', 'x'],
    ['x', 9, 16, 17, 5, 12, 19, 8, 'x', 3, 10, 'x', 'x'],
    ['x', 10, 3, 'x', 14, 16, 2, 16, 4, 10, 18, 15, 'x'],
    [15, 5, 5, 'x', 13, 'x', 7, 'x', 4, 1, 17, 15],
    [5, 2, 6, 'x', 'x', 'x', 'x', 8, 16, 'x', 'x', 'x', 'x']
]

distances, previous_nodes = dijkstra((len(matrix), len(matrix[0])), (7, 1), (2, 10))
path = get_path(previous_nodes, (7, 1), (2, 10))
print(path)
