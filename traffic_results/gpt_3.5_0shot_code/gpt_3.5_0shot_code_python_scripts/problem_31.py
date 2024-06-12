
import heapq

city_map = [
    [10, 'x', 19, 11, 'x', 'x', 6, 12, 'x', 'x', 'x'],
    [2, 9, 10, 'x', 'x', 10, 17, 'x', 'x', 11, 5],
    ['x', 15, 8, 9, 'x', 7, 17, 20, 'x', 'x', 13],
    [1, 9, 15, 14, 9, 9, 13, 7, 12, 'x', 10],
    [9, 'x', 17, 'x', 'x', 7, 'x', 'x', 1, 'x', 14],
    [16, 18, 11, 'x', 14, 18, 9, 13, 'x', 'x', 'x'],
    [9, 3, 5, 8, 17, 15, 19, 'x', 3, 'x', 14],
    [2, 13, 'x', 'x', 17, 13, 14, 18, 9, 'x', 6],
    [3, 'x', 18, 6, 'x', 14, 'x', 'x', 'x', 8, 19],
    [2, 4, 'x', 'x', 'x', 'x', 3, 4, 'x', 19, 'x'],
    ['x', 'x', 'x', 'x', 11, 'x', 'x', 'x', 'x', 5, 5]
]

districts = {
    1: [(0, 0), (0, 1), (0, 2)],
    2: [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)],
    3: [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10)]
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
        
        for i in range(len(city_map)):
            for j in range(len(city_map[0])):
                if city_map[i][j] != 'x' and (i, j) != node:
                    new_cost = cost + city_map[i][j]
                    heapq.heappush(heap, (new_cost, (i, j), path))
    
    return None

start_workshop = (3, 7)
end_workshop = (7, 0)

path = None
for district in districts.values():
    for workshop in district:
        path1 = dijkstra(start_workshop, workshop)
        if path1:
            for workshop2 in district:
                path2 = dijkstra(workshop, workshop2)
                if path2:
                    path3 = dijkstra(workshop2, end_workshop)
                    if path3:
                        path = path1 + path2[1:] + path3[1:]
                        break
        if path:
            break
    if path:
        break

print(path)
