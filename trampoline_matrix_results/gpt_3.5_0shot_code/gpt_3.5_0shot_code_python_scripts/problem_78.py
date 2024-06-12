
import numpy as np
from queue import Queue

# Define the grid with broken and functional trampolines
grid = np.array([[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
                 [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
                 [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
                 [0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                 [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                 [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1],
                 [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                 [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
                 [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]])

# Define the starting and ending positions
start = (4, 13)
end = (6, 0)

# Define the possible moves
moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

# Perform BFS to find the shortest path
def bfs(grid, start, end):
    q = Queue()
    q.put([start])
    
    while not q.empty():
        path = q.get()
        node = path[-1]
        
        if node == end:
            return path
        
        for move in moves:
            new_node = (node[0] + move[0], node[1] + move[1])
            if 0 <= new_node[0] < grid.shape[0] and 0 <= new_node[1] < grid.shape[1] and grid[new_node[0], new_node[1]] == 0 and new_node not in path:
                new_path = list(path)
                new_path.append(new_node)
                q.put(new_path)

# Find the shortest path
shortest_path = bfs(grid, start, end)

# Print the shortest path
print(shortest_path)
