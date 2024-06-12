
import heapq

def dijkstra(matrix, start, end, district_rows):
    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    heap = [(matrix[start[0]][start[1]], start)]  # (cost, position)
    visited = set()
    path = {end: None}

    while heap:
        cost, position = heapq.heappop(heap)
        if position in visited:
            continue
        visited.add(position)

        if position == start:
            district_visited = {(position[0] // district_rows[0], position[1] // district_rows[1]): 1}
        else:
            district_visited = {(position[0] // district_rows[0], position[1] // district_rows[1]): 1}

        for direction in directions:
            next_position = (position[0] + direction[0], position[1] + direction[1])
            if (0 <= next_position[0] < m) and (0 <= next_position[1] < n) and matrix[next_position[0]][next_position[1]] != 'x' and next_position not in visited:
                new_cost = cost + matrix[next_position[0]][next_position[1]]
                if next_position not in path or new_cost < path[next_position]:
                    path[next_position] = position
                    heapq.heappush(heap, (new_cost, next_position))

    if end not in path:
        return None

    position = end
    route = []
    while position is not None:
        route.append(position)
        position = path[position]
    route.reverse()

    return route

matrix = [
    [18, 19, 9, 'x', 'x', 'x', 3, 'x', 8, 'x'],
    [13, 2, 3, 15, 3, 'x', 8, 9, 'x', 'x'],
    ['x', 6, 18, 1, 20, 7, 16, 8, 1, 19],
    ['x', 'x', 'x', 20, 14, 'x', 19, 11, 9, 6],
    [2, 'x', 'x', 6, 5, 6, 7, 'x', 8],
    [17, 9, 5, 3, 3, 'x', 16, 18, 'x', 8],
    [10, 'x', 14, 16, 'x', 8, 'x', 9, 'x', 13],
    ['x', 17, 8, 11, 12, 'x', 4, 8, 'x', 7],
    ['x', 'x', 6, 'x', 'x', 'x', 'x', 13, 'x', 8],
    [9, 'x', 'x', 'x', 3, 10, 'x', 3, 10, 1]
]

start, end = (5, 1), (3, 9)
district_rows = (4, 3)
route = dijkstra(matrix, start, end, district_rows)
print(route)
