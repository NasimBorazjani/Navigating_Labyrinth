
import numpy as np
from queue import Queue

# Define the grid
grid = np.array([[0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                 [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                 [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
                 [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
                 [0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
                 [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
                 [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
                 [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
                 [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
                 [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1]])

# Define the starting and ending positions
start = (0, 13)
end = (8, 1)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# BFS to find the shortest path
def bfs(grid, start, end, moves):
    q = Queue()
    q.put([start])
    
    while not q.empty():
        path = q.get()
        current = path[-1]
        
        if current == end:
            return path
        
        for move in moves:
            new_pos = (current[0] + move[0], current[1] + move[1])
            if 0 <= new_pos[0] < grid.shape[0] and 0 <= new_pos[1] < grid.shape[1] and grid[new_pos[0], new_pos[1]] == 0:
                new_path = list(path)
                new_path.append(new_pos)
                q.put(new_path)
    
    return None

# Find the shortest path
shortest_path = bfs(grid, start, end, moves)

# Print the shortest path
print(shortest_path)
