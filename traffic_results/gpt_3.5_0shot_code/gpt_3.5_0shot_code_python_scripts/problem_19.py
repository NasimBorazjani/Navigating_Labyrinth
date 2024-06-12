
import heapq

city_map = [
    ['x', 16, 15, 14, 2, 12, 3, 'x', 7, 7],
    [11, 'x', 'x', 'x', 4, 10, 5, 'x', 'x', 'x'],
    [12, 'x', 3, 'x', 'x', 19, 'x', 13, 'x', 'x'],
    [16, 15, 13, 'x', 12, 'x', 'x', 1, 'x', 7],
    [2, 6, 'x', 5, 'x', 14, 7, 'x', 8, 18],
    [19, 17, 2, 11, 8, 17, 12, 8, 9, 14],
    [11, 1, 10, 11, 'x', 'x', 19, 6, 2, 18],
    [7, 'x', 10, 15, 'x', 'x', 'x', 'x', 18, 17],
    ['x', 6, 'x', 'x', 'x', 5, 'x', 7, 12, 20],
    ['x', 'x', 2, 15, 'x', 17, 'x', 'x', 10, 11]
]

districts = {
    1: [(0, 0), (0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (1, 6), (2, 0), (2, 2), (2, 5)],
    2: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 8), (4, 9), (5, 0), (5, 1)],
    3: [(6, 0), (6, 1), (6, 2), (6, 3), (6, 6), (6, 7), (6, 8), (6, 9), (7, 2), (7, 8), (8, 2), (8, 4), (8, 6), (8, 8), (8, 9), (9, 2), (9, 3), (9, 5), (9, 8), (9, 9)]
}

start = (5, 0)
end = (3, 9)

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

path = dijkstra(start, end)
print(path)
