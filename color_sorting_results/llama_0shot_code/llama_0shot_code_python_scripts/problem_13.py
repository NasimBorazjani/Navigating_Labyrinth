
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
                return (cost, path)
            for (next_node, edge_cost) in graph[node]:
                if next_node not in seen:
                    heappush(queue, (cost + edge_cost, next_node, path))
    return float("inf")

def sort_it(tubes):
    graph = {}
    for i, tube1 in enumerate(tubes):
        for j, tube2 in enumerate(tubes):
            if i != j and len(tube2[1]) < 6:
                ball1 = tube1[0]
                ball2 = tube2[0]
                if ball1 != ball2:
                    if (ball1, len(tube1[1]), i) not in graph:
                        graph[(ball1, len(tube1[1]), i)] = []
                    if (ball2, len(tube2[1]), j) not in graph:
                        graph[(ball2, len(tube2[1]), j)] = []
                    graph[(ball1, len(tube1[1]), i)].append(((ball2, len(tube2[1]), j), 1))
                    graph[(ball2, len(tube2[1]), j)].append(((ball1, len(tube1[1]), i), 1))
    start = (tubes[0][0], len(tubes[0][1]), 0)
    end = (tubes[0][0], 4, 0)
    cost, path = shortest_path(graph, start, end)
    return [(path[i], path[i+1]) for i in range(0, len(path), 2)][1:]

tubes = [('Green', 4), ('Blue', 4), ('Red', 4)]
print(sort_it(tubes))
