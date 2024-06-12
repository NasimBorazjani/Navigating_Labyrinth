
from collections import deque

def bfs(graph, start, end):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node not in visited:
            visited.add(node)
            if node == end:
                return path
            for neighbour in graph[node]:
                queue.append((neighbour, path + [(node, neighbour)]))

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
                    if color in other_counts and other_counts[color] < 7 and count > 0:
                        graph[i].append(j)
    start = tuple(sorted(tubes))
    end = ((4, 'Blue'), (3, 'Red'), (3, 'Green'))
    return bfs(graph, start, end)

tubes = [['Blue', 'Red', 'Red', 'Blue'], ['Green', 'Red', 'Red', 'Green'], ['Blue', 'Blue', 'Green', 'Green']]
print(sort_it(tubes))
