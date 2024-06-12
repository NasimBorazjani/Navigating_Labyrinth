
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

def sort_it(tubes):
    graph = defaultdict(list)
    for i, tube1 in enumerate(tubes):
        for j, tube2 in enumerate(tubes):
            if i != j:
                cost = sum(min(tube2.get(color, 0), 6 - tube2.get(color, 0)) for color in tube1)
                graph[i].append((j, cost))
    start = tuple(tubes)
    end = ({color: 6 for color in set(sum(tubes, []))},)
    cost, path = shortest_path(graph, start, end)
    return [(path[i], path[i+1]) for i in range(len(path)-1)]

tubes = [{'Green': 3, 'Blue': 1}, {'Red': 2, 'Green': 1, 'Blue': 1}, {'Red': 2, 'Green': 1, 'Blue': 1}]
print(sort_it(tubes))
