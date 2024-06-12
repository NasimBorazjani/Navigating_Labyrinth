
import heapq

city_map = [
    [None, 10, None, 8, 13, 8, 4, 3, 15, None, 17],
    [9, None, 6, 4, 17, None, 16, 3, 19, None, None],
    [8, 3, 18, None, None, 3, None, 7, 12, 16, 17],
    [8, None, None, 13, None, 7, None, 8, None, 12, 9],
    [2, 9, None, None, 9, 4, 18, None, None, 11, None],
    [14, 20, None, None, None, None, 10, None, None, 7, None],
    [None, None, 18, 16, 12, 10, None, None, 10, None, None],
    [None, None, 16, None, None, 10, None, None, 3, 18, 18],
    [None, None, None, None, None, None, 13, 3, None, None, None],
    [5, 13, 1, None, None, 8, None, 19, None, None, None],
    [None, None, 16, None, None, 7, 18, 4, 11, None, 16]
]

districts = {
    1: [(0, 0), (0, 1)],
    2: [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
    3: [(5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10)]
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
        
        for neighbor, weight in city_map[node[0]][node[1]].items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor, path))
    
    return None

def find_path(start, end):
    path = []
    
    for district in districts.values():
        for workshop in district:
            temp_path = dijkstra(start, workshop) + dijkstra(workshop, end)[1:]
            if temp_path and (not path or len(temp_path) < len(path)):
                path = temp_path
    
    return path

start = (3, 10)
end = (5, 1)
path = find_path(start, end)
print(path)
