
from collections import deque

def bfs(graph, start, end):
    queue = deque([(start, [start], 0)])
    visited = set([start])
    shortest_path = None
    shortest_time = float('inf')
    while queue:
        (node, path, time) = queue.popleft()
        for (next_node, travel_time) in graph[node]:
            if next_node not in visited and (shortest_path is None or len(set(path)) == len(set(shortest_path))):
                new_time = time + travel_time
                new_path = path + [next_node]
                if next_node == end and new_time < shortest_time:
                    shortest_path = new_path
                    shortest_time = new_time
                else:
                    queue.append((next_node, new_path, new_time))
                    visited.add(next_node)
    return shortest_path

def solve(matrix, start, end):
    graph = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 'x':
                graph[(i, j)] = []
                if i > 0 and matrix[i-1][j] != 'x':
                    graph[(i, j)].append(((i-1, j), matrix[i-1][j]))
                if i < len(matrix)-1 and matrix[i+1][j] != 'x':
                    graph[(i, j)].append(((i+1, j), matrix[i+1][j]))
                if j > 0 and matrix[i][j-1] != 'x':
                    graph[(i, j)].append(((i, j-1), matrix[i][j-1]))
                if j < len(matrix[i])-1 and matrix[i][j+1] != 'x':
                    graph[(i, j)].append(((i, j+1), matrix[i][j+1]))
    return bfs(graph, start, end)

matrix = [
    ['x', 'x', 6, 'x', 7, 'x', 9, 4, 11],
    ['x', 3, 'x', 6, 5, 3, 15, 'x', 3],
    ['x', 'x', 'x', 4, 'x', 9, 1, 8, 'x'],
    [15, 18, 1, 6, 5, 10, 6, 14, 8],
    [18, 10, 7, 18, 2, 'x', 'x', 'x', 7],
    [11, 9, 16, 'x', 11, 'x', 11, 'x', 17],
    [7, 'x', 18, 'x', 8, 10, 20, 6, 'x'],
    [15, 4, 17, 'x', 16, 2, 12, 16, 'x'],
    [9, 10, 18, 17, 9, 6, 7, 'x', 15]
]
start = (3, 0)
end = (6, 6)
print(solve(matrix, start, end))
