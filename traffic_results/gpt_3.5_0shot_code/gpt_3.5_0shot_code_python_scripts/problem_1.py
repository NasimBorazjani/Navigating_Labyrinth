
import heapq

# Define the city map
city_map = [
    [13, 'x', 'x', 3, 10, 20, 3, 'x', 5],
    ['x', 'x', 'x', 'x', 20, 16, 'x', 'x', 17],
    [3, 14, 18, 8, 1, 20, 14, 'x', 7],
    [13, 3, 6, 10, 7, 4, 6, 6, 1],
    [10, 12, 2, 'x', 11, 'x', 10, 8, 11],
    ['x', 'x', 'x', 11, 6, 18, 13, 20, 17],
    ['x', 'x', 16, 'x', 4, 17, 7, 10, 15],
    ['x', 7, 16, 6, 19, 4, 7, 'x', 'x'],
    ['x', 11, 18, 'x', 'x', 'x', 3, 8, 'x']
]

# Define the districts
districts = {
    1: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)],
    2: [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2)],
    3: [(5, 0), (5, 1), (5, 2), (6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1)]
}

# Define the start and end workshops
start = (5, 7)
end = (2, 1)

# Define the possible movements
movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Define a function to calculate the distance between two workshops
def distance(w1, w2):
    return abs(w1[0] - w2[0]) + abs(w1[1] - w2[1])

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
for district1 in districts[1]:
    for district2 in districts[2]:
        for district3 in districts[3]:
            path1 = shortest_path(start, district1)
            path2 = shortest_path(district1, district2)
            path3 = shortest_path(district2, district3)
            path4 = shortest_path(district3, end)
            
            if path1 and path2 and path3 and path4:
                final_path = path1 + path2[1:] + path3[1:] + path4[1:]
                print(final_path)
                break
