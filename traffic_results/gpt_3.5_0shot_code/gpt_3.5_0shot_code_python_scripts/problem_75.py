
import heapq

# Define the matrix map of the city
city_map = [
    ['x', 9, 4, 8, 'x', 'x', 4, 'x', 8, 12, 'x', 'x', 14],
    [17, 'x', 3, 'x', 6, 'x', 12, 2, 'x', 'x', 'x', 5, 19],
    ['x', 8, 8, 'x', 5, 'x', 15, 14, 14, 3, 10, 12, 3],
    [4, 'x', 16, 'x', 'x', 11, 12, 'x', 'x', 6, 5, 18, 19],
    ['x', 4, 9, 17, 'x', 'x', 'x', 13, 4, 7, 'x', 2, 16],
    [3, 6, 'x', 'x', 'x', 10, 5, 'x', 18, 10, 9, 20, 4],
    ['x', 'x', 'x', 14, 18, 'x', 'x', 'x', 'x', 16, 'x', 'x', 4],
    [14, 12, 'x', 4, 12, 11, 19, 'x', 3, 2, 'x', 13, 'x'],
    [19, 6, 2, 18, 'x', 'x', 8, 7, 1, 12, 19, 'x', 'x'],
    ['x', 9, 16, 17, 5, 12, 19, 8, 'x', 3, 10, 'x', 'x'],
    ['x', 10, 3, 'x', 14, 16, 2, 16, 4, 10, 18, 15, 'x'],
    [15, 5, 5, 'x', 13, 'x', 3, 7, 'x', 4, 1, 17, 15],
    [5, 2, 6, 'x', 'x', 'x', 'x', 8, 16, 'x', 'x', 'x', 'x']
]

# Define the districts
districts = {
    1: (0, 2),
    2: (3, 7),
    3: (8, 12)
}

# Define the start and end workshops
start = (7, 1)
end = (2, 10)

# Define the directions
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

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
        
        for dx, dy in directions:
            x, y = current[0] + dx, current[1] + dy
            
            if 0 <= x < len(city_map) and 0 <= y < len(city_map[0]) and city_map[x][y] != 'x':
                new_cost = cost + city_map[x][y]
                new_path = path + [(x, y)]
                heapq.heappush(pq, (new_cost, (x, y), new_path))

# Find the shortest path that satisfies the conditions
path = None
for d1 in range(districts[1][0], districts[1][1] + 1):
    for d2 in range(districts[2][0], districts[2][1] + 1):
        for d3 in range(districts[3][0], districts[3][1] + 1):
            new_path = shortest_path(start, (d1, d2)) + shortest_path((d1, d2), (d3, d2)) + shortest_path((d3, d2), end)
            if path is None or sum(city_map[x][y] for x, y in new_path) < sum(city_map[x][y] for x, y in path):
                path = new_path

print(path)
