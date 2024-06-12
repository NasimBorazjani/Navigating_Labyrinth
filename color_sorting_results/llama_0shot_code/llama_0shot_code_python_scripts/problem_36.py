
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

def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [])])
    seen = set()
    while queue:
        path = queue.popleft()
        node = path[0]
        if node not in seen:
            seen.add(node)
            neighbours = possible_moves(graph, node)
            for neighbour in neighbours:
                if neighbour not in seen:
                    queue.append((neighbour, path[1] + [neighbour]))
                    if neighbour == goal:
                        return path[1] + [neighbour]
    return None

def sort_it(tubes):
    graph = create_graph(tubes)
    initial_state = tuple(sorted(graph.items()))
    goal_state = tuple(sorted({i: {'Blue': 4, 'Red': 4, 'Green': 4}}.items()))
    return bfs_shortest_path(graph, initial_state, goal_state)

tubes = [['Blue', 'Red', 'Red', 'Red'], ['Green', 'Blue', 'Green', 'Green'], ['Blue', 'Blue', 'Green', 'Red']]
print(sort_it(tubes))
