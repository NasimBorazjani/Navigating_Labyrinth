
from collections import deque

def bfs(graph, start, end):
    queue = deque([(start, [start])])
    while queue:
        (node, path) = queue.popleft()
        for next_node in graph[node] - set(path):
            if next_node == end:
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))

def solve(matrix, start, end):
    graph = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 'x':
                graph[(i, j)] = set()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x, y = i + dx, j + dy
                    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] != 'x':
                        graph[(i, j)].add((x, y))

    paths = list(bfs(graph, start, end))
    for path in paths:
        districts = {1, 2, 3}
        for i, j in path:
            if i < 3:
                districts.discard(1)
            elif i < 7:
                districts.discard(2)
            else:
                districts.discard(3)
        if not districts:
            return path

    return None
