
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # right, left, down, up
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    distances = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    previous_nodes = [[None for _ in range(cols)] for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if visited[current_node[0]][current_node[1]]:
            continue
        visited[current_node[0]][current_node[1]] = True
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node[0]][current_node[1]]
            return path[::-1] # shortest path from start to end
        for direction in directions:
            next_node = (current_node[0] + direction[0], current_node[1] + direction[1])
            if (0 <= next_node[0] < rows and 0 <= next_node[1] < cols and 
                not visited[next_node[0]][next_node[1]] and matrix[next_node[0]][next_node[1]] != 'x'):
                distance = current_distance + matrix[next_node[0]][next_node[1]]
                if distance < distances[next_node[0]][next_node[1]]:
                    distances[next_node[0]][next_node[1]] = distance
                    previous_nodes[next_node[0]][next_node[1]] = current_node
                    heapq.heappush(queue, (distance, next_node))
    return [] # if there is no path

matrix = [['x', 'x', 'x', 3, 'x', 'x', 16, 2, 16, 3],
          [8, 'x', 8, 5, 'x', 'x', 10, 'x', 19, 4, 'x'],
          ['x', 'x', 18, 1, 16, 'x', 9, 15, 'x', 'x', 11],
          ['x', 'x', 17, 16, 4, 19, 2, 'x', 1, 11, 'x'],
          [9, 'x', 5, 16, 18, 'x', 'x', 7, 18, 6],
          ['x', 15, 7, 'x', 'x', 'x', 19, 8, 9, 17, 'x'],
          ['x', 15, 19, 'x', 'x', 'x', 6, 2, 6, 'x', 5],
          ['x', 12, 11, 3, 11, 4, 'x', 'x', 'x', 3, 'x'],
          [18, 12, 4, 'x', 3, 10, 'x', 3, 'x', 7, 14],
          [15, 11, 12, 'x', 13, 2, 'x', 'x', 5, 14, 'x'],
          ['x', 'x', 15, 'x', 16, 4, 10, 13, 'x', 'x', 4]]

start = (3, 6)
end = (8, 0)

path = dijkstra(matrix, start, end)
print(path)
