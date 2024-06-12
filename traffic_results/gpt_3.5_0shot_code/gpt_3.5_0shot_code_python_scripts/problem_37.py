
import heapq

# Define the city map
city_map = [
    [15, -1, 12, -1, 9, 19, -1, -1, 13, -1, 16],
    [14, 6, 3, 18, -1, 8, 18, -1, -1, -1, -1],
    [16, 10, 9, 4, 9, 5, 15, 4, -1, -1, 2],
    [5, 9, -1, 8, 1, 15, 7, 15, -1, -1, -1],
    [6, -1, 3, -1, 4, 6, 6, 19, -1, 16, 13],
    [17, -1, 11, 5, 18, 11, 18, -1, -1, 10, 19],
    [6, 3, -1, -1, 10, 18, 2, -1, -1, -1, -1],
    [-1, -1, 4, 2, -1, 13, 7, -1, 3, 19, 16],
    [-1, 1, 10, -1, 15, -1, 2, -1, 1, 7, 10],
    [-1, -1, -1, 4, 7, -1, 7, -1, -1, 6, -1],
    [16, -1, 15, 3, -1, 8, -1, -1, 13, -1, 14]
]

# Define the districts
districts = {
    1: [(0, 0), (0, 1)],
    2: [(2, 0), (6, 0)],
    3: [(7, 0), (10, 0)]
}

# Define the start and end workshops
start = (7, 5)
end = (1, 0)

# Define the directions
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Dijkstra's algorithm to find the shortest path
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
            x, y = current[0] + dx, current[1] + dy
            
            if 0 <= x < len(city_map) and 0 <= y < len(city_map[0]) and city_map[x][y] != -1:
                new_cost = cost + city_map[x][y]
                new_path = path + [(x, y)]
                heapq.heappush(pq, (new_cost, (x, y), new_path))

# Find the shortest path that satisfies the conditions
for d1 in districts[1]:
    for d2 in districts[2]:
        for d3 in districts[3]:
            path1 = dijkstra(start, d1)
            path2 = dijkstra(d1, d2)
            path3 = dijkstra(d2, d3)
            path4 = dijkstra(d3, end)
            
            if path1 and path2 and path3 and path4:
                final_path = path1 + path2[1:] + path3[1:] + path4[1:]
                print(final_path)
                break
