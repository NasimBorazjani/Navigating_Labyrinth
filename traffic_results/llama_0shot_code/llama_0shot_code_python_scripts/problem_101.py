
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    heap = [(matrix[start[0]][start[1]], start)]
    distances = {(i, j): float('inf') for i in range(rows) for j in range(cols)}
    distances[start] = matrix[start[0]][start[1]]
    parents = {(i, j): None for i in range(rows) for j in range(cols)}
    districts = {(i, j): (i // 5) + 1 for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    visited_districts = set()

    while heap:
        dist, position = heapq.heappop(heap)
        if position == end:
            break
        if distances[position] < dist:
            continue
        for direction in directions:
            next_position = (position[0] + direction[0], position[1] + direction[1])
            if 0 <= next_position[0] < rows and 0 <= next_position[1] < cols and matrix[next_position[0]][next_position[1]] != 'x':
                next_dist = dist + matrix[next_position[0]][next_position[1]]
                if next_dist < distances[next_position]:
                    distances[next_position] = next_dist
                    parents[next_position] = position
                    heapq.heappush(heap, (next_dist, next_position))
                    district = districts[next_position]
                    if district not in visited_districts:
                        visited_districts.add(district)

    path = []
    while end is not None:
        path.append(end)
        end = parents[end]
    path.reverse()

    if len(visited_districts) != 3:
        for district in range(1, 4):
            if district not in visited_districts:
                for position in sorted(districts.items(), key=lambda x: x[1] == district and -distances[x[0]]):
                    if position[1] == district:
                        path.insert(1, position[0])
                        break
                break
    return path

matrix = [
    ['x', 3, 1, 19, 8, 1, 4, 18, 15, 17, 4, 3, 'x', 3, 'x'],
    ['x', 11, 'x', 'x', 'x', 12, 'x', 19, 15, 4, 'x', 'x', 'x', 'x', 'x'],
    [4, 1, 'x', 8, 'x', 12, 17, 'x', 14, 4, 9, 11, 13, 6, 19],
    [2, 'x', 6, 14, 15, 'x', 18, 9, 'x', 10, 10, 'x', 'x', 1, 'x'],
    ['x', 11, 'x', 8, 'x', 5, 'x', 8, 7, 6, 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 17, 'x', 13, 'x', 'x', 'x', 18, 19, 5, 'x', 'x'],
    ['x', 12, 18, 'x', 'x', 'x', 19, 'x', 12, 'x', 11, 7, 19, 12, 'x'],
    [6, 6, 'x', 6, 4, 18, 'x', 15, 18, 'x', 6, 8, 'x'],
    [10, 10, 'x', 'x', 6, 4, 11, 19, 'x', 9, 'x', 2, 'x', 3, 14],
    ['x', 18, 14, 10, 'x', 1, 6, 'x', 15, 'x', 6, 'x', 14, 'x'],
    ['x', 'x', 7, 10, 'x', 2, 'x', 7, 14, 4, 11, 'x', 'x', 'x'],
    [12, 'x', 6, 'x', 8, 5, 6, 6, 8, 'x', 'x', 'x', 'x', 4, 7],
    ['x', 'x', 1, 8, 10, 4, 10, 17, 19, 11, 2, 'x', 'x', 16],
    ['x', 'x', 7, 10, 'x', 2, 'x', 7, 14, 4, 11, 'x', 'x', 'x']
]

start = (7, 0)
end = (4, 13)

path = dijkstra(matrix, start, end)
print(path)
