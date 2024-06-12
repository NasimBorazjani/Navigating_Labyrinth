
import numpy as np
from queue import Queue

# Define the grid
grid = np.array([[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                 [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
                 [0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1],
                 [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
                 [1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
                 [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
                 [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                 [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0],
                 [1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0],
                 [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
                 [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                 [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
                 [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0],
                 [0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0]])

# Define the starting and ending positions
start = (0, 4)
end = (13, 12)

# Define the possible moves
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Function to check if a position is valid
def is_valid_position(pos):
    return 0 <= pos[0] < 14 and 0 <= pos[1] < 14

# Function to find the shortest path
def find_shortest_path(grid, start, end, moves):
    q = Queue()
    q.put((start, [start]))
    
    while not q.empty():
        current, path = q.get()
        
        if current == end:
            return path
        
        for move in moves:
            new_pos = (current[0] + move[0], current[1] + move[1])
            if is_valid_position(new_pos) and grid[new_pos[0], new_pos[1]] == 0:
                new_path = path.copy()
                new_path.append(new_pos)
                q.put((new_pos, new_path))

# Find the shortest path
shortest_path = find_shortest_path(grid, start, end, moves)

# Print the shortest path
print(shortest_path)
