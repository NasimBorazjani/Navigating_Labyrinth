
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
                if neighbour not in seen:
                    heapq.heappush(queue, (cost + c, neighbour, path))
    return float("inf")

def sort_it(tubes):
    graph = {}
    for i, tube in enumerate(tubes):
        graph[i] = []
        for j, tube2 in enumerate(tubes):
            if i != j:
                for color in set(tube):
                    count_color = tube.count(color)
                    count_color_tube2 = tube2.count(color)
                    if count_color_tube2 < 6 - len(tube2):
                        graph[i].append((abs(count_color - count_color_tube2), j))
    cost, path = shortest_path(graph, 0, len(tubes) - 1)
    return [(path[i], path[i + 1]) for i in range(len(path) - 1)]

tubes = [['Red', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Red', 'Green'], ['Green', 'Blue', 'Red', 'Red']]
print(sort_it(tubes))
