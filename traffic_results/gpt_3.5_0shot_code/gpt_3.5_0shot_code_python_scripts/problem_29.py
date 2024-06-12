
import heapq

city_map = [
    [0, 0, 0, 4, 6, 0, 9, 15, 11, 2],
    [19, 0, 14, 3, 10, 18, 0, 0, 0, 1],
    [0, 9, 0, 11, 7, 14, 0, 0, 16, 18],
    [0, 5, 4, 5, 2, 4, 7, 5, 19, 14],
    [0, 3, 20, 0, 5, 16, 0, 0, 1, 9],
    [0, 3, 15, 9, 4, 0, 0, 0, 0, 4],
    [11, 18, 19, 8, 17, 9, 0, 10, 10, 19],
    [0, 0, 0, 17, 7, 0, 0, 7, 12, 8],
    [0, 0, 11, 19, 0, 13, 10, 13, 0, 0],
    [18, 0, 0, 0, 6, 10, 7, 0, 8, 0]
]

def get_neighbors(city_map, current_pos):
    neighbors = []
    rows, cols = len(city_map), len(city_map[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for dx, dy in directions:
        new_x, new_y = current_pos[0] + dx, current_pos[1] + dy
        if 0 <= new_x < rows and 0 <= new_y < cols and city_map[new_x][new_y] != 0:
            neighbors.append((new_x, new_y))
    
    return neighbors

def dijkstra(city_map, start, end):
    pq = [(0, start, [start])]
    visited = set()
    
    while pq:
        cost, current_pos, path = heapq.heappop(pq)
        
        if current_pos == end:
            return path
        
        if current_pos in visited:
            continue
        
        visited.add(current_pos)
        
        for neighbor in get_neighbors(city_map, current_pos):
            new_cost = cost + city_map[neighbor[0]][neighbor[1]]
            heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))
    
    return None

start_pos = (3, 9)
end_pos = (6, 1)

path = dijkstra(city_map, start_pos, end_pos)
print(path)
