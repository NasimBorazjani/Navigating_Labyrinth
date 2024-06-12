
from collections import deque

def bfs(graph, start, end, districts):
    queue = deque([(start, [start], set([districts[start]]))])
    while queue:
        (vertex, path, visited_districts) = queue.popleft()
        for next in graph[vertex] - set(path):
            if next == end and len(visited_districts) == 3:
                return path + [next]
            else:
                queue.append((next, path + [next], visited_districts | set([districts[next]])))

def solve(matrix, start, end):
    graph = {i: set() for i in range(len(matrix) * len(matrix[0])) if matrix[i // len(matrix[0])][i % len(matrix[0])] != 'x'}
    districts = {i: i // len(matrix[0]) // 4 + 1 for i in range(len(matrix) * len(matrix[0])) if matrix[i // len(matrix[0])][i % len(matrix[0])] != 'x'}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 'x':
                if i > 0 and matrix[i - 1][j] != 'x':
                    graph[i * len(matrix[0]) + j].add((i - 1) * len(matrix[0]) + j)
                if i < len(matrix) - 1 and matrix[i + 1][j] != 'x':
                    graph[i * len(matrix[0]) + j].add((i + 1) * len(matrix[0]) + j)
                if j > 0 and matrix[i][j - 1] != 'x':
                    graph[i * len(matrix[0]) + j].add(i * len(matrix[0]) + j - 1)
                if j < len(matrix[0]) - 1 and matrix[i][j + 1] != 'x':
                    graph[i * len(matrix[0]) + j].add(i * len(matrix[0]) + j + 1)
    return bfs(graph, start[0] * len(matrix[0]) + start[1], end[0] * len(matrix[0]) + end[1], districts)
