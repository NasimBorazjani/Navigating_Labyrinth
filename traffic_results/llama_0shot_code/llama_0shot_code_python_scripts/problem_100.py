
import heapq

def dijkstra(matrix, start, end):
    height = len(matrix)
    width = len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # north, south, east, west
    visited = set()
    queue = [(matrix[start[0]][start[1]], start)]
    prev = {start: None}

    while queue:
        (dist, current) = heapq.heappop(queue)
        if current not in visited:
            visited.add(current)
            if current == end:
                path = []
                while current is not None:
                    path.append(current)
                    current = prev[current]
                return path[::-1] # shortest path from start to end
            for direction in directions:
                next_node = (current[0] + direction[0], current[1] + direction[1])
                if (0 <= next_node[0] < height and 0 <= next_node[1] < width and matrix[next_node[0]][next_node[1]] != 'x' and next_node not in visited):
                    heapq.heappush(queue, (dist + matrix[next_node[0]][next_node[1]], next_node))
                    prev[next_node] = current
    return None # if there is no path from start to end

def get_path(matrix, start, end):
    path = dijkstra(matrix, start, end)
    return [matrix[i[0]][i[1]] for i in path]

matrix = [
    ['x', 2, 16, 'x', 9, 'x', 14, 'x', 'x', 4, 8],
    [9, 'x', 4, 'x', 'x', 7, 11, 'x', 'x', 6, 11, 'x'],
    ['x', 'x', 10, 14, 'x', 'x', 18, 'x', 'x', 'x', 'x', 6, 16, 'x'],
    # ...
    ['x', 13, 3, 3, 1, 'x', 6, 14, 20, 8, 'x', 4, 10, 17, 'x'],
    [1, 8, 'x', 16, 'x', 'x', 9, 'x', 10, 'x', 'x', 5, 8],
    ['x', 'x', 1, 'x', 6, 'x', 'x', 7, 16, 'x', 'x', 'x', 17, 'x'],
    [14, 'x', 'x', 10, 18, 'x', 6, 13, 'x', 'x', 'x', 'x', 15, 'x'],
    ['x', 8, 2, 'x', 17, 'x', 'x', 7, 14, 4, 8, 12, 3, 'x', 15, 13, 2],
    [16, 'x', 'x', 12, 'x', 8, 1, 7, 7, 12, 17, 2, 2, 7],
    ['x', 1, 8, 'x', 6, 14, 20, 8, 'x', 4, 10, 17, 'x'],
    [1, 8, 'x', 16, 'x', 'x', 9, 'x', 10, 'x', 'x', 5, 8],
    ['x', 'x', 1, 'x', 6, 'x', 'x', 7, 16, 'x', 'x', 'x', 'x', 17, 'x'],
    [14, 'x', 'x', 10, 18, 'x', 6, 13, 'x', 'x', 'x', 'x', 15, 'x'],
    ['x', 8, 2, 'x', 17, 'x', 'x', 7, 14, 4, 4, 'x', 'x', 17, 'x']
]

print(get_path(matrix, (4, 0), (9, 11)))
