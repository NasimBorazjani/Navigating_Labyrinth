
import heapq

# Define the matrix map of the city
city_map = [
    [13, 'x', 'x', 'x', 'x', 'x', 8, 'x', 'x', 6],
    ['x', 'x', 'x', 8, 10, 'x', 17, 'x', 15, 14],
    ['x', 6, 'x', 'x', 'x', 16, 12, 7, 8, 11],
    ['x', 15, 'x', 1, 11, 19, 9, 17, 'x', 'x'],
    [18, 20, 16, 19, 12, 1, 'x', 'x', 'x', 5],
    [11, 'x', 18, 14, 'x', 2, 'x', 9, 8, 1],
    ['x', 2, 5, 16, 3, 9, 2, 18, 'x', 'x'],
    ['x', 8, 15, 17, 16, 6, 'x', 3, 'x', 10],
    [3, 'x', 'x', 'x', 8, 9, 10, 'x', 6, 'x'],
    [6, 'x', 9, 16, 1, 3, 16, 18, 'x', 'x']
]

# Define the districts
districts = {
    1: [(0, 1), (1, 1)],
    2: [(2, 0), (4, 9)],
    3: [(5, 0), (9, 9)]
}

# Define the start and end workshops
start = (1, 8)
end = (4, 1)

# Define the directions
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Define a function to calculate the shortest path using Dijkstra's algorithm
def shortest_path(start, end):
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
            
            if 0 <= x < len(city_map) and 0 <= y < len(city_map[0]) and city_map[x][y] != 'x':
                new_cost = cost + city_map[x][y]
                heapq.heappush(pq, (new_cost, (x, y), path + [(x, y)]))
    
    return None

# Find the shortest path that satisfies the conditions
for district in districts.values():
    for workshop in district:
        path1 = shortest_path(start, workshop)
        path2 = shortest_path(workshop, end)
        
        if path1 and path2:
            print(path1 + path2)
            break
