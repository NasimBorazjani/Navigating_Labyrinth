
import heapq

def dijkstra(matrix, start, end):
    height = len(matrix)
    width = len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
    queue = [(matrix[start[0]][start[1]], start)]
    distances = {start: 0}
    previous_nodes = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node == end:
            break
        for direction in directions:
            next_node = (current_node[0] + direction[0], current_node[1] + direction[1])
            if 0 <= next_node[0] < height and 0 <= next_node[1] < width and matrix[next_node[0]][next_node[1]] != 'x':
                next_distance = current_distance + matrix[next_node[0]][next_node[1]]
                if next_node not in distances or next_distance < distances[next_node]:
                    distances[next_node] = next_distance
                    previous_nodes[next_node] = current_node
                    heapq.heappush(queue, (next_distance, next_node))

    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes.get(end)
    path.reverse()

    return path

matrix = [
    [4, 1, 20, 15, 9, 'x', 8, 6, 'x', 'x', 14, 'x'],
    [5, 11, 9, 12, 10, 4, 15, 18, 7, 'x', 'x', 13],
    [15, 9, 1, 'x', 18, 3, 1, 19, 'x', 'x', 17, 17],
    ['x', 17, 11, 10, 'x', 19, 8, 'x', 'x', 'x', 'x', 7],
    [5, 'x', 1, 'x', 14, 13, 4, 8, 5, 'x', 13, 14],
    [16, 6, 'x', 'x', 'x', 17, 'x', 15, 4, 'x', 'x', 15],
    ['x', 'x', 'x', 15, 'x', 19, 10, 'x', 16, 18, 11, 1],
    [6, 8, 'x', 'x', 5, 5, 'x', 3, 8, 9, 14],
    [10, 14, 'x', 'x', 'x', 'x', 'x', 'x', 6, 2, 'x', 'x'],
    [12, 'x', 'x', 6, 11, 4, 'x', 'x', 12, 'x', 4, 16],
    [4, 'x', 'x', 'x', 11, 'x', 'x', 18, 16, 'x', 10],
    ['x', 6, 'x', 'x', 11, 'x', 5, 13, 8, 1, 17, 9]
]

start = (2, 0)
end = (7, 8)

path = dijkstra(matrix, start, end)

print(path)
