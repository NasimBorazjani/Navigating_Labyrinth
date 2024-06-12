
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
            if i != j:
                color1, count1 = tube1[-1], len(tube1)
                color2, count2 = tube2[-1], len(tube2)
                if count1 < 7 and count2 < 7 and color1 != color2:
                    edge_cost = 1
                    if (color1, count1) not in graph:
                        graph[(color1, count1)] = []
                    if (color2, count2) not in graph:
                        graph[(color2, count2)] = []
                    graph[(color1, count1)].append(((color2, count2), edge_cost))
                    graph[(color2, count2)].append(((color1, count1), edge_cost))
    start = (tubes[0][-1], len(tubes[0]))
    end = ('Blue', 4)
    cost, path = shortest_path(graph, start, end)
    return [(path[i], path[i+1]) for i in range(len(path)-1)]

tubes = [['Blue', 'Green', 'Green', 'Blue'], ['Red', 'Blue', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Blue']]
print(sort_it(tubes))
