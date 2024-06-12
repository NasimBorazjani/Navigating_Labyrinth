
import heapq

city_map = [
    [15, 'x', 8, 'x', 6, 9, 'x', 'x', 'x'],
    [14, 'x', 8, 'x', 14, 'x', 5, 11, 'x', 9],
    ['x', 17, 8, 'x', 17, 15, 12, 'x', 'x', 13],
    ['x', 13, 'x', 'x', 2, 'x', 17, 17, 1, 'x'],
    [6, 'x', 1, 5, 17, 'x', 2, 18, 11, 7],
    [12, 8, 17, 10, 'x', 'x', 'x', 15, 'x', 16],
    [12, 12, 'x', 4, 'x', 13, 'x', 10, 'x', 16],
    ['x', 'x', 10, 'x', 6, 'x', 'x', 'x', 8, 5],
    ['x', 2, 11, 18, 15, 'x', 11, 'x', 'x', 12],
    ['x', 'x', 14, 'x', 'x', 7, 14, 15, 18, 9]
]

districts = {
    1: [(0, 0), (0, 2), (1, 2), (1, 4)],
    2: [(4, 0), (4, 2), (5, 2), (5, 9)],
    3: [(6, 3), (6, 7), (7, 2), (7, 8), (8, 1), (8, 6), (9, 2), (9, 6)]
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
                heapq.heappush(heap, (cost + get_cost(node, neighbor), neighbor, path))
    
    return None

def get_neighbors(node):
    neighbors = []
    row, col = node
    
    if row > 0 and city_map[row-1][col] != 'x':
        neighbors.append((row-1, col))
    if row < len(city_map) - 1 and city_map[row+1][col] != 'x':
        neighbors.append((row+1, col))
    if col > 0 and city_map[row][col-1] != 'x':
        neighbors.append((row, col-1))
    if col < len(city_map[0]) - 1 and city_map[row][col+1] != 'x':
        neighbors.append((row, col+1))
    
    return neighbors

def get_cost(node1, node2):
    row1, col1 = node1
    row2, col2 = node2
    
    return city_map[row2][col2]

start = (5, 0)
end = (3, 8)

path = dijkstra(start, end)
print(path)
