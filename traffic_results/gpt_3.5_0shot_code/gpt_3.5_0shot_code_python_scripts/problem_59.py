
import heapq

# Define the matrix map of the city
city_map = [
    [4, 1, 20, 15, 9, 'x', 8, 6, 'x', 'x', 14, 'x'],
    [5, 11, 9, 12, 10, 4, 15, 18, 7, 'x', 'x', 13],
    [15, 9, 1, 'x', 18, 3, 1, 19, 'x', 'x', 17, 17],
    ['x', 17, 11, 10, 'x', 19, 8, 'x', 'x', 'x', 'x', 7],
    [5, 'x', 1, 'x', 14, 13, 4, 8, 5, 'x', 13, 14],
    [16, 6, 'x', 'x', 'x', 17, 'x', 15, 4, 'x', 'x', 15],
    ['x', 'x', 'x', 15, 'x', 19, 10, 'x', 16, 18, 11, 1],
    [6, 8, 'x', 3, 'x', 5, 5, 'x', 3, 8, 9, 14],
    [10, 14, 'x', 'x', 'x', 'x', 'x', 'x', 6, 2, 'x', 'x'],
    [12, 'x', 'x', 6, 11, 4, 'x', 'x', 12, 'x', 4, 16],
    [4, 'x', 'x', 'x', 11, 'x', 'x', 'x', 18, 16, 'x', 10],
    ['x', 6, 'x', 'x', 11, 'x', 5, 13, 8, 1, 17, 9]
]

# Define the districts
districts = {
    1: [(0, 0), (0, 1)],
    2: [(2, 0), (6, 11)],
    3: [(7, 8), (11, 11)]
}

# Define the directions Ben can move
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Define a function to find the shortest path using Dijkstra's algorithm
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
path = None
for workshop1 in districts[1]:
    for workshop2 in districts[2]:
        for workshop3 in districts[3]:
            path1 = shortest_path((2, 0), workshop1)
            path2 = shortest_path(workshop1, workshop2)
            path3 = shortest_path(workshop2, workshop3)
            
            if path1 and path2 and path3:
                path = path1 + path2[1:] + path3[1:]
                break
        if path:
            break

print(path)
