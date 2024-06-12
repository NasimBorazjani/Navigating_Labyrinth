
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

def sort_it(tubes):
    graph = {}
    for i, tube1 in enumerate(tubes):
        graph[i] = []
        for j, tube2 in enumerate(tubes):
            if i != j:
                moves = get_moves(tube1, tube2)
                graph[i].append((j, moves))
    start = tuple(sorted(tubes))
    end = (0, 1, 2, 3, 4, 5)
    _, path = shortest_path(graph, start, end)
    return [(path[i], path[i+1]) for i in range(0, len(path), 2)]

def get_moves(tube1, tube2):
    moves = 0
    for color in tube1:
        if color in tube2:
            moves += tube1[color] - tube2[color]
    return moves

tubes = [{'Red': 2, 'Blue': 2}, {'Red': 1, 'Blue': 1, 'Green': 1}, {'Green': 3, 'Blue': 1}]
print(sort_it(tubes))
