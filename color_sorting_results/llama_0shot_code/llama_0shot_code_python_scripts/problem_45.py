
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
            if i != j and len(tube2) < 7:
                for color, count in tube1.items():
                    if color not in tube2 or tube2[color] < 4:
                        moves.append((i, j, color, count))
    return moves

def bfs(graph, moves):
    queue = deque([(0, (), {i: tube for i, tube in enumerate(graph)})])
    visited = set()
    while queue:
        cost, path, tubes = queue.popleft()
        if id(tubes) in visited:
            continue
        visited.add(id(tubes))
        if all(len(tube) == 1 for tube in tubes.values()):
            return cost, path
        for move in moves:
            i, j, color, count = move
            if count > 0 and tubes[i][color] > 0 and len(tubes[j]) < 7:
                new_tubes = {**tubes}
                new_tubes[i] = {**tubes[i]}
                new_tubes[j] = {**tubes[j]}
                new_tubes[i][color] -= count
                new_tubes[j][color] += count
                queue.append((cost + 1, path + ((i, j),), new_tubes))
    return None

def sort_it(tubes):
    graph = create_graph(tubes)
    moves = possible_moves(graph)
    cost, path = bfs(graph, moves)
    return path

tubes = [['Red', 'Green', 'Green', 'Green'], ['Blue', 'Red', 'Blue', 'Blue'], ['Green', 'Red', 'Red', 'Blue']]
print(sort_it(tubes))
