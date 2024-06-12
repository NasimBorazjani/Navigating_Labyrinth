
import heapq

# Define the matrix map of the city
city_map = [
    [19, 'x', 3, 'x', 'x', 'x', 13, 'x', 12, 'x'],
    ['x', 'x', 8, 'x', 15, 18, 11, 12, 'x', 7],
    ['x', 8, 'x', 'x', 15, 20, 17, 12, 2, 8],
    ['x', 'x', 4, 13, 2, 14, 19, 13, 15, 19],
    [13, 2, 'x', 8, 'x', 17, 13, 'x', 'x', 12],
    [2, 20, 20, 14, 'x', 'x', 15, 'x', 2, 19],
    [15, 16, 18, 'x', 2, 'x', 'x', 'x', 'x', 'x'],
    [2, 'x', 17, 'x', 'x', 12, 'x', 'x', 3, 'x'],
    [2, 'x', 10, 'x', 6, 'x', 'x', 9, 8, 19],
    [17, 'x', 6, 13, 'x', 18, 'x', 3, 'x', 18]
]

# Define the districts
districts = {
    1: (0, 2),
    2: (3, 5),
    3: (6, 9)
}

# Define the start and end workshops
start = (3, 8)
end = (6, 0)

# Define the directions Ben can move
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Function to find the shortest path using Dijkstra's algorithm
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
for d1 in range(districts[1][0], districts[1][1] + 1):
    for d2 in range(districts[2][0], districts[2][1] + 1):
        for d3 in range(districts[3][0], districts[3][1] + 1):
            new_path = shortest_path(start, (d1, d2), (d2, d3), end)
            if new_path and (not path or len(new_path) < len(path)):
                path = new_path

print(path)
