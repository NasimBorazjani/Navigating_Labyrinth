
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
                most_common1 = counter1.most_common(1)[0][0]
                most_common2 = counter2.most_common(1)[0][0]
                least_common1 = counter1.most_common()[-1][0]
                least_common2 = counter2.most_common()[-1][0]
                edge_cost = abs(counter1[most_common1] - counter2[most_common2])
                if counter1[least_common1] < 7 and counter2[least_common2] < 7:
                    graph[i].append((j, edge_cost))
    return shortest_path(graph, tuple(sorted(tubes)), tuple(sorted([most_common] * 4 for most_common in sorted(counter.most_common()))))

tubes = [['Blue', 'Green', 'Blue', 'Red'], ['Red', 'Green', 'Blue', 'Red'], ['Green', 'Red', 'Green', 'Blue']]
print(calculate_moves(tubes))
