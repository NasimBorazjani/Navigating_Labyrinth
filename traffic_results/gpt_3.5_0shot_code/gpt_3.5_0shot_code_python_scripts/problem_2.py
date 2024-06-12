
import heapq

# Define the matrix map of the city
city_map = [
    ['x', 13, 9, 'x', 'x', 16, 6, 18, 7],
    ['x', 3, 11, 'x', 'x', 5, 7, 'x', 19],
    [8, 'x', 2, 5, 6, 12, 9, 10, 7],
    [12, 1, 6, 20, 19, 18, 12, 'x', 14],
    [16, 5, 10, 3, 'x', 'x', 'x', 1, 9],
    ['x', 3, 'x', 'x', 'x', 'x', 'x', 'x', 4],
    [7, 10, 'x', 1, 'x', 'x', 17, 'x', 8],
    ['x', 5, 'x', 'x', 'x', 17, 'x', 9, 'x'],
    [13, 16, 8, 15, 'x', 2, 'x', 1, 2]
]

# Define the districts
districts = {
    1: [(0, 0), (0, 1)],
    2: [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
    3: [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]
}

# Define the start and end workshops
start = (2, 2)
end = (5, 8)

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
            x, y = current[0] + dx, current[1] + dy
            
            if 0 <= x < len(city_map) and 0 <= y < len(city_map[0]) and city_map[x][y] != 'x' and (x, y) not in visited:
                new_cost = cost + city_map[x][y]
                heapq.heappush(pq, (new_cost, (x, y), path + [(x, y)]))
    
    return None

# Find the shortest path that satisfies the conditions
path = None
for workshop in districts[1]:
    for workshop2 in districts[2]:
        for workshop3 in districts[3]:
            path1 = dijkstra(start, workshop)
            path2 = dijkstra(workshop, workshop2)
            path3 = dijkstra(workshop2, workshop3)
            path4 = dijkstra(workshop3, end)
            
            if path1 and path2 and path3 and path4:
                path = path1 + path2[1:] + path3[1:] + path4[1:]
                break

if path:
    print(path)
else:
    print("No valid path found.")
