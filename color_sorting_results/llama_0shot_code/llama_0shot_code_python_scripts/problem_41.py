
import heapq
from collections import Counter

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
    graph = {i: [] for i in range(len(tubes))}
    for i, tube1 in enumerate(tubes):
        counter1 = Counter(tube1)
        for j, tube2 in enumerate(tubes):
            if i != j:
                counter2 = Counter(tube2)
                moves = sum(abs(counter1[c] - counter2[c]) for c in set(counter1) | set(counter2))
                graph[i].append((j, moves))
    start = tuple(sorted(tubes, key=lambda x: Counter(x)))
    end = ((1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1))
    _, path = shortest_path(graph, start, end)
    return [(path[i], path[i+1]) for i in range(0, len(path), 2)]

tubes = [['Green', 'Blue', 'Red', 'Blue'], ['Red', 'Green', 'Blue', 'Green'], ['Red', 'Blue', 'Green', 'Red']]
print(calculate_moves(tubes))
