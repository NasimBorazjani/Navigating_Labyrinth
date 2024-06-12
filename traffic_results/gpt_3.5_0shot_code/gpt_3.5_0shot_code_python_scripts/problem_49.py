
import heapq

city_map = [
    [None, None, 13, 9, None, 15, None, None, 2, 13, 9, 11],
    [8, None, 4, 5, 13, None, None, 7, 16, None, 15, 13],
    [None, None, None, None, 3, None, 4, 3, 18, None, 11, 18],
    [6, None, 14, 5, 16, None, 11, None, 3, 16, 3, 3],
    [15, 12, None, None, 10, 3, 2, 14, None, 18, None, None],
    [11, 1, 2, 1, 17, 15, None, 2, None, 12, None, None],
    [None, None, 3, 15, 16, 1, None, None, None, None, None, None],
    [None, 10, None, None, None, 6, 1, 8, 19, 13, 7, None],
    [None, None, None, None, None, None, None, None, None, None, None, 3],
    [3, 7, 12, None, 15, None, 19, 13, 17, 14, None, None],
    [None, None, None, None, 4, 4, 18, None, 5, None, None, 10],
    [None, None, 15, 9, 13, 10, 8, 4, 8, 6, 7, 7]
]

districts = {
    1: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
    2: [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
    3: [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2), (10, 0), (10, 1), (10, 2), (11, 0), (11, 1), (11, 2)]
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
                heapq.heappush(heap, (cost + get_cost(node, neighbor), neighbor, path))
    
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

def get_cost(node1, node2):
    return city_map[node2[0]][node2[1]]

start = (3, 11)
end = (4, 0)

path = dijkstra(start, end)
print(path)
