
from collections import deque

def create_graph(tubes):
    graph = {}
    for i, tube in enumerate(tubes):
        color_count = {}
        for color in tube:
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1
        graph[i] = color_count
    return graph

def possible_moves(graph, source):
    moves = []
    source_color_count = graph[source]
    for dest, dest_color_count in graph.items():
        if source != dest:
            for color, count in source_color_count.items():
                if color in dest_color_count:
                    moves.append((source, dest, color, count - dest_color_count[color]))
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
    parent_nodes = bfs_shortest_path(graph, 0, len(tubes) - 1)
    return [(parent_nodes[i], parent_nodes[i + 1]) for i in range(len(parent_nodes) - 1)]

tubes = [['Red', 'Blue', 'Green', 'Green'], ['Blue', 'Red', 'Green', 'Blue'], ['Green', 'Blue', 'Red', 'Red']]
print(sort_it(tubes))
