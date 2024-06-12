
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
    queue = deque([(source, [])])
    visited = set([source])
    while queue:
        path = queue.popleft()
        node = path[0]
        if node == destination:
            return path[1]
        for move in possible_moves(graph, node):
            if move[1] not in visited:
                visited.add(move[1])
                queue.append((move[1], path + [move]))

def sort_it(tubes):
    graph = create_graph(tubes)
    moves = []
    for i in range(len(tubes)):
        path = bfs_shortest_path(graph, i, len(tubes))
        if path:
            moves.extend(path)
    return moves

tubes = [['Red', 'Red', 'Green', 'Blue'], ['Green', 'Green', 'Red', 'Green'], ['Blue', 'Blue', 'Red', 'Blue']]
print(sort_it(tubes))
