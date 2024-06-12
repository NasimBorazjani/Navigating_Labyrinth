
import heapq

def create_graph(matrix):
    rows, cols = len(matrix), len(matrix[0])
    graph = {}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                node = (i, j)
                if node not in graph:
                    graph[node] = {}
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != 'x' and (nx // 3 != i // 3 or ny // 3 != j // 3):
                        graph[node][(nx, ny)] = matrix[nx][ny]
    return graph

def shortest_path(graph, start, end):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        dist, node, path = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return path
            for neighbor, cost in graph[node].items():
                heapq.heappush(queue, (dist + cost, neighbor, path))
    return None

matrix = [['x', 'x', 3, 10, 20, 3, 'x', 5],
          ['x', 'x', 'x', 'x', 20, 16, 'x', 'x', 17],
          [3, 14, 18, 8, 1, 20, 14, 'x', 7],
          [13, 3, 6, 10, 7, 4, 6, 6, 1],
          [10, 12, 2, 'x', 11, 'x', 10, 8, 11],
          ['x', 'x', 'x', 11, 6, 18, 13, 20, 17],
          ['x', 'x', 16, 'x', 4, 17, 7, 10, 15],
          ['x', 7, 16, 6, 19, 4, 7, 'x', 'x'],
          ['x', 11, 18, 'x', 'x', 'x', 3, 8, 'x']]

graph = create_graph(matrix)
start, end = (5, 7), (2, 1)
path = shortest_path(graph, start, end)
print(path)
