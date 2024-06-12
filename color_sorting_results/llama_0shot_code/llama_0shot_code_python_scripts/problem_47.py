
import heapq
from collections import Counter

def create_graph(tubes):
    graph = {}
    for i, tube1 in enumerate(tubes):
        graph[i] = {}
        for j, tube2 in enumerate(tubes):
            if i != j:
                counter1 = Counter(tube1)
                counter2 = Counter(tube2)
                most_common1 = counter1.most_common(1)[0][0]
                most_common2 = counter2.most_common(1)[0][0]
                least_common1 = counter1.most_common()[-1][0]
                least_common2 = counter2.most_common()[-1][0]
                moves = abs(counter1[most_common1] - counter2[most_common2])
                graph[i][j] = moves
    return graph

def shortest_path(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    while queue:
        moves, node, path = heapq.heappop(queue)
        if node not in seen:
            seen.add(node)
            path = path + [node]
            if node == end:
                return path
            for next_node, edge_moves in graph[node].items():
                if next_node not in seen:
                    heapq.heappush(queue, (moves + edge_moves, next_node, path))
    return None

def sort_it(tubes):
    graph = create_graph(tubes)
    start = tuple(sorted(tubes, key=lambda tube: Counter(tube).most_common(1)[0][0]))
    end = tuple([i] * 4 for i in range(3))
    path = shortest_path(graph, start, end)
    return [(path[i], path[i + 1]) for i in range(0, len(path), 2)]

tubes = [['Blue', 'Red', 'Green', 'Green'], ['Green', 'Blue', 'Red', 'Blue'], ['Red', 'Green', 'Blue', 'Red']]
print(sort_it(tubes))
