
import heapq

# Define the matrix map of the city
city_map = [
    ['x', 7, 7, 12, 7, 'x', 13, 1, 18],
    [9, 18, 'x', 4, 19, 8, 'x', 15, 10],
    [9, 'x', 10, 5, 5, 9, 8, 'x', 'x'],
    [14, 4, 19, 9, 14, 'x', 'x', 7, 9],
    [9, 4, 11, 15, 7, 'x', 17, 3, 'x'],
    [11, 'x', 2, 18, 15, 15, 'x', 'x', 'x'],
    ['x', 5, 10, 'x', 'x', 13, 'x', 9, 'x'],
    [3, 'x', 2, 'x', 12, 'x', 'x', 'x', 4],
    ['x', 'x', 7, 'x', 19, 'x', 'x', 'x', 9]
]

# Define the districts
districts = {
    1: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
    2: [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
    3: [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)]
}

# Define the start and end workshops
start = (6, 1)
end = (2, 6)

# Define the possible movements
movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Define a function to calculate the distance between two workshops
def distance(workshop1, workshop2):
    return abs(workshop1[0] - workshop2[0]) + abs(workshop1[1] - workshop2[1])

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
        
        for move in movements:
            new_pos = (current[0] + move[0], current[1] + move[1])
            
            if 0 <= new_pos[0] < len(city_map) and 0 <= new_pos[1] < len(city_map[0]) and city_map[new_pos[0]][new_pos[1]] != 'x':
                new_cost = cost + city_map[new_pos[0]][new_pos[1]]
                heapq.heappush(pq, (new_cost, new_pos, path + [new_pos]))
    
    return None

# Find the shortest path that satisfies the conditions
path = None
for workshop1 in districts[1]:
    for workshop2 in districts[2]:
        for workshop3 in districts[3]:
            path1 = shortest_path(start, workshop1)
            path2 = shortest_path(workshop1, workshop2)
            path3 = shortest_path(workshop2, workshop3)
            path4 = shortest_path(workshop3, end)
            
            if path1 and path2 and path3 and path4:
                path = path1 + path2[1:] + path3[1:] + path4[1:]
                break

if path:
    print(path)
else:
    print("No valid path found")
