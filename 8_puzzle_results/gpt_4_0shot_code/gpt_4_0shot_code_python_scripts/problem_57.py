
from heapq import heappop, heappush

def astar(start, goal):
    queue = [(0, start, [])]
    seen = set()
    while queue:
        (cost, node, path) = heappop(queue)
        if node in seen:
            continue
        seen.add(node)
        path = path + [node]
        if node == goal:
            return path
        for (next_node, c) in get_neighbors(node):
            heappush(queue, (cost + c, next_node, path))

def get_neighbors(node):
    neighbors = []
    i, j = node.index('_'), node[0].index('_')
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        x, y = i + dx, j + dy
        if 0 <= x < len(node) and 0 <= y < len(node[0]):
            new_node = [row[:] for row in node]
            new_node[i][j], new_node[x][y] = new_node[x][y], new_node[i][j]
            neighbors.append((new_node, 1))
    return neighbors

start = [[71, 42, 22, 90], [79, 78, '_', 68], [25, 58, 28, 12]]
goal = [[90, 79, 78, 71], [68, 58, 42, 25], [22, 12, 28, '_']]
path = astar(start, goal)
for node in path:
    print(node)
