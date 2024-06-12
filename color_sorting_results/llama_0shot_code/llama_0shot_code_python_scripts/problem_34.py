
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
    source_content = graph[source]
    for dest, dest_content in graph.items():
        if dest != source:
            for color, count in source_content.items():
                if color in dest_content:
                    moves.append((source, dest, color, count))
                else:
                    moves.append((source, dest, color, count))
    return moves

def bfs_shortest_path(graph, initial, final):
    queue = deque([(initial, [])])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[0]
        if node not in visited:
            visited.add(node)
            if node == final:
                return path[1]
            for move in possible_moves(graph, node):
                queue.append((move, path[1] + [move]))
    return None

def sort_it(tubes):
    graph = create_graph(tubes)
    initial_state = tuple(sorted(graph.items()))
    final_state = ((0, {'Blue': 3, 'Green': 3, 'Red': 3}), (1, {}), (2, {}))
    shortest_path = bfs_shortest_path(graph, initial_state, final_state)
    return shortest_path

tubes = [['Red', 'Green', 'Blue', 'Blue'], ['Blue', 'Red', 'Green', 'Red'], ['Green', 'Blue', 'Red', 'Green']]
print(sort_it(tubes))
