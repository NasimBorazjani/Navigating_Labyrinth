
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    def in_bounds(row, col):
        return 0 <= row < rows and 0 <= col < cols

    def get_min_distance_node(distances, visited):
        min_val = float('inf')
        min_node = None
        for node in distances:
            if node not in visited and distances[node] < min_val:
                min_val = distances[node]
                min_node = node
        return min_node

    def get_neighbors(node):
        row, col = node
        neighbors = []
        for direction in directions:
            new_row, new_col = row + direction[0], col + direction[1]
            if in_bounds(new_row, new_col) and matrix[new_row][new_col] != 'x':
                neighbors.append((new_row, new_col))
        return neighbors

    distances = {node: float('inf') for row in range(rows) for col in range(cols) for node in [(row, col)]}
    distances[start] = 0
    visited = set()
    distances_queue = [(0, start)]

    while distances_queue:
        current_distance, current_node = heapq.heappop(distances_queue)
        if current_node not in visited:
            visited.add(current_node)
            if current_node == end:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = previous_nodes.get(current_node, None)
                return path[::-1]  # shortest path from start to end
            for neighbor in get_neighbors(current_node):
                distance = current_distance + matrix[neighbor[0]][neighbor[1]]
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(distances_queue, (distance, neighbor))
                    previous_nodes[neighbor] = current_node

    return []  # if there is no path from start to end

previous_nodes = {}
start, end = (5, 8), (3, 0)
matrix = [['x', 'x', 'x', 'x', 'x', '8', '15', '18', '10'],
          ['4', '5', '10', '6', '20', '2', '12', 'x', 'x', 'x'],
          ['19', '6', '19', '7', '6', '2', 'x', '15', 'x', '14'],
          ['16', '17', 'x', '2', '3', '7', '4', 'x', '18', '6'],
          ['x', '2', '1', '19', '7', '10', '18', '5', '3', '19'],
          ['8', '5', 'x', '1', 'x', '10', '17', 'x', '13', '5'],
          ['18', '1', '3', '4', 'x', 'x', '8', 'x', '5', 'x'],
          ['15', 'x', 'x', '13', 'x', '11', 'x', '2', 'x', 'x'],
          ['4', 'x', 'x', '4', '1', 'x', 'x', 'x', 'x', 'x'],
          ['x', '10', '8', 'x', 'x', '7', '19', 'x', 'x', 'x']]

path = dijkstra(matrix, start, end)
print(path)
