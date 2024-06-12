
import heapq

city_map = [
    [10, 'x', 'x', 1, 1, 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    [11, 9, 17, 'x', 14, 3, 'x', 13, 'x', 'x', 6, 'x'],
    ['x', 5, 'x', 'x', 10, 13, 13, 19, 10, 'x', 1, 12],
    [6, 'x', 'x', 17, 5, 6, 17, 4, 5, 'x', 1, 'x'],
    [4, 11, 1, 'x', 'x', 'x', 14, 7, 19, 4, 'x', 6],
    ['x', 'x', 6, 18, 'x', 'x', 'x', 5, 8, 2, 1, 'x'],
    [19, 19, 10, 9, 19, 19, 'x', 6, 'x', 1, 14, 11],
    ['x', 'x', 'x', 18, 11, 'x', 7, 5, 15, 13, 1, 11],
    ['x', 4, 'x', 8, 'x', 11, 'x', 'x', 9, 'x', 'x', 15],
    [10, 8, 10, 2, 'x', 'x', 'x', 'x', 'x', 12, 'x', 17],
    [19, 'x', 3, 11, 'x', 'x', 9, 3, 15, 'x', 5, 17],
    [18, 'x', 'x', 'x', 11, 14, 'x', 14, 13, 'x', 'x', 8]
]

districts = {
    1: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
    2: [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2), (6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2)],
    3: [(8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2), (10, 0), (10, 1), (10, 2), (11, 0), (11, 1), (11, 2)]
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
        
        row, col = node
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        
        for neighbor in neighbors:
            n_row, n_col = neighbor
            if 0 <= n_row < len(city_map) and 0 <= n_col < len(city_map[0]) and city_map[n_row][n_col] != 'x':
                heapq.heappush(heap, (cost + city_map[n_row][n_col], neighbor, path))
    
    return None

start_workshop = (3, 3)
end_workshop = (8, 11)

path = None
for district in districts.values():
    for workshop in district:
        path1 = dijkstra(start_workshop, workshop)
        if path1:
            for workshop2 in district:
                path2 = dijkstra(workshop, workshop2)
                if path2 and (not path or len(path1) + len(path2) < len(path)):
                    path = path1 + path2

print(path)
