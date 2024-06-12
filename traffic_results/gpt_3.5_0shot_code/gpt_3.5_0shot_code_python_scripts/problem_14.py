
import heapq

# Define the matrix map of the city
city_map = [
    ['x', 3, 13, 18, 'x', 'x', 3, 'x', 'x'],
    ['x', 3, 'x', 'x', 18, 1, 13, 'x', 'x'],
    ['x', 'x', 'x', 6, 'x', 13, 'x', 11, 1],
    [4, 3, 'x', 'x', 'x', 'x', 6, 6, 11],
    [14, 16, 'x', 'x', 'x', 'x', 'x', 18, 11],
    [14, 'x', 11, 'x', 'x', 4, 'x', 1, 'x'],
    [18, 7, 1, 'x', 8, 'x', 'x', 'x', 'x'],
    [4, 9, 6, 12, 13, 19, 'x', 14, 4],
    ['x', 'x', 17, 12, 7, 7, 9, 3, 1]
]

# Define the districts
districts = {
    1: [(0, 0), (3, 8)],
    2: [(4, 0), (6, 8)],
    3: [(7, 0), (8, 8)]
}

# Define the start and end workshops
start = (3, 1)
end = (7, 8)

# Define the directions Ben can move
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Function to calculate the shortest path using Dijkstra's algorithm
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
            
            if 0 <= new_x < len(city_map) and 0 <= new_y < len(city_map[0]) and city_map[new_x][new_y] != 'x':
                new_cost = cost + city_map[new_x][new_y]
                heapq.heappush(pq, (new_cost, (new_x, new_y), path + [(new_x, new_y)]))
    
    return None

# Find the shortest path that satisfies the conditions
for district in districts.values():
    for workshop in district:
        path1 = dijkstra(start, workshop)
        path2 = dijkstra(workshop, end)
        
        if path1 and path2:
            path = path1 + path2[1:]
            print(path)
            break
