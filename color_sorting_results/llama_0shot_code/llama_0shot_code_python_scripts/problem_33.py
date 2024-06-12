
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

def possible_moves(graph):
    moves = []
    for i, tube1 in enumerate(graph):
        for j, tube2 in enumerate(graph):
            if i != j:
                for color, count in tube1.items():
                    if color not in tube2 or tube2[color] < 7:
                        moves.append((i, j, color))
    return moves

def bfs(graph, initial, final):
    queue = deque([[initial]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == final:
            return path
        for move in possible_moves(graph):
            if move[0] == node:
                new_path = list(path)
                new_path.append(move[1])
                queue.append(new_path)

def solve_sort_it(tubes):
    graph = create_graph(tubes)
    initial = tuple(sorted(graph.items()))
    final = ((0, {'Green': 4}), (1, {'Red': 2, 'Blue': 2}), (2, {'Red': 2, 'Blue': 2}))
    path = bfs(graph, initial, final)
    return [(path[i], path[i+1]) for i in range(len(path)-1)]

tubes = [['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Blue', 'Blue'], ['Red', 'Blue', 'Blue', 'Red']]
print(solve_sort_it(tubes))
