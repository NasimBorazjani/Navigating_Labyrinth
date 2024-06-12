
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # north, south, east, west
    dist = {(i, j): float('inf') for i in range(rows) for j in range(cols)}
    dist[start] = 0
    visited = set()
    path = {end: None}

    def in_bounds(i, j):
        return 0 <= i < rows and 0 <= j < cols

    def get_district(i, j):
        if i <= 1:
            return 1
        elif 2 <= i <= 6:
            return 2
        else:
            return 3

    def district_penalty(u, v):
        return 0 if get_district(u[0], u[1]) == get_district(v[0], v[1]) else 1000

    heap = [(0, start)]
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_node not in visited:
            visited.add(current_node)
            if current_node == end:
                while path[current_node] is not None:
                    current_node = path[current_node]
                    if get_district(current_node[0], current_node[1]) != get_district(end[0], end[1]):
                        return False
                    end = current_node
                return [(i, j) for i, j in reversed([end] + [path[i] for i in path if path[i] is not None])]
            for direction in directions:
                next_i, next_j = current_node[0] + direction[0], current_node[1] + direction[1]
                if in_bounds(next_i, next_j) and matrix[next_i][next_j] != 'x' and (next_i, next_j) not in visited:
                    new_dist = current_dist + matrix[next_i][next_j] + district_penalty(current_node, (next_i, next_j))
                    if new_dist < dist[(next_i, next_j)]:
                        dist[(next_i, next_j)] = new_dist
                        path[(next_i, next_j)] = current_node
                        heapq.heappush(heap, (new_dist, (next_i, next_j)))
    return False

matrix = [
    [15, 4, 9, 10, 19, 'x', 12, 4, 'x', 15],
    [12, 19, 11, 'x', 'x', 'x', 'x', 7, 6, 3],
    [4, 'x', 8, 'x', 'x', 19, 'x', 11, 1, 6],
    ['x', 'x', 5, 'x', 'x', 'x', 12, 6, 'x'],
    ['x', 14, 'x', 'x', 14, 11, 2, 9, 6, 14],
    [8, 8, 5, 17, 7, 'x', 1, 2, 'x', 6],
    [18, 'x', 'x', 15, 'x', 15, 4, 'x', 7],
    [19, 'x', 10, 18, 14, 'x', 14, 9, 8, 6],
    [19, 'x', 14, 'x', 10, 8, 15, 'x', 15, 'x'],
    [12, 1, 5, 3, 3, 'x', 'x', 'x', 'x']
]

start, end = (1, 9), (6, 3)
print(dijkstra(matrix, start, end))
