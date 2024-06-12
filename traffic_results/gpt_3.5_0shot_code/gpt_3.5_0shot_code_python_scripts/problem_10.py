
import heapq

# Define the matrix map of the city
city_map = [
    [float('inf'), float('inf'), 6, float('inf'), 7, float('inf'), 9, 4, 11],
    [float('inf'), 3, float('inf'), 6, 5, 3, 15, float('inf'), 3],
    [float('inf'), float('inf'), float('inf'), 4, float('inf'), 9, 1, 8, float('inf')],
    [15, 18, 1, 6, 5, 10, 6, 14, 8],
    [18, 10, 7, 18, 2, float('inf'), float('inf'), float('inf'), 7],
    [11, 9, 16, float('inf'), 11, float('inf'), 11, float('inf'), 17],
    [7, float('inf'), 18, float('inf'), 8, 10, 20, 6, float('inf')],
    [15, 4, 17, float('inf'), 16, 2, 12, 16, float('inf')],
    [9, 10, 18, 17, 9, 6, 7, float('inf'), 15]
]

# Define the districts
districts = {
    1: [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2)],
    2: [(4, 0), (4, 1), (4, 2), (4, 3), (5, 0), (5, 2), (5, 3), (6, 0), (6, 1), (6, 2)],
    3: [(7, 0), (7, 1), (7, 2), (7, 3), (8, 0), (8, 1), (8, 2), (8, 3)]
}

# Define the start and end workshops
start_workshop = (3, 0)
end_workshop = (6, 6)

# Dijkstra's algorithm to find the shortest path
def dijkstra(start, end):
    heap = [(0, start, [])]
    visited = set()
    
    while heap:
        (cost, node, path) = heapq.heappop(heap)
        
        if node in visited:
            continue
        
        path = path + [node]
        
        if node == end:
            return path
        
        visited.add(node)
        
        row, col = node
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        
        for neighbor in neighbors:
            n_row, n_col = neighbor
            if 0 <= n_row < len(city_map) and 0 <= n_col < len(city_map[0]) and city_map[n_row][n_col] != 'x':
                new_cost = cost + city_map[n_row][n_col]
                heapq.heappush(heap, (new_cost, neighbor, path))
    
    return None

# Find the shortest path that visits at least one workshop in each district
path = None
for district in districts.values():
    for workshop in district:
        temp_path = dijkstra(start_workshop, workshop)
        if temp_path:
            temp_path += dijkstra(workshop, end_workshop)[1:]
            if not path or sum(city_map[row][col] for row, col in temp_path) < sum(city_map[row][col] for row, col in path):
                path = temp_path

# Print the shortest path
print(path)
