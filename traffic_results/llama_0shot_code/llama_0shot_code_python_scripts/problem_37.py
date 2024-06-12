
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    # Convert matrix into graph
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Dijkstra's algorithm
    visited = set()
    paths = {start: (None, matrix[start[0]][start[1]])}
    queue = [(matrix[start[0]][start[1]], start)]
    while queue:
        _, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == end:
                path = []
                while node is not None:
                    path.append(node)
                    node = paths[node][0]
                return path[::-1]

            for neighbor, cost in graph[node].items():
                old_cost = paths.get(neighbor, (None, float('inf')))[1]
                new_cost = paths[node][1] + cost
                if new_cost < old_cost:
                    paths[neighbor] = (node, new_cost)
                    heapq.heappush(queue, (new_cost, neighbor))

    return None

def get_district(row):
    if 0 <= row <= 1:
        return 1
    elif 2 <= row <= 6:
        return 2
    elif 7 <= row <= 10:
        return 3

def main(matrix):
    start, end = (7, 5), (1, 0)
    path = dijkstra(matrix, start, end)
    if path is None:
        return "No path found"

    districts_visited = set(get_district(node[0]) for node in path)
    if len(districts_visited) < 3:
        # Find the district with the highest number that has not been visited yet
        missing_districts = [d for d in range(1, 4) if d not in districts_visited]
        for district in sorted(missing_districts, reverse=True):
            # Add the first workshop in this district to the path
            for i in range(len(matrix)):
                if get_district(i) == district:
                    for j in range(len(matrix[0])):
                        if matrix[i][j] != 'x':
                            path.insert(0, (i, j))
                            break
                    break
            break

    return [(matrix[node[0]][node[1]] if matrix[node[0]][node[1]] != 'x' else 'x') for node in path]

matrix = [
    [15, 'x', 12, 9, 19, 'x', 13, 'x', 16],
    [14, 6, 3, 18, 'x', 8, 18, 'x', 'x', 'x', 'x'],
    [16, 10, 9, 4, 9, 5, 15, 4, 'x', 'x', 2],
    [5, 9, 'x', 8, 1, 15, 7, 15, 'x', 'x', 'x'],
    [6, 'x', 3, 'x', 4, 6, 6, 19, 'x', 16, 13],
    [17, 'x', 11, 5, 18, 11, 18, 'x', 'x', 10, 19],
    [6, 3, 'x', 'x', 10, 18, 2, 'x', 'x', 'x', 'x'],
    ['x', 'x', 4, 2, 'x', 13, 7, 'x', 3, 19, 16],
    ['x', 1, 10, 'x', 15, 'x', 2, 'x', 1, 7, 10],
    ['x', 'x', 'x', 4, 7, 'x', 7, 'x', 'x', 6, 'x'],
    [16, 'x', 15, 3, 'x', 8, 'x', 13, 'x', 14]
]

print(main(matrix))
