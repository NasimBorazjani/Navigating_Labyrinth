
import heapq

# Define the matrix map of the city
city_map = [
    [0, 0, 0, 0, 9, 0, 20, 3, 9],
    [17, 11, 17, 0, 9, 2, 7, 0, 15],
    [0, 4, 2, 19, 12, 6, 0, 4, 17],
    [15, 0, 0, 15, 11, 19, 0, 9, 5],
    [3, 9, 19, 15, 2, 0, 0, 18, 0],
    [19, 5, 9, 11, 9, 0, 0, 3, 0],
    [0, 0, 2, 8, 8, 0, 0, 0, 19],
    [0, 0, 14, 0, 0, 0, 18, 0, 18],
    [0, 14, 18, 7, 8, 0, 10, 15, 0]
]

# Define the districts
districts = {
    1: [(0, 3), (1, 3), (2, 3), (3, 3)],
    2: [(4, 4)],
    3: [(5, 0), (6, 0), (7, 0), (8, 0)]
}

# Define the start and end workshops
start = (3, 7)
end = (5, 0)

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
            
            if 0 <= x < len(city_map) and 0 <= y < len(city_map[0]) and city_map[x][y] != 0 and (x, y) not in visited:
                new_cost = cost + city_map[x][y]
                heapq.heappush(pq, (new_cost, (x, y), path + [(x, y)]))
    
    return None

# Find the shortest path that satisfies the conditions
for d1 in districts[1]:
    for d2 in districts[2]:
        for d3 in districts[3]:
            path1 = shortest_path(start, d1)
            path2 = shortest_path(d1, d2)
            path3 = shortest_path(d2, d3)
            path4 = shortest_path(d3, end)
            
            if path1 and path2 and path3 and path4:
                final_path = path1 + path2[1:] + path3[1:] + path4[1:]
                print(final_path)
                break
