
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
    for i in graph:
        for j in graph:
            if i != j:
                for color in graph[i]:
                    if color in graph[j]:
                        moves.append((i, j, color, graph[j][color]))
    return moves

def bfs(graph, moves, start, end):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node not in visited:
            visited.add(node)
            if node == end:
                return path
            for move in moves:
                if move[0] == node:
                    queue.append((move[1], path + [(move[0], move[1])]))
    return None

def sort_it(tubes):
    graph = create_graph(tubes)
    moves = possible_moves(graph)
    start = list(graph.keys())[0]
    end = list(graph.keys())[-1]
    path = bfs(graph, moves, start, end)
    return path

tubes = [['Green', 'Red', 'Red', 'Green'], ['Blue', 'Red', 'Green', 'Blue'], ['Green', 'Blue', 'Blue', 'Red']]
print(sort_it(tubes))
