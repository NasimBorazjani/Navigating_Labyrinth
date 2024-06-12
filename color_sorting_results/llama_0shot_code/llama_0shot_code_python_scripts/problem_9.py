
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
                moves = abs(counter1[most_common1] - counter2[most_common2])
                graph[i].append((j, moves))
    start = tuple(sorted(tubes, key=lambda x: Counter(x).most_common(1)[0][0]))
    end = (('Green', 'Green', 'Green', 'Green', 'Blue', 'Blue'),
           ('Red', 'Red', 'Red', 'Red', 'Blue', 'Blue'),
           ('Blue', 'Blue', 'Blue', 'Blue', 'Red', 'Red'))
    return shortest_path(graph, start, end)

tubes = [['Green', 'Blue', 'Green', 'Red'], ['Red', 'Green', 'Blue', 'Red'], ['Blue', 'Red', 'Green', 'Blue']]
print(calculate_moves(tubes))
