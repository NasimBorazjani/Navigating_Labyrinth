
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
            for c, neighbour in graph[node]:
                if neighbour not in seen:
                    heapq.heappush(queue, (cost + c, neighbour, path))
    return float("inf")

def sort_it(tubes):
    graph = {}
    for i, tube in enumerate(tubes):
        graph[i] = []
        counts = {}
        for ball in tube:
            if ball not in counts:
                counts[ball] = 0
            counts[ball] += 1
        for j, other_tube in enumerate(tubes):
            if i != j:
                other_counts = {}
                for ball in other_tube:
                    if ball not in other_counts:
                        other_counts[ball] = 0
                    other_counts[ball] += 1
                moves = sum([min(counts[color], 7 - other_counts[color]) for color in counts])
                graph[i].append((moves, j))
    initial_state = tuple(sorted(tubes))
    final_state = tuple([i for i in range(7)])
    _, moves = shortest_path(graph, initial_state, final_state)
    return [(moves[i], moves[i+1]) for i in range(0, len(moves), 2)]

tubes = [['Red', 'Red', 'Blue', 'Blue'], ['Red', 'Green', 'Green', 'Green'], ['Red', 'Blue', 'Blue', 'Green']]
print(sort_it(tubes))
