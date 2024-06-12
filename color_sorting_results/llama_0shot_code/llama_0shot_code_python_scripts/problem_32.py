
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
                for color, count in counts.items():
                    if color in other_counts and other_counts[color] < 7:
                        moves = count - (7 - other_counts[color])
                        graph[i].append((moves, j))
    start = 0
    end = len(tubes) - 1
    cost, path = shortest_path(graph, start, end)
    return [(path[i], path[i+1]) for i in range(len(path)-1)]

tubes = [['Green', 'Red', 'Blue', 'Green'], ['Blue', 'Blue', 'Red', 'Blue'], ['Red', 'Red', 'Green', 'Green']]
print(sort_it(tubes))
