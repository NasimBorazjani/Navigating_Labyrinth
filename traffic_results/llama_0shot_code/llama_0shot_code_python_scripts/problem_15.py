
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # right, left, down, up

    # Create a graph from the matrix
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Use Dijkstra's algorithm to find the shortest path
    queue = [(matrix[start[0]][start[1]], start, [])]
    visited = set()
    while queue:
        dist, node, path = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return path[::-1] # Reverse the path to get the correct direction
            for neighbor, cost in graph[node].items():
                heapq.heappush(queue, (dist + cost, neighbor, path))

    return None # If there's no path to the destination

# Test the function
matrix = [
    [4, 13, 'x', 9, 'x', 'x', 'x', 'x', 'x'],
    [1, 11, 'x', 16, 5, 7, 12, 16, 'x'],
    [12, 11, 'x', 14, 'x', 'x', 12, 'x', 3],
    [9, 11, 'x', 9, 10, 'x', 'x', 'x', 'x'],
    [20, 2, 'x', 1, 16, 12, 18, 17, 10],
    [10, 13, 4, 15, 13, 2, 20, 3, 15],
    ['x', 6, 13, 1, 8, 20, 14, 11, 3],
    [14, 'x', 9, 'x', 'x', 13, 19, 10, 'x'],
    [12, 'x', 18, 1, 'x', 'x', 9, 'x', 'x']
]

start, end = (3, 1), (5, 8)
print(shortest_path(matrix, start, end))
