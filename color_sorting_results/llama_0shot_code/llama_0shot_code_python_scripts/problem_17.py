
import heapq
from collections import defaultdict

def shortest_path(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in seen:
            seen.add(node)
            path = path + [node]
            if node == end:
                return (cost, path)
            for (next_node, edge_cost) in graph[node]:
                heapq.heappush(queue, (cost + edge_cost, next_node, path))
    return float("inf")

def calculate_moves(tubes):
    colors = set(sum((list(tube.keys()) for tube in tubes), []))
    graph = defaultdict(list)
    for i, tube1 in enumerate(tubes):
        for j, tube2 in enumerate(tubes):
            if i != j:
                moves = sum(min(tube1.get(color, 0), tube2.get(color, 6) - tube2.get(color, 0)) for color in colors) + 1
                graph[i].append((j, moves))
                graph[j].append((i, moves))
    start = tuple(tubes)
    end = tuple((color, 6) for color in colors)
    _, path = shortest_path(graph, start, end)
    return [(path[i], path[i+1]) for i in range(0, len(path), 2)]

tubes = [{'Blue': 2, 'Red': 2}, {'Green': 3, 'Red': 1}, {'Blue': 2, 'Green': 1, 'Red': 1}]
print(calculate_moves(tubes))
