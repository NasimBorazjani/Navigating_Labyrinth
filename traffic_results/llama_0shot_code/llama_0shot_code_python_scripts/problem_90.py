
import heapq

def dijkstra(matrix, start):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    # Make a heap with (distance, position)
    heap = [(matrix[start[0]][start[1]], start)]
    distances = {start: matrix[start[0]][start[1]]}
    paths = {start: []}

    while heap:
        (dist, pos) = heapq.heappop(heap)
        if pos == (rows-1, cols-1):
            return dist, paths[pos]

        for direction in directions:
            next_row, next_col = pos[0] + direction[0], pos[1] + direction[1]
            if 0 <= next_row < rows and 0 <= next_col < cols and matrix[next_row][next_col] != 'x':
                new_dist = dist + matrix[next_row][next_col]
                new_pos = (next_row, next_col)
                if new_pos not in distances or new_dist < distances[new_pos]:
                    distances[new_pos] = new_dist
                    paths[new_pos] = paths[pos] + [new_pos]
                    heapq.heappush(heap, (new_dist, new_pos))

    return float('inf')  # If there is no path

def solve(matrix):
    start, end = (6, 0), (4, 13)
    matrix[start[0]][start[1]] = 0
    matrix[end[0]][end[1]] = 0
    districts = [(0, 4), (5, 6), (7, 13)]
    min_district_distances = [min(matrix[r[0]:r[1]+1], key=lambda row: min(row[c[0]:c[1]+1] for c in districts if c[0]<=r[0]<c[1])) for r in districts]
    min_district_positions = [(matrix.index(row), row.index(min_dist)) for min_dist, row in zip(min_district_distances, min_district_distances)]
    min_district_positions.append(start)
    min_district_positions.append(end)
    matrix[start[0]][start[1]] = 1
    matrix[end[0]][end[1]] = 1
    _, path = dijkstra(matrix, start)
    return path

matrix = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 15, 'x', 'x', 19, 1],
          ['x', 12, 'x', 19, 'x', 13, 'x', 14, 13, 8, 'x', 1, 6],
          ['x', 17, 'x', 19, 5, 4, 'x', 'x', 12, 'x', 'x', 10, 14, 'x'],
          ['x', 18, 'x', 1, 14, 'x', 12, 11, 4, 4, 7],
          [2, 15, 'x', 'x', 'x', 14, 'x', 16, 5, 2, 4, 'x', 10, 2],
          [8, 2, 15, 18, 19, 6, 13, 7, 6, 'x', 'x', 'x', 1, 'x'],
          [5, 'x', 11, 2, 8, 8, 'x', 1, 10, 8, 13, 7, 12, 18],
          ['x', 18, 8, 19, 'x', 'x', 16, 11, 'x', 9, 'x', 9, 8],
          [4, 10, 'x', 12, 12, 13, 13, 2, 13, 'x', 'x', 'x', 8, 18],
          [1, 'x', 'x', 'x', 5, 12, 18, 16, 5, 17, 'x', 16, 11, 18],
          [19, 'x', 'x', 'x', 'x', 1, 'x', 'x', 'x', 10, 19, 'x', 'x'],
          ['x', 14, 'x', 'x', 'x', 15, 16, 9, 'x', 'x', 'x', 'x', 'x'],
          [6, 'x', 16, 18, 6, 'x', 18, 5, 'x', 'x', 'x', 6, 1]]

print(solve(matrix))
