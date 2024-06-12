
from queue import Queue

# Define the grid of trampolines
grid = [
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
]

# Define the starting and ending positions
start = (6, 11)
end = (0, 0)

# Define the possible moves
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Function to check if a position is valid and not broken
def is_valid_move(row, col):
    return 0 <= row < 12 and 0 <= col < 12 and grid[row][col] == 0

# Function to find the shortest path using BFS
def find_shortest_path(start, end):
    q = Queue()
    q.put([start])
    
    while not q.empty():
        path = q.get()
        current = path[-1]
        
        if current == end:
            return path
        
        for move in moves:
            new_row = current[0] + move[0]
            new_col = current[1] + move[1]
            
            if is_valid_move(new_row, new_col):
                new_path = list(path)
                new_path.append((new_row, new_col))
                q.put(new_path)

# Find the shortest path from start to end
shortest_path = find_shortest_path(start, end)

# Print the shortest path
print(shortest_path)
