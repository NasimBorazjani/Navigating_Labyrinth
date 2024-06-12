
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # north, south, east, west

    # Create a graph from the matrix
    graph = {(i, j): [] for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)].append((matrix[ni][nj], (ni, nj)))

    # Dijkstra's algorithm
    queue = [(matrix[start[0]][start[1]], start, [])]
    visited = set()
    while queue:
        dist, pos, path = heapq.heappop(queue)
        if pos not in visited:
            visited.add(pos)
            path = path + [pos]
            if pos == end:
                return path[::-1]  # shortest path from start to end

            for d, next_pos in graph[pos]:
                heapq.heappush(queue, (dist + d, next_pos, path))

    return None  # no path from start to end

def solve(matrix):
    start, end = (3, 8), (6, 0)
    path = dijkstra(matrix, start, end)

    # Ensure that the path visits at least one workshop in each district
    districts = [
        [(i, j) for j in range(10) if matrix[i][j] != 'x'],
        [(i, j) for j in range(10) if matrix[i][j] != 'x'],
        [(i, j) for j in range(10) if matrix[i][j] != 'x']
    ]
    district_paths = [list(filter(lambda p: p in district, path)) for district in districts]
    missing_districts = [i for i, district_path in enumerate(district_paths) if not district_path]
    for i in missing_districts:
        # Add the nearest workshop from the missing district to the path
        district = districts[i]
        distances = {workshop: min(matrix[workshop[0]][workshop[1]] for workshop in path) for workshop in district}
        nearest_workshop = min(distances, key=distances.get)
        path.append(nearest_workshop)

    return path[::-1]  # reverse the path to start from the start workshop

matrix = [
    [19, 'x', 'x', 'x', 13, 'x', 12, 'x'],
    ['x', 'x', 8, 'x', 15, 18, 11, 12, 'x', 7],
    ['x', 8, 'x', 'x', 15, 20, 17, 12, 2, 8],
    ['x', 'x', 4, 13, 2, 14, 19, 13, 15, 19],
    [13, 2, 'x', 'x', 8, 'x', 'x', 12],
    [2, 20, 20, 14, 'x', 'x', 15, 'x', 2, 19],
    [15, 16, 18, 'x', 2, 'x', 'x', 'x', 'x'],
    [2, 'x', 17, 'x', 12, 'x', 'x', 3, 'x'],
    [2, 'x', 10, 6, 'x', 'x', 9, 8, 19],
    [17, 'x', 6, 13, 'x', 18, 'x', 'x', 18]
]

print(solve(matrix))
