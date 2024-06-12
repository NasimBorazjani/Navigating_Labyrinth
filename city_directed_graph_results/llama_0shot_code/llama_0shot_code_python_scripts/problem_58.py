
from collections import deque

matrix = [
    "010001011000",
    "000101000000",
    "010001000000",
    "010000000011",
    "011000100011",
    "000010000100",
    "100000100011",
    "010001000000",
    "000000001001",
    "010000100000",
    "100011000011",
    "011000011000",
]

cities = "BKSTXTPQMREGJVE"

# Convert the adjacency matrix to a dictionary
graph = {cities[i]: {cities[j]: (1 if matrix[i][j] == '1' else 0) for j in range(len(matrix[i]))} for i in range(len(matrix))}

destinations = ['B', 'V']

# Create a queue for BFS and a visited set
queue = deque(['S'])
visited = set('S')

# Function to find the shortest path
def shortest_path(graph, queue, visited, destinations):
    while queue:
        city = queue.popleft()
        for dest in destinations:
            if city == dest and visited.count(dest) == 1:
                return True
        for neighbor, val in graph[city].items():
            if val == 1 and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return False

# Check if there is a solution
if not shortest_path(graph, queue, visited, destinations):
    print("No solution")
else:
    print("Path:", 'S' + ''.join(queue))
