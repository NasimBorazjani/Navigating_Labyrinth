
import heapq

def dijkstra(matrix, start, end):
    height = len(matrix)
    width = len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, Left, Down, Up
    visited = [[0 for _ in range(width)] for _ in range(height)]
    distances = [[float('inf') for _ in range(width)] for _ in range(height)]
    previous_nodes = [[None for _ in range(width)] for _ in range(height)]
    districts_visited = [False, False, False]
    distances[start[0]][start[1]] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node[0]][current_node[1]]:
            continue
        if current_node == end and len(districts_visited) == 3:
            break
        for direction in directions:
            next_node = (current_node[0] + direction[0], current_node[1] + direction[1])
            if 0 <= next_node[0] < height and 0 <= next_node[1] < width and matrix[next_node[0]][next_node[1]] != 'x' and not visited[next_node[0]][next_node[1]]:
                new_distance = current_distance + matrix[next_node[0]][next_node[1]]
                if new_distance < distances[next_node[0]][next_node[1]]:
                    distances[next_node[0]][next_node[1]] = new_distance
                    previous_nodes[next_node[0]][next_node[1]] = current_node
                    heapq.heappush(queue, (new_distance, next_node))
                    if next_node[0] in [0,1,2] and not districts_visited[0]: # District 1
                        districts_visited[0] = True
                    elif next_node[0] in [3,4,5,6,7] and not districts_visited[1]: # District 2
                        districts_visited[1] = True
                    elif next_node[0] in [8,9,10,11,12] and not districts_visited[2]: # District 3
                        districts_visited[2] = True
    path = []
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node[0]][current_node[1]]
    return path[::-1] # Reverse the path to get the correct order

matrix = [
    [5, 15, 15, 5, 6, 19, 'x', 9, 2, 'x', 16, 'x', 15],
    [16, 'x', 'x', 7, 5, 'x', 'x', 'x', 5, 2, 19, 'x', 3],
    ['x', 11, 2, 19, 17, 5, 11, 6, 3, 18, 15, 16, 'x'],
    [2, 'x', 12, 'x', 20, 11, 7, 19, 2, 'x', 4, 14, 'x'],
    [3, 'x', 19, 'x', 19, 'x', 14, 'x', 18, 7],
    [6, 'x', 5, 8, 3, 12, 12, 11, 5, 14, 'x', 'x'],
    ['x', 'x', 13, 'x', 'x', 20, 'x', 'x', 'x', 18, 10, 'x', 3],
    ['x', 'x', 13, 1, 10, 18, 'x', 'x', 'x', 'x', 10, 'x', 15],
    [10, 'x', 9, 2, 17, 19, 16, 8, 18, 10, 'x', 13],
    ['x', 'x', 2, 8, 2, 7, 'x', 17, 'x', 1, 9, 'x'],
    ['x', 13, 'x', 19, 15, 3, 15, 13, 1, 12, 4, 7, 'x'],
    [14, 'x', 'x', 'x', 'x', 'x', 16, 'x', 15, 'x', 'x', 'x'],
    [3, 15, 'x', 'x', 9, 'x', 9, 1, 6, 'x', 5]
]

start = (8, 2)
end = (2, 9)

print(dijkstra(matrix, start, end))
