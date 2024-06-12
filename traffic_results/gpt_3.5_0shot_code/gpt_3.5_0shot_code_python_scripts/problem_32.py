
import heapq

city_map = [
    [0, 0, 13, 0, 0, 7, 0, 13, 3, 0, 13],
    [10, 4, 0, 4, 12, 2, 0, 3, 4, 0, 15],
    [0, 3, 0, 0, 15, 9, 0, 0, 18, 17, 14],
    [5, 0, 0, 0, 3, 0, 11, 0, 17, 9, 17],
    [8, 3, 13, 0, 5, 7, 8, 17, 7, 0, 0],
    [0, 0, 13, 2, 2, 11, 6, 8, 0, 0, 0],
    [0, 1, 9, 6, 5, 13, 16, 1, 7, 5, 0],
    [4, 0, 13, 0, 10, 18, 3, 0, 0, 19, 19],
    [0, 0, 0, 2, 5, 9, 13, 0, 7, 1, 0],
    [0, 0, 7, 0, 0, 5, 19, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 19, 0, 0, 0, 0, 1]
]

districts = {
    1: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 8), (2, 9), (2, 10)],
    2: [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10)],
    3: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (5, 1), (5, 2)]
}

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
        
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                heapq.heappush(heap, (cost + city_map[neighbor[0]][neighbor[1]], neighbor, path))
    
    return None

def get_neighbors(node):
    neighbors = []
    row, col = node
    
    if row > 0 and city_map[row - 1][col] != 'x':
        neighbors.append((row - 1, col))
    if row < len(city_map) - 1 and city_map[row + 1][col] != 'x':
        neighbors.append((row + 1, col))
    if col > 0 and city_map[row][col - 1] != 'x':
        neighbors.append((row, col - 1))
    if col < len(city_map[0]) - 1 and city_map[row][col + 1] != 'x':
        neighbors.append((row, col + 1))
    
    return neighbors

start = (5, 2)
end = (2, 10)

path = None
for district in districts.values():
    for workshop in district:
        temp_path = dijkstra(start, workshop) + dijkstra(workshop, end)[1:]
        if temp_path and (not path or len(temp_path) < len(path)):
            path = temp_path

print(path)
