
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
                source, dest, color, count = move
                new_path = list(path)
                new_path.append((source, dest))
                queue.append((dest, new_path))
    return None

def sort_it(tubes):
    graph = create_graph(tubes)
    initial_state = tuple(sorted(graph.items()))
    final_state = ((0, {'Blue': 4}), (1, {'Green': 3, 'Red': 3}), (2, {'Blue': 2, 'Green': 2, 'Red': 1}))
    return bfs_shortest_path(graph, initial_state, final_state)

tubes = [['Blue', 'Green', 'Red', 'Red'], ['Red', 'Blue', 'Green', 'Red'], ['Blue', 'Blue', 'Green', 'Green']]
print(sort_it(tubes))
