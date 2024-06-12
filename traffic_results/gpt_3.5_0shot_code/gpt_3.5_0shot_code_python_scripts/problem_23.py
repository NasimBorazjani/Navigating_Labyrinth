
import heapq

city_map = [
    [0, 0, 0, 0, 0, 8, 0, 15, 18, 10],
    [4, 5, 10, 6, 20, 2, 12, 0, 0, 0],
    [19, 6, 19, 7, 6, 2, 0, 15, 0, 14],
    [16, 17, 0, 2, 3, 7, 4, 0, 18, 6],
    [0, 2, 1, 19, 7, 10, 18, 5, 3, 19],
    [8, 5, 0, 1, 0, 10, 17, 0, 13, 5],
    [18, 1, 3, 4, 0, 0, 8, 0, 5, 0],
    [15, 0, 0, 13, 0, 11, 0, 2, 0, 0],
    [4, 0, 0, 4, 1, 0, 0, 0, 0, 0],
    [0, 10, 8, 0, 0, 7, 19, 0, 0, 0]
]

districts = {
    1: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
    2: [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2)],
    3: [(5, 0), (5, 1), (5, 2), (6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2)]
}

start = (5, 8)
end = (3, 0)

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
            if 0 <= n_row < len(city_map) and 0 <= n_col < len(city_map[0]) and city_map[n_row][n_col] != 0 and neighbor not in visited:
                heapq.heappush(heap, (cost + city_map[n_row][n_col], neighbor, path))
    
    return None

path = None
for d1 in districts[1]:
    for d2 in districts[2]:
        for d3 in districts[3]:
            path1 = dijkstra(start, d1)
            path2 = dijkstra(d1, d2)
            path3 = dijkstra(d2, d3)
            path4 = dijkstra(d3, end)
            
            if path1 and path2 and path3 and path4:
                path = path1 + path2[1:] + path3[1:] + path4[1:]
                break

if path:
    print(path)
else:
    print("No valid path found")
