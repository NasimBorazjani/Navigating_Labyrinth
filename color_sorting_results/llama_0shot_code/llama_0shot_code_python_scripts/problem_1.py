
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
            if i != j and tube2[1] < 6:
                edge_cost = 1
                if tube1[0] != tube2[0]:
                    edge_cost = 2
                graph.setdefault(i, []).append((j, edge_cost))
                graph.setdefault(j, []).append((i, edge_cost))
    start = tuple(tubes.index(tube) for tube in tubes if tube[0] == 'Green' and tube[1] == 4)
    end = tuple(i for i, tube in enumerate(tubes) if tube[1] == 6)
    cost, path = shortest_path(graph, start, end)
    return [(path[i], path[i+1]) for i in range(0, len(path), 2)]

tubes = [('Green', 4), ('Blue', 4), ('Red', 4)]
print(sort_it(tubes))
