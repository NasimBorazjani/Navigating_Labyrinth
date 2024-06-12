
from collections import deque

def bfs(graph, start):
    matrix_to_city = {
        0: 'R', 1: 'Y', 2: 'W', 3: 'H', 4: 'J', 5: 'A', 6: 'O', 7: 'N', 8: 'U', 9: 'E', 10: 'Q', 11: 'L', 12: 'P', 13: 'V', 14: 'X'
    }
    city_to_matrix = {v: k for k, v in matrix_to_city.items()}
    graph = {city_to_matrix[k]: [city_to_matrix[i] for i, v in enumerate(v) if v == 1] for k, v in enumerate(graph)}

    queue = deque([(start, [start])])
    visited = set([start])
    dests = set(['Y', 'N'])
    paths = []

    while queue:
        city, path = queue.popleft()
        for i in graph[city]:
            if i in dests and i not in visited:
                if len(list(filter(lambda p: p == i, path))) == 1:
                    if len(list(filter(lambda p: p in dests, path))) == 2:
                        paths.append(path + [i])
            elif i not in visited:
                queue.append((i, path + [i]))
                visited.add(i)

    return min(paths, key=len)

graph = [
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0]
]

print(bfs(graph, 'Q'))
