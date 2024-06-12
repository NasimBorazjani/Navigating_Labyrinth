
import heapq

# Define the city map
city_map = [
    [11, -1, -1, -1, 15, 5, 18, 4, 1, 17, 14, -1, 9],
    [-1, 10, 10, 7, 12, 12, 6, -1, -1, 8, 4, 19, 11],
    [17, -1, -1, 12, 8, -1, -1, -1, 14, 19, -1, 18, 16],
    [17, -1, 16, -1, -1, 17, 4, -1, 15, -1, -1, -1, 17],
    [17, -1, -1, 6, -1, -1, 12, 6, 10, 3, 11, -1, 19],
    [10, -1, 9, 15, 17, 4, -1, -1, -1, -1, 14, 17, 18],
    [4, -1, -1, -1, -1, 13, 18, 13, -1, 17, 12, -1, 19],
    [-1, 2, 11, 7, 6, 14, 9, -1, 12, 17, 9, 13, 14],
    [-1, 18, 16, -1, -1, -1, 11, 6, 12, -1, -1, 10, -1],
    [5, 3, -1, -1, -1, 5, -1, 14, -1, -1, -1, -1, -1],
    [18, -1, -1, -1, -1, 14, -1, -1, 13, 1, 3, -1, -1],
    [1, 16, 10, -1, -1, 14, 13, -1, 10, -1, 1, -1, 18],
    [8, -1, -1, 10, 2, 10, -1, -1, -1, -1, -1, 13, 5]
]

# Define the districts
districts = {
    1: [(0, 0), (0, 1), (0, 2)],
    2: [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)],
    3: [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11), (8, 12)]
}

# Define the start and end workshops
start = (8, 11)
end = (2, 3)

# Define the directions
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(start, end):
    pq = [(0, start, [start])]
    visited = set()
    
    while pq:
        cost, current, path = heapq.heappop(pq)
        
        if current == end:
            return path
        
        if current in visited:
            continue
        
        visited.add(current)
        
        for dx, dy in directions:
            new_x, new_y = current[0] + dx, current[1] + dy
            
            if 0 <= new_x < len(city_map) and 0 <= new_y < len(city_map[0]) and city_map[new_x][new_y] != -1:
                new_cost = cost + city_map[new_x][new_y]
                heapq.heappush(pq, (new_cost, (new_x, new_y), path + [(new_x, new_y)]))
    
    return None

# Find the shortest path that satisfies the conditions
for district in districts.values():
    for workshop in district:
        path1 = dijkstra(start, workshop)
        if path1:
            for workshop2 in district:
                path2 = dijkstra(workshop, workshop2)
                if path2:
                    path3 = dijkstra(workshop2, end)
                    if path3:
                        print(path1 + path2[1:] + path3)
                        exit()
