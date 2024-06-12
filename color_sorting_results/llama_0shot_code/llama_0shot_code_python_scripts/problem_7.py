
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
                return cost, path
            for c, neighbour in graph[node]:
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
                moves = sum((counts[ball] - other_counts[ball]) for ball in counts if ball not in other_counts or other_counts[ball] < counts[ball])
                graph[i].append((moves, j))
    start = tuple(tubes.index(tube) for tube in tubes)
    end = tuple(range(len(tubes)))
    cost, path = shortest_path(graph, start, end)
    return [(path[i], path[i+1]) for i in range(0, len(path), 2)]

tubes = [['Red', 'Red', 'Blue', 'Green'], ['Blue', 'Red', 'Blue', 'Green'], ['Blue', 'Green', 'Red', 'Green']]
print(sort_it(tubes))
