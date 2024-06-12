
import heapq

# Define the matrix map of the city
city_map = [
    ['x', 9, 'x', 10, 'x', 11, 13, 5, 4, 'x', 'x', 19, 13, 'x', 'x'],
    ['x', 6, 3, 8, 18, 8, 1, 5, 2, 'x', 'x', 17, 'x', 'x', 'x'],
    ['x', 'x', 11, 5, 'x', 11, 13, 20, 7, 'x', 'x', 'x', 'x', 15, 4],
    [3, 'x', 14, 4, 20, 4, 15, 12, 12, 4, 'x', 8, 4, 'x', 'x'],
    [4, 1, 'x', 9, 17, 'x', 17, 'x', 11, 16, 6, 12, 'x', 18, 'x'],
    [8, 5, 17, 'x', 'x', 1, 'x', 'x', 'x', 19, 14, 2, 1, 'x', 'x'],
    [11, 9, 'x', 'x', 14, 'x', 'x', 'x', 'x', 'x', 'x', 2, 12, 4, 16],
    ['x', 'x', 2, 'x', 'x', 6, 6, 8, 'x', 11, 18, 11, 10, 'x', 'x'],
    ['x', 'x', 'x', 16, 'x', 7, 'x', 'x', 'x', 'x', 7, 11, 18, 9, 17],
    [13, 19, 13, 'x', 18, 'x', 14, 'x', 14, 14, 'x', 'x', 20, 15, 15],
    ['x', 'x', 'x', 'x', 17, 'x', 8, 'x', 'x', 'x', 'x', 'x', 6, 11, 'x'],
    [5, 'x', 7, 'x', 15, 'x', 'x', 19, 1, 'x', 'x', 10, 'x', 'x', 18],
    [11, 19, 'x', 18, 'x', 5, 'x', 19, 16, 'x', 'x', 13, 'x', 'x', 5],
    [8, 16, 6, 13, 1, 'x', 14, 4, 'x', 'x', 'x', 1, 'x', 'x', 5],
    ['x', 19, 5, 'x', 'x', 'x', 12, 5, 9, 16, 11, 9, 14, 'x', 'x']
]

# Define the districts
districts = {
    1: [(0, 3), (0, 4), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8), (2, 12), (2, 13)],
    2: [(4, 0), (4, 1), (4, 3), (4, 4), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (4, 13)],
    3: [(8, 0), (8, 1), (8, 2), (8, 4), (8, 6), (8, 7), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (9, 0), (9, 1), (9, 2), (9, 5), (9, 7), (9, 8), (9, 9), (9, 12), (9, 13), (9, 14), (10, 12), (10, 13), (10, 14), (11, 1), (11, 3), (11, 5), (11, 7), (11, 8), (11, 9), (11, 10), (11, 12), (11, 13), (11, 14), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 12), (12, 13), (12, 14), (13, 0), (13, 1), (13, 2), (13, 3), (13, 4), (13, 6), (13, 7), (13, 8), (13, 9), (13, 10), (13, 11), (13, 13), (13, 14)]
}

# Define the directions Ben can move
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Define the function to calculate the shortest path using Dijkstra's algorithm
def dijkstra(start, end):
    heap = [(0, start, [])]
    visited = set()
    
    while heap:
        (cost, node, path) = heapq.heappop(heap)
        
        if node in visited:
            continue
        
        visited.add(node)
        path = path + [node]
        
        if node == end:
            return path
        
        row, col = node
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            new_node = (new_row, new_col)
            
            if 0 <= new_row < len(city_map) and 0 <= new_col < len(city_map[0]) and city_map[new_row][new_col] != 'x' and new_node not in visited:
                new_cost = cost + city_map[new_row][new_col]
                heapq.heappush(heap, (new_cost, new_node, path))
    
    return None

# Find the shortest path that satisfies the conditions
shortest_path = None
for workshop1 in districts[1]:
    for workshop2 in districts[2]:
        for workshop3 in districts[3]:
            path1 = dijkstra((8, 13), workshop1)
            path2 = dijkstra(workshop1, workshop2)
            path3 = dijkstra(workshop2, workshop3)
            
            if path1 and path2 and path3:
                total_path = path1 + path2[1:] + path3[1:]
                if not shortest_path or sum(city_map[row][col] for row, col in total_path) < sum(city_map[row][col] for row, col in shortest_path):
                    shortest_path = total_path

# Print the shortest path
print(shortest_path)
