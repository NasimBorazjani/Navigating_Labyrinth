
import heapq

# Define the matrix map of the city
city_map = [
    [5, 10, 'x', 'x', 'x', 16, 'x', 'x', 'x', 16, 'x', 10, 8, 'x'],
    [1, 'x', 13, 'x', 7, 'x', 'x', 'x', 10, 3, 3, 13, 18, 11],
    [14, 'x', 'x', 'x', 9, 16, 16, 15, 'x', 'x', 15, 'x', 4, 4],
    [15, 'x', 3, 'x', 'x', 17, 'x', 16, 10, 9, 'x', 6, 16, 17],
    [12, 8, 'x', 10, 'x', 'x', 13, 10, 'x', 'x', 6, 3, 'x', 1],
    ['x', 'x', 'x', 5, 8, 9, 6, 14, 1, 'x', 'x', 2, 12, 'x'],
    [13, 'x', 'x', 'x', 16, 6, 'x', 17, 12, 18, 'x', 17, 8, 'x'],
    [10, 'x', 14, 15, 'x', 'x', 'x', 20, 'x', 17, 18, 8, 'x', 4],
    ['x', 11, 3, 'x', 'x', 'x', 'x', 7, 'x', 4, 'x', 'x', 11, 2],
    [7, 'x', 'x', 10, 'x', 19, 'x', 7, 17, 'x', 'x', 14, 'x', 15],
    [12, 11, 'x', 'x', 9, 7, 'x', 15, 1, 5, 5, 11, 15, 'x'],
    ['x', 9, 9, 'x', 'x', 'x', 'x', 8, 'x', 8, 19, 11, 12, 12],
    ['x', 17, 5, 'x', 'x', 17, 'x', 'x', 12, 'x', 15, 12, 10, 'x'],
    [18, 'x', 'x', 'x', 3, 'x', 7, 'x', 8, 5, 12, 8, 10, 'x']
]

# Define the districts
districts = {
    1: [(0, 4)],
    2: [(5, 9)],
    3: [(10, 13)]
}

# Define the start and end workshops
start = (10, 12)
end = (4, 3)

# Define the directions Ben can move
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the priority queue with the start workshop
pq = [(0, start, [start])]

# Initialize a set to keep track of visited workshops
visited = set()

# Initialize a variable to store the shortest path
shortest_path = None

# Dijkstra's algorithm
while pq:
    time, current, path = heapq.heappop(pq)
    
    if current == end:
        if all(any(workshop in district for workshop in path) for district in districts.values()):
            shortest_path = path
            break
    
    visited.add(current)
    
    for dx, dy in directions:
        new_x, new_y = current[0] + dx, current[1] + dy
        
        if 0 <= new_x < len(city_map) and 0 <= new_y < len(city_map[0]) and city_map[new_x][new_y] != 'x' and (new_x, new_y) not in visited:
            new_time = time + city_map[new_x][new_y]
            new_path = path + [(new_x, new_y)]
            heapq.heappush(pq, (new_time, (new_x, new_y), new_path))

# Print the shortest path
print(shortest_path)
