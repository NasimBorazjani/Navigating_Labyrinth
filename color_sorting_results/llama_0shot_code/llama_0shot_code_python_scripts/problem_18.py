
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
    graph = []
    for i, tube1 in enumerate(tubes):
        node1 = (tube1[0], len(tube1))
        graph.append([])
        for j, tube2 in enumerate(tubes):
            if i != j:
                node2 = (tube2[0], len(tube2))
                if node1[1] > 0 and node2[1] < 6:
                    graph[i].append((j, 1))
    start = (tubes[0][0], len(tubes[0]))
    end = (tubes[1][0], len(tubes[1]))
    cost, path = shortest_path(graph, start, end)
    return [(path[i], path[i+1]) for i in range(len(path)-1)]

tubes = [['Green', 'Green', 'Red', 'Blue'], ['Red', 'Red', 'Blue', 'Green'], ['Red', 'Green', 'Blue', 'Blue']]
print(sort_it(tubes))
