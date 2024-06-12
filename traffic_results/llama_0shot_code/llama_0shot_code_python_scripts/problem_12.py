
import heapq

def dijkstra(matrix, start, end):
    height = len(matrix)
    width = len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, Left, Down, Up
    district_ends = [(3,5), (4,4), (5,8)]

    def get_neighbors(pos):
        row, col = pos
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < height and 0 <= new_col < width and matrix[new_row][new_col] != 'x':
                yield (new_row, new_col), matrix[new_row][new_col]

    def heuristic(pos):
        row, col = pos
        return abs(row - end[0]) + abs(col - end[1])

    queue = [(0, start, [])]
    visited = set()
    while queue:
        cost, pos, path = heapq.heappop(queue)
        if pos not in visited:
            visited.add(pos)
            path = path + [pos]
            if pos == end:
                return path
            for neighbor, weight in get_neighbors(pos):
                if neighbor not in visited:
                    district_visited = any(neighbor[0] <= end[0] <= district_end[0] and neighbor[1] <= end[1] <= district_end[1] for district_end in district_ends)
                    if district_visited:
                        heapq.heappush(queue, (cost + weight + heuristic(neighbor), neighbor, path))
    return None

matrix = [
    [19, 'x', 17, 14, 3, 'x', 10, 5, 2],
    ['x', 'x', 1, 'x', 'x', 19, 7, 1],
    [16, 12, 'x', 3, 19, 2, 14, 1, 14],
    ['x', 1, 16, 'x', 'x', 12, 'x', 3],
    ['x', 'x', 7, 19, 10, 'x', 'x', 19],
    [5, 'x', 'x', 6, 14, 'x', 'x', 10, 12],
    ['x', 'x', 'x', 'x', 18, 'x', 15, 12],
    ['x', 'x', 16, 8, 'x', 3, 'x', 'x'],
    ['x', 'x', 'x', 16, 'x', 'x', 8, 14, 7]
]

start, end = (3, 1), (5, 8)
path = dijkstra(matrix, start, end)
print(path)
