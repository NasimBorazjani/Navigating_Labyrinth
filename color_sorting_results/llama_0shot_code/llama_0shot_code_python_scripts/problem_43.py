
from collections import defaultdict
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
    graph = defaultdict(list)
    for i, tube1 in enumerate(tubes):
        for j, tube2 in enumerate(tubes):
            if i != j and tube1[0] != tube2[0] and tube1[1] < 7 and tube2[1] < 7:
                graph[tube1].append((1, tube2))
                graph[tube2].append((1, tube1))
    start = (tubes[0][0], 4)
    end = (tubes[0][0], 7)
    cost, path = shortest_path(graph, start, end)
    return [(path.index(tube1), path.index(tube2)) for tube1, tube2 in zip(path[::2], path[1::2])]

tubes = [('Green', 4), ('Red', 4), ('Blue', 4)]
print(sort_it(tubes))
