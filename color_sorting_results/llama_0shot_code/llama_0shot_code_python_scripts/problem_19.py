
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
                if next_node not in seen:
                    heapq.heappush(queue, (cost + edge_cost, next_node, path))
    return float("inf")

def calculate_weight(src_tube, dest_tube):
    weight = 0
    for color in set(src_tube.keys()) | set(dest_tube.keys()):
        weight += abs(src_tube.get(color, 0) - dest_tube.get(color, 0))
    return weight

def sort_it(tubes):
    graph = defaultdict(list)
    for i, src_tube in enumerate(tubes):
        src_tube = dict(Counter(src_tube))
        for j, dest_tube in enumerate(tubes):
            if i != j:
                dest_tube = dict(Counter(dest_tube))
                weight = calculate_weight(src_tube, dest_tube)
                graph[i].append((j, weight))
    start = tuple(sorted((Counter(tube) for tube in tubes), key=str))
    end = (defaultdict(int), defaultdict(int), defaultdict(int))
    shortest_path_length, path = shortest_path(graph, start, tuple(sorted((Counter(tube) for tube in tubes), key=str)))
    return [(path[i], path[i+1]) for i in range(len(path)-1)]

from collections import Counter
print(sort_it([['Blue', 'Green', 'Green', 'Red'], ['Red', 'Blue', 'Green', 'Red'], ['Blue', 'Red', 'Green', 'Blue']]))
