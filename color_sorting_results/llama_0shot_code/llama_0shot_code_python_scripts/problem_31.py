
import collections

def shortest_path(graph, start, end):
    queue = collections.deque([(0, start, [])])
    seen = set()
    while queue:
        (cost, node, path) = queue.popleft()
        if node not in seen:
            seen.add(node)
            path = path + [node]
            if node == end:
                return cost, path
            for c, neighbour in graph[node]:
                queue.append((cost + c, neighbour, path))
    return float('inf')

def sort_it(tubes):
    colors = {'Red': 0, 'Green': 1, 'Blue': 2}
    tubes = [[(colors[ball], 1) for ball in tube] for tube in tubes]
    graph = [[] for _ in range(len(tubes))]
    for i, tube in enumerate(tubes):
        for j, (color, count) in enumerate(tube):
            for k, (_, count2) in enumerate(tubes):
                if i != k and color == colors[tubes[k][0][0]]:
                    graph[i].append((abs(count - count2), k))
    start = sum(tubes[0])
    end = sum((1, 1, 1))
    _, path = shortest_path(graph, start, end)
    return [(path[i], path[i+1]) for i in range(0, len(path), 2)]

tubes = [['Red', 'Red', 'Red', 'Green'], ['Blue', 'Green', 'Green', 'Blue'], ['Blue', 'Red', 'Green', 'Blue']]
print(sort_it(tubes))
