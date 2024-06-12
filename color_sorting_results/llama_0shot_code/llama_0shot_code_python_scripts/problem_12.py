
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
    final_state = ((0, {'Blue': 4}), (1, {'Green': 3, 'Red': 1}), (2, {'Blue': 2, 'Green': 1, 'Red': 2}))
    return bfs_shortest_path(graph, initial_state, final_state)

tubes = [['Blue', 'Blue', 'Red', 'Blue'], ['Red', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Blue', 'Green']]
print(sort_it(tubes))
