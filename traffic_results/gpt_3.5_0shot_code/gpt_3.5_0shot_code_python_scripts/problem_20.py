
import heapq

# Define the matrix map of the city
city_map = [
    [19, 'x', 7, 'x', 12, 'x', 15, 5, 19, 14],
    [17, 'x', 3, 5, 7, 'x', 'x', 'x', 17, 20],
    ['x', 11, 15, 8, 'x', 16, 4, 'x', 1, 1],
    ['x', 8, 19, 4, 3, 3, 3, 17, 8, 15],
    [13, 10, 17, 17, 6, 1, 'x', 8, 13, 20],
    [20, 'x', 'x', 'x', 'x', 4, 18, 4, 17, 'x'],
    [5, 'x', 'x', 10, 'x', 'x', 14, 2, 5, 'x'],
    [7, 'x', 4, 'x', 'x', 'x', 15, 'x', 'x', 'x'],
    [18, 'x', 18, 'x', 4, 'x', 'x', 'x', 17, 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 13, 'x', 'x']
]

# Define the districts
districts = {
    1: [(0, 0), (0, 1), (0, 2), (0, 3)],
    2: [(4, 0), (4, 1)],
    3: [(6, 0), (6, 1), (6, 2), (6, 3)]
}

# Define the start and end workshops
start = (6, 0)
end = (4, 9)

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
            
            if 0 <= x < len(city_map) and 0 <= y < len(city_map[0]) and city_map[x][y] != 'x' and (x, y) not in visited:
                new_cost = cost + city_map[x][y]
                heapq.heappush(pq, (new_cost, (x, y), path + [(x, y)]))
    
    return None

# Find the shortest path that satisfies the conditions
for workshop in districts[1]:
    path1 = dijkstra(start, workshop)
    for workshop in districts[2]:
        path2 = dijkstra(path1[-1], workshop)
        for workshop in districts[3]:
            path3 = dijkstra(path2[-1], workshop)
            if path3 and path3[-1] == end:
                print(path1 + path2 + path3)
                break
