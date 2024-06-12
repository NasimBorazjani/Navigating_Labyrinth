
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

def possible_moves(graph):
    moves = []
    for i, tube1 in enumerate(graph):
        for j, tube2 in enumerate(graph):
            if i != j:
                for color, count in graph[j].items():
                    if color in graph[i] and graph[i][color] < 4 and graph[i][color] + count <= 4:
                        moves.append((i, j, color, min(4 - graph[i][color], count)))
    return moves

def bfs(graph, moves):
    queue = deque([(0, (), {i: i for i in graph})])
    visited = set()
    while queue:
        cost, path, mapping = queue.popleft()
        if mapping not in visited:
            visited.add(mapping)
            if all(len(graph[i]) == 1 for i in graph):
                return cost, path
            for move in moves:
                i, j, color, count = move
                if graph[i][color] >= count and all(graph[j][c] <= 4 for c in graph[j]):
                    new_graph = {i: {c: count for c, count in graph[i].items() if c != color},
                                 j: {c: graph[j].get(c, 0) + count for c in graph[j]}}
                    new_graph[i][color] -= count
                    new_mapping = {i: i for i in new_graph}
                    queue.append((cost + count, path + ((i, j),), new_mapping))
    return None

def sort_it(tubes):
    graph = create_graph(tubes)
    moves = possible_moves(graph)
    cost, path = bfs(graph, moves)
    return path

tubes = [['Red', 'Red', 'Blue', 'Green'], ['Blue', 'Green', 'Blue', 'Blue'], ['Red', 'Green', 'Green', 'Red']]
print(sort_it(tubes))
