
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # north, south, west, east

    # Create a graph
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Use Dijkstra's algorithm to find the shortest path
    queue = [(matrix[start[0]][start[1]], start, {start})]
    shortest_times = {start: (0, None)}
    while queue:
        time, current, visited = heapq.heappop(queue)
        if current == end:
            break
        for neighbor, t in graph[current].items():
            if neighbor not in visited:
                new_time = time + t
                if neighbor not in shortest_times or new_time < shortest_times[neighbor][0]:
                    shortest_times[neighbor] = (new_time, current)
                    heapq.heappush(queue, (new_time, neighbor, visited | {neighbor}))

    # Create the shortest path
    path = []
    while end is not None:
        path.append(end)
        end = shortest_times[end][1]
    path.reverse()

    # Check and fix the path
    districts = [set(range(0, 5)), set(range(5, 6)), set(range(6, 12))]
    district_counts = {i: 0 for i in range(3)}
    for i in range(1, len(path)):
        district_counts[path[i][0] // 5] += 1
    for d in range(3):
        if district_counts[d] == 0:
            for i in districts[d]:
                for j in range(cols):
                    if (i, j) in graph and graph[(i, j)] and (path[0][0] // 5 != d or i != path[0][0]):
                        path.insert(1, (i, j))
                        break
                break

    return path

matrix = [
    [5, 'x', 'x', 4, 'x', 7, 11, 8, 3, 19, 'x'],
    ['x', 'x', 6, 15, 16, 'x', 'x', 4, 'x', 7, 8, 19],
    [18, 'x', 'x', 15, 'x', 'x', 'x', 8, 4, 16, 7, 9],
    ['x', 19, 'x', 'x', 'x', 16, 'x', 17, 15, 'x', 9],
    [15, 8, 19, 'x', 4, 4, 'x', 'x', 'x', 3, 3, 10],
    [18, 6, 14, 5, 'x', 18, 19, 15, 18, 19, 12, 5],
    [12, 'x', 2, 2, 6, 3, 3, 8, 3, 1, 15],
    [10, 4, 'x', 9, 15, 3, 'x', 7, 'x', 17, 'x', 'x'],
    [5, 18, 'x', 17, 'x', 17, 'x', 15, 'x', 18, 'x'],
    [4, 'x', 16, 11, 10, 3, 12, 'x', 11, 14, 3, 'x'],
    ['x', 9, 9, 14, 19, 15, 'x', 1, 10, 19, 6, 'x'],
    ['x', 'x', 17, 4, 'x', 2, 'x', 7, 'x', 4, 4, 18]
]

start = (4, 11)
end = (6, 0)

print(shortest_path(matrix, start, end))
