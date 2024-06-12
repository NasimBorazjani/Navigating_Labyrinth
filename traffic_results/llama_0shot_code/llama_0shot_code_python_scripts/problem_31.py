
import heapq

def shortest_path(matrix):
    # Convert matrix into graph
    graph = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
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
                if j < len(matrix[0]) - 1 and matrix[i][j+1] != 'x':
                    graph[node][(i, j+1)] = matrix[i][j+1]

    # Use Dijkstra's algorithm to find shortest path
    queue = [(matrix[3][7], (3, 7))]
    visited = set()
    while queue:
        dist, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == (7, 0):
                path = [node]
                while node != (3, 7):
                    dist, node = min((dist, prev_node) for prev_node, dist in graph[node].items() if prev_node in visited)
                    path.append(node)
                return [(i, j) for j, i in path[::-1]]
            for next_node, next_dist in graph[node].items():
                heapq.heappush(queue, (dist + next_dist, next_node))

    return None

matrix = [
    [10, 'x', 19, 11, 'x', 'x', 6, 12, 'x', 'x'],
    [2, 9, 10, 'x', 'x', 10, 17, 'x', 'x', 11, 5],
    ['x', 15, 8, 9, 'x', 7, 17, 20, 'x', 'x', 13],
    [1, 9, 15, 14, 9, 9, 13, 7, 12, 'x', 10],
    [9, 'x', 17, 'x', 'x', 7, 'x', 1, 14],
    [16, 18, 11, 'x', 14, 18, 9, 13, 'x', 'x', 'x'],
    [9, 3, 5, 8, 17, 15, 19, 'x', 3, 'x', 14],
    [2, 13, 'x', 'x', 17, 13, 14, 18, 9, 'x', 6],
    [3, 'x', 18, 6, 'x', 14, 'x', 'x', 8, 19],
    [2, 4, 'x', 'x', 'x', 'x', 3, 4, 'x', 19, 'x'],
    ['x', 'x', 'x', 'x', 11, 'x', 'x', 'x', 'x', 5, 5]
]

print(shortest_path(matrix))
