
import heapq

# Define the matrix map of the city
city_map = [
    ['x', 10, 16, 12, 'x', 'x', 'x', 'x', 18, 18, 10, 'x', 'x', 19],
    [7, 'x', 'x', 11, 5, 13, 6, 'x', 'x', 'x', 'x', 'x', 8, 14],
    ['x', 15, 6, 20, 4, 9, 16, 9, 16, 'x', 11, 'x', 'x', 9],
    [1, 16, 'x', 'x', 'x', 6, 15, 1, 10, 10, 9, 4, 'x', 4],
    ['x', 'x', 'x', 1, 12, 'x', 12, 17, 'x', 'x', 13, 'x', 'x', 2],
    ['x', 'x', 9, 'x', 'x', 'x', 'x', 17, 'x', 'x', 'x', 'x', 10, 11],
    [7, 'x', 7, 12, 'x', 'x', 'x', 2, 2, 8, 10, 8, 'x', 'x'],
    [3, 3, 'x', 16, 11, 'x', 4, 6, 'x', 'x', 4, 17, 13, 16],
    [4, 15, 'x', 'x', 'x', 'x', 'x', 'x', 11, 19, 16, 'x', 'x', 'x'],
    [10, 5, 17, 'x', 2, 'x', 'x', 3, 10, 3, 12, 'x', 8, 'x'],
    ['x', 17, 12, 'x', 'x', 'x', 6, 2, 13, 'x', 'x', 'x', 'x', 'x'],
    ['x', 10, 'x', 'x', 15, 'x', 'x', 'x', 8, 'x', 3, 'x', 'x', 19],
    [1, 7, 'x', 'x', 16, 'x', 'x', 'x', 3, 15, 10, 12, 6, 8],
    ['x', 'x', 'x', 'x', 9, 'x', 'x', 'x', 7, 'x', 'x', 'x', 'x', 8]
]

# Define the districts
districts = {
    1: [(0, 0), (0, 1), (0, 2)],
    2: [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)],
    3: [(9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13)]
}

# Define the start and end workshops
start = (9, 10)
end = (2, 3)

# Define the directions
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Define a function to calculate the shortest path using Dijkstra's algorithm
def dijkstra(start, end):
    heap = [(0, start, [start])]
    visited = set()
    
    while heap:
        (cost, current, path) = heapq.heappop(heap)
        
        if current == end:
            return path
        
        if current in visited:
            continue
        
        visited.add(current)
        
        for dx, dy in directions:
            x, y = current[0] + dx, current[1] + dy
            
            if 0 <= x < len(city_map) and 0 <= y < len(city_map[0]) and city_map[x][y] != 'x':
                new_cost = cost + city_map[x][y]
                heapq.heappush(heap, (new_cost, (x, y), path + [(x, y)]))
    
    return None

# Find the shortest path that satisfies the conditions
shortest_path = None
for workshop in districts[1]:
    path1 = dijkstra(start, workshop)
    if path1:
        for workshop in districts[2]:
            path2 = dijkstra(path1[-1], workshop)
            if path2:
                for workshop in districts[3]:
                    path3 = dijkstra(path2[-1], workshop)
                    if path3 and (not shortest_path or len(path1 + path2 + path3) < len(shortest_path)):
                        shortest_path = path1 + path2 + path3

print(shortest_path)
