
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
    graph = {}
    for i, tube1 in enumerate(tubes):
        graph[i] = []
        counter1 = Counter(tube1)
        for j, tube2 in enumerate(tubes):
            if i != j:
                counter2 = Counter(tube2)
                moves = sum(abs(counter1[color] - counter2[color]) for color in counter1.keys() & counter2.keys())
                graph[i].append((j, moves))
    start = tuple(sorted(tubes, key=lambda tube: Counter(tube).most_common(1)[0][0]))
    end = (0, 1, 2, 3)
    _, path = shortest_path(graph, start, end)
    return [(path[i], path[i+1]) for i in range(len(path)-1)]

tubes = [['Blue', 'Green', 'Green', 'Red'], ['Red', 'Red', 'Green', 'Blue'], ['Green', 'Blue', 'Blue', 'Red']]
print(calculate_moves(tubes))
