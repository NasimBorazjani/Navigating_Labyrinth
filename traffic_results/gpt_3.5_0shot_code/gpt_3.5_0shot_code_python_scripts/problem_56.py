
import heapq

# Define the matrix map of the city
city_map = [
    [2, -1, -1, 14, -1, 19, 6, -1, -1, 14, 18, -1],
    [-1, 10, 1, 15, -1, -1, -1, -1, 17, 2, 9, 12],
    [13, 14, -1, 2, -1, -1, 10, 10, -1, -1, -1, -1],
    [9, 17, 3, 15, 4, 4, -1, 9, 15, 16, -1, 9],
    [10, 7, 3, 8, -1, 7, -1, 16, 3, 7, -1, -1],
    [16, 20, 16, 19, 18, 3, -1, -1, 11, 14, 5, -1],
    [14, 13, 8, 14, 12, 19, 6, 3, 19, 10, 11, -1],
    [-1, 18, -1, -1, 4, 19, 6, 14, 15, 17, 7, -1],
    [-1, 2, -1, -1, -1, -1, -1, 7, -1, 19, -1, -1],
    [-1, 3, 14, 1, -1, 18, 4, 12, -1, 3, 10, -1],
    [2, -1, 16, 13, -1, 17, -1, -1, 17, 16, 4, 10],
    [-1, 4, 10, -1, -1, -1, 7, -1, 19, 7, -1, -1]
]

# Define the districts
districts = {
    1: [(0, 0), (0, 1), (0, 2), (0, 3)],
    2: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)],
    3: [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10)]
}

# Define the start and end workshops
start = (6, 9)
end = (3, 0)

# Dijkstra's algorithm to find the shortest path
def dijkstra(start, end):
    heap = [(0, start, [start])]
    visited = set()
    
    while heap:
        (cost, current, path) = heapq.heappop(heap)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        if current == end:
            return path
        
        row, col = current
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            new_pos = (new_row, new_col)
            
            if 0 <= new_row < len(city_map) and 0 <= new_col < len(city_map[0]) and city_map[new_row][new_col] != -1 and new_pos not in visited:
                new_cost = cost + city_map[new_row][new_col]
                new_path = path + [new_pos]
                heapq.heappush(heap, (new_cost, new_pos, new_path))
    
    return None

# Find the shortest path while visiting at least one workshop in each district
path = None
for district in districts.values():
    for workshop in district:
        temp_path = dijkstra(start, workshop)
        if temp_path:
            temp_path += dijkstra(workshop, end)[1:]
            if path is None or sum(city_map[row][col] for row, col in temp_path) < sum(city_map[row][col] for row, col in path):
                path = temp_path

# Print the shortest path
print(path)
