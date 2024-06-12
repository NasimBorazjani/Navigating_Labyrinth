
import heapq

# Define the city map
city_map = [
    [7, -1, 19, 11, 6, -1, 4, 15, 9, 3],
    [-1, -1, 13, -1, 8, 17, -1, -1, 12, 16],
    [-1, -1, 2, -1, 15, 8, -1, 13, 4, -1],
    [13, 11, 3, 3, 3, -1, -1, -1, -1, -1],
    [1, 16, 14, 6, 14, 17, 4, 9, 1, -1],
    [-1, 4, 9, -1, 17, 17, -1, 13, 2, 9],
    [-1, -1, -1, -1, 5, 14, 17, 12, 7, 14],
    [-1, 15, 1, 6, -1, -1, 5, -1, -1, 1],
    [-1, -1, 19, -1, -1, -1, -1, -1, 13, 8],
    [-1, 6, 9, 12, 8, 8, -1, 18, -1, -1]
]

# Define the districts
districts = {
    1: [(0, 3)],
    2: [(4, 4)],
    3: [(5, 9)]
}

# Define the start and end workshops
start = (5, 9)
end = (3, 1)

# Define the directions
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
            
            if 0 <= x < len(city_map) and 0 <= y < len(city_map[0]) and city_map[x][y] != -1:
                new_cost = cost + city_map[x][y]
                new_path = path + [(x, y)]
                heapq.heappush(pq, (new_cost, (x, y), new_path))

# Find the shortest path that satisfies the conditions
path = None
for d1 in districts[1]:
    for d2 in districts[2]:
        for d3 in districts[3]:
            path1 = shortest_path(start, d1)
            path2 = shortest_path(d1, d2)
            path3 = shortest_path(d2, d3)
            path4 = shortest_path(d3, end)
            
            if path1 and path2 and path3 and path4:
                path = path1 + path2[1:] + path3[1:] + path4[1:]
                break

# Print the result
print(path)
