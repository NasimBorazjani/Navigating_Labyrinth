
from collections import deque

# Define the matrix map of the city
city_map = [
    [0, 0, 11, 16, 0, 0, 0, 0, 4, 0, 14, 5, 0, 0],
    [3, 1, 13, 0, 0, 14, 11, 0, 0, 15, 12, 15, 0, 0],
    [17, 15, 17, 10, 11, 0, 7, 1, 1, 14, 0, 9, 0, 0],
    [8, 0, 0, 13, 2, 12, 0, 8, 0, 0, 9, 13, 19, 5],
    [4, 0, 2, 3, 8, 0, 0, 17, 0, 0, 16, 10, 0, 0],
    [0, 0, 0, 0, 3, 13, 14, 16, 18, 11, 4, 19, 20, 0],
    [0, 11, 0, 0, 3, 10, 8, 9, 18, 7, 1, 14, 0, 6],
    [11, 0, 12, 11, 0, 11, 10, 3, 10, 12, 15, 0, 11, 0],
    [0, 0, 4, 18, 0, 0, 13, 0, 14, 10, 0, 8, 0, 17],
    [0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 18, 19, 18],
    [19, 4, 0, 2, 14, 2, 0, 9, 0, 10, 7, 17, 4, 12],
    [13, 2, 0, 0, 18, 5, 0, 11, 0, 0, 0, 18, 0, 0],
    [0, 0, 13, 1, 13, 0, 2, 0, 0, 0, 0, 0, 0, 14],
    [0, 12, 0, 0, 0, 0, 0, 0, 19, 0, 0, 9, 1, 0]
]

# Define the districts
districts = {
    1: [(0, 0), (0, 1), (0, 2), (0, 3)],
    2: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)],
    3: [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13)]
}

# Define the start and end workshops
start_workshop = (3, 0)
end_workshop = (5, 12)

# Perform breadth-first search to find the shortest path
def bfs(start, end):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        current, path = queue.popleft()
        
        if current == end:
            return path
        
        visited.add(current)
        
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return None

# Get valid neighbors of a workshop
def get_neighbors(workshop):
    row, col = workshop
    neighbors = []
    
    if row > 0 and city_map[row - 1][col] != 0:
        neighbors.append((row - 1, col))
    if row < len(city_map) - 1 and city_map[row + 1][col] != 0:
        neighbors.append((row + 1, col))
    if col > 0 and city_map[row][col - 1] != 0:
        neighbors.append((row, col - 1))
    if col < len(city_map[0]) - 1 and city_map[row][col + 1] != 0:
        neighbors.append((row, col + 1))
    
    return neighbors

# Find the shortest path that satisfies the district requirements
path = None
for workshop_1 in districts[1]:
    for workshop_2 in districts[2]:
        for workshop_3 in districts[3]:
            path_1 = bfs(start_workshop, workshop_1)
            path_2 = bfs(workshop_1, workshop_2)
            path_3 = bfs(workshop_2, workshop_3)
            path_4 = bfs(workshop_3, end_workshop)
            
            if path_1 and path_2 and path_3 and path_4:
                path = path_1 + path_2[1:] + path_3[1:] + path_4[1:]
                break

if path:
    print(path)
else:
    print("No valid path found.")
