
import heapq
from collections import defaultdict

def create_graph(tubes):
    graph = defaultdict(list)
    for i, tube1 in enumerate(tubes):
        for j, tube2 in enumerate(tubes):
            if i != j:
                weight = len(set(tube1.keys()) | set(tube2.keys()))
                graph[i].append((weight, j))
    return graph

def dijkstra(graph, start):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, current, path) = heapq.heappop(queue)
        if current not in visited:
            visited.add(current)
            path = path + [current]
            if len(visited) == len(graph):
                return (cost, path)
            for weight, neighbour in graph[current]:
                heapq.heappush(queue, (cost + weight, neighbour, path))
    return float("inf")

def sort_it(tubes):
    graph = create_graph(tubes)
    _, path = dijkstra(graph, 0)
    return [(path[i], path[i+1]) for i in range(len(path)-1)]

tubes = [{'Green': 2, 'Blue': 2}, {'Red': 3, 'Green': 1}, {'Green': 1, 'Blue': 2, 'Red': 1}]
print(sort_it(tubes))
