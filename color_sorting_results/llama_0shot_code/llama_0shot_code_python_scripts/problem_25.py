
from collections import deque
from heapq import heappop, heappush

def shortest_path(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    while queue:
        (cost, node, path) = heappop(queue)
        if node not in seen:
            seen.add(node)
            path = path + [node]
            if node == end:
                return cost, path
            for c, neighbour in graph[node]:
                if neighbour not in seen:
                    heappush(queue, (cost + c, neighbour, path))
    return float('inf')

def sort_it(tubes):
    graph = {}
    for i, tube1 in enumerate(tubes):
        for j, tube2 in enumerate(tubes):
            if i != j:
                color1, count1 = tube1[0], len(tube1)
                color2, count2 = tube2[0], len(tube2)
                if count2 < 6 and color1 != color2:
                    graph[(i, j)] = (1, (color1, count1), (color2, count2))
    start = tuple(tubes)
    end = tuple(('', 0) for _ in tubes)
    _, path = shortest_path(graph, start, end)
    return [(path[i], path[i+1]) for i in range(0, len(path), 2)]

tubes = [['Green', 'Green', 'Red', 'Red'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Red', 'Green', 'Red']]
print(sort_it(tubes))
