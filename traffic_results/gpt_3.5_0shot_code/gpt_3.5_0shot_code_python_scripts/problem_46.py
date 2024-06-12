
import heapq

# Define the matrix map of the city
city_map = [
    [3, 14, 2, 'x', 'x', 'x', 19, 13, 17, 12, 8, 'x'],
    [1, 2, 13, 1, 4, 19, 'x', 'x', 16, 'x', 'x', 12],
    [9, 8, 9, 15, 'x', 12, 'x', 'x', 'x', 'x', 'x', 14],
    [11, 1, 10, 18, 'x', 16, 1, 'x', 12, 'x', 'x', 'x'],
    [7, 16, 13, 10, 13, 'x', 14, 'x', 'x', 9, 'x', 7],
    [19, 7, 7, 20, 13, 14, 18, 'x', 'x', 7, 5, 'x'],
    [4, 'x', 11, 'x', 'x', 2, 7, 1, 5, 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 18, 'x', 1, 'x'],
    [4, 'x', 'x', 9, 19, 2, 18, 8, 16, 14, 19, 7],
    ['x', 'x', 'x', 'x', 9, 'x', 17, 17, 1, 2, 2, 15],
    [18, 'x', 'x', 'x', 'x', 'x', 'x', 11, 10, 'x', 17, 'x'],
    [9, 'x', 'x', 'x', 10, 3, 'x', 'x', 13, 'x', 2, 'x']
]

# Define the districts
districts = {
    1: [(0, 0), (1, 0)],
    2: [(2, 0), (7, 11)],
    3: [(8, 0), (11, 10)]
}

# Define the possible movements
movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

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
        
        for dx, dy in movements:
            x, y = current
            new_x, new_y = x + dx, y + dy
            
            if 0 <= new_x < len(city_map) and 0 <= new_y < len(city_map[0]) and city_map[new_x][new_y] != 'x':
                new_cost = cost + city_map[new_x][new_y]
                heapq.heappush(pq, (new_cost, (new_x, new_y), path + [(new_x, new_y)]))
    
    return None

# Find the shortest path that satisfies the conditions
path = None
for workshop1 in districts[1]:
    for workshop2 in districts[2]:
        for workshop3 in districts[3]:
            path1 = shortest_path((1, 0), workshop1)
            path2 = shortest_path(workshop1, workshop2)
            path3 = shortest_path(workshop2, workshop3)
            
            if path1 and path2 and path3:
                path = path1 + path2[1:] + path3[1:]
                break

if path:
    print(path)
else:
    print("No valid path found")
