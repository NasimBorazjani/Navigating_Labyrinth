
import heapq

city_map = [
    [None, None, None, None, 13, None, None, 3, 8],
    [None, 18, 19, 19, 2, 9, None, None, None],
    [15, None, 6, None, None, None, 13, 13, 4],
    [7, None, 4, 10, None, 11, 10, 17, None],
    [2, 7, None, None, 8, 16, 4, 1, 4],
    [None, None, None, 5, 16, 15, None, 17, 10],
    [None, None, None, 5, 14, 9, 3, 15, None],
    [None, 6, 4, None, None, None, 18, None, None],
    [17, None, 19, None, 1, 4, 8, None, 8]
]

districts = {
    1: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)],
    2: [(2, 0), (2, 2), (2, 6), (2, 7), (2, 8), (3, 0), (3, 2), (3, 3), (3, 5), (3, 6), (3, 8), (4, 0), (4, 1), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)],
    3: [(5, 3), (5, 4), (5, 5), (5, 7), (5, 8), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (7, 1), (7, 2), (7, 5), (7, 6), (8, 0), (8, 2), (8, 4), (8, 5), (8, 7), (8, 8)]
}

def dijkstra(start, end):
    heap = [(0, start, [])]
    visited = set()
    
    while heap:
        (cost, node, path) = heapq.heappop(heap)
        
        if node in visited:
            continue
        
        path = path + [node]
        visited.add(node)
        
        if node == end:
            return path
        
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                heapq.heappush(heap, (cost + city_map[neighbor[0]][neighbor[1]], neighbor, path))
    
    return None

def get_neighbors(node):
    neighbors = []
    row, col = node
    
    if row > 0 and city_map[row-1][col] is not None:
        neighbors.append((row-1, col))
    if row < len(city_map) - 1 and city_map[row+1][col] is not None:
        neighbors.append((row+1, col))
    if col > 0 and city_map[row][col-1] is not None:
        neighbors.append((row, col-1))
    if col < len(city_map[0]) - 1 and city_map[row][col+1] is not None:
        neighbors.append((row, col+1))
    
    return neighbors

start = (2, 8)
end = (6, 3)

path = dijkstra(start, end)
print(path)
