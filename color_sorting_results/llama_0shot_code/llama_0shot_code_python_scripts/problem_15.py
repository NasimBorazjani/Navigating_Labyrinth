
from collections import deque

def create_graph(tubes):
    graph = {}
    for i, tube in enumerate(tubes):
        content = {}
        for ball in tube:
            if ball in content:
                content[ball] += 1
            else:
                content[ball] = 1
        graph[i] = content
    return graph

def possible_moves(graph, source):
    moves = []
    for dest, content in graph.items():
        if dest != source:
            for color, count in content.items():
                if color in graph[source] and count < 6:
                    moves.append((source, dest, color))
    return moves

def bfs_shortest_path(graph, source, destination):
    queue = deque([(source, [source])])
    visited = set([source])
    while queue:
        vertex, path = queue.popleft()
        for move in possible_moves(graph, vertex):
            if move[1] not in visited:
                visited.add(move[1])
                queue.append((move[1], path + [move[1]]))
                if move[1] == destination:
                    return path + [move[1]]
    return None

def sort_it(tubes):
    graph = create_graph(tubes)
    source = list(graph.keys())[0]
    destination = {0: 1, 1: 2, 2: 0}
    path = bfs_shortest_path(graph, source, destination[source])
    return [(path[i], path[i+1]) for i in range(len(path)-1)]

tubes = [['Blue', 'Red', 'Red', 'Blue'], ['Green', 'Green', 'Red', 'Red'], ['Green', 'Green', 'Blue', 'Blue']]
print(sort_it(tubes))
