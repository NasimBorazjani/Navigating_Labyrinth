
from collections import deque

def bfs(graph, start, end, district):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in graph[vertex] - set(path):
            if next == end and path[-1][0] in district:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def solve(matrix, start, end):
    graph = {i: set() for i in range(len(matrix))}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 'x':
                if i > 0 and matrix[i-1][j] != 'x':
                    graph[(i, j)].add((i-1, j))
                if i < len(matrix)-1 and matrix[i+1][j] != 'x':
                    graph[(i, j)].add((i+1, j))
                if j > 0 and matrix[i][j-1] != 'x':
                    graph[(i, j)].add((i, j-1))
                if j < len(matrix[i])-1 and matrix[i][j+1] != 'x':
                    graph[(i, j)].add((i, j+1))
    paths = list(bfs(graph, start, end, range(4, 9)))
    min_path = min(paths, key=len)
    return min_path
