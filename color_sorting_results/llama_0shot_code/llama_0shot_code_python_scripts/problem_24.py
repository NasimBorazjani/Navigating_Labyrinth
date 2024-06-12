
import heapq

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
        for j, tube2 in enumerate(tubes):
            if i != j:
                moves = abs(tube1.get('Red', 0) - tube2.get('Red', 0))
                moves += abs(tube1.get('Blue', 0) - tube2.get('Blue', 0))
                moves += abs(tube1.get('Green', 0) - tube2.get('Green', 0))
                moves += 1  # For the initial move
                graph[i].append((j, moves))
    start = tuple(tubes.index(tube) for tube in tubes)
    end = (0, 1, 2)
    cost, path = shortest_path(graph, start, end)
    return [(path[i], path[i+1]) for i in range(0, len(path), 2)]

tubes = [{'Red': 2, 'Blue': 2, 'Green': 0}, {'Red': 3, 'Blue': 1, 'Green': 1}, {'Red': 1, 'Blue': 2, 'Green': 2}]
print(calculate_moves(tubes))
